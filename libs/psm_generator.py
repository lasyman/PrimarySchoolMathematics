from libs.psm_help import *


class Generator(object):
    """
    题目生成器
    """
    def __init__(self, param):
        self.param = param
        self.__data_list = list()

    def __get_formula(self):
        """
        根据给出的属性返回一道合法的口算题
        :return:
        """

        f = []
        for i in range(self.param.step + 1):
            f.append(self.param.multistep[i])
        if self.param.step == 1:
            # 返回一步口算题
            return getOne(f, self.param.signum, self.param.multistep[4], self.param.carry,
                          self.param.abdication, self.param.is_result)
        elif self.param.step > 1:
            return getMoreStep(f, self.param.multistep[4], self.param.symbols, self.param.step, self.param.carry,
                               self.param.abdication, self.param.is_bracket, self.param.is_result)

    def generate_data(self):
        """
        根据条件生成所需口算题
        :return:
        """
        slist = list()
        while True:
            formula = self.__get_formula()  # 生成一道算式题
            if formula:
                slist.append(formula)
            if len(slist) == self.param.number:
                break

        random.shuffle(slist)  # 洗牌，先打乱list中的排序
        self.__data_list = random.sample(slist, self.param.number)  # 随机取需要的口算题量。
        return self.__data_list

    def produce(self):
        """
        打印预览预留接口
        """
        pass

    def test(self):
        """
        测试使用
        """
        pass

    def get_answer(self):
        """
        生成口算题答案
        """
        answer_list = []
        for item in self.__data_list:
            answer = item.replace("x", "*").replace("÷", "/").replace("=", "")
            r = eval(answer)
            if re.match("\d+\.0$", str(r)):
                answer += "=" + str(int(r))
            else:
                answer += "=" + str(r)
            answer_list.append(answer.replace("*", "x").replace("/", "÷"))
        return answer_list
