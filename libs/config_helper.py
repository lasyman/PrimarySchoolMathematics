import configparser
from params import Params
from libs.units import (
    get_user_path,
)


class CfgHelper(object):
    """
    读取ini配置帮助类
    """
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cfg_file = None

    def init_data(self):
        """
        初始化默认配置
        """
        config_path = get_user_path() / "psm"
        self.cfg_file = config_path / "sys.cfg"
        self.cf.read(self.cfg_file)
        if not config_path.exists():
            config_path.mkdir()
        if not self.cfg_file.exists():
            self.create_default_cfg()

    def create_default_cfg(self):
        """
        创建默认配置
        :return:
        """
        param = Params()
        self.update_param_to_cfg("config", param)

    def update_param_to_cfg(self, section, param: Params):
        """
        更新字典到配置文件
        :param section:
        :param param:
        :return:
        """
        if not self.cf.has_section(section):
            self.cf.add_section(section)
        for key, value in param.to_dict().items():
            self.cf.set(section, key, str(value))
        with open(self.cfg_file, "w") as conf:
            self.cf.write(conf)

    def set_cfg(self, section, key, value):
        """
        添加或者更新配置
        """
        if not self.cf.has_section(section):
            self.cf.add_section(section)

        self.cf.set(section, key, value)

        with open(self.cfg_file, "w") as conf:
            self.cf.write(conf)

    def get_cfg(self, section, key):
        """
        读取配置
        """
        if not self.cf.has_section(section):
            return ""

        return self.cf.get(section, key)

    def get_options(self, section):
        """
        获取某个scetion的keys
        """
        keys = list()
        if self.cf.has_section(section):
            keys = self.cf.options(section)

        return keys


cfg = CfgHelper()
cfg.init_data()
