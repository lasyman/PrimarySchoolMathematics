from libs.units import get_desktop_path


class Params(object):
    """
    参数类
    """
    signum = 1
    step = 1
    is_result = 0
    is_bracket = 0
    multistep = [[1, 9], [1, 9], [1, 9], [1, 99], [1, 81]]
    symbols = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    number = 5
    juanzishu = 1
    lieshu = 4
    jz_title = "小学生数学计算题"
    inf_title = "姓名：__________ 日期：____月____日 时间：________ 对题：____道"
    carry = 1
    abdication = 2
    out_put = get_desktop_path()

    def to_dict(self):
        """
        转换为字典类型
        :return:
        """
        data = dict()
        data["signum"] = self.signum
        data["step"] = self.step
        data["is_result"] = self.is_result
        data["is_bracket"] = self.is_bracket
        data["multistep"] = self.multistep
        data["symbols"] = self.symbols
        data["number"] = self.number
        data["juanzishu"] = self.juanzishu
        data["lieshu"] = self.lieshu
        data["jz_title"] = self.jz_title
        data["inf_title"] = self.inf_title
        data["carry"] = self.carry
        data["abdication"] = self.abdication
        data["out_put"] = self.out_put
        return data
