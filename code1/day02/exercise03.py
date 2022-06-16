"""
    检查字符串中的空格是否完全匹配
"""
from day02.linkstack import LinkStack, LinkNode


class CheckCharPair:
    """
        检查字符串的单个特殊符号是否成对出现
    """

    def __init__(self, all_key="()[]{}<>《》"):
        self.__all_key = all_key
        # 找出所有字符串的左侧字符，用于判断遇到左侧字符入站操作
        self.__left_key = [char for i, char in enumerate(all_key) if i % 2 == 0]
        # 将每个配套的字符生成字典，右侧的字符为键，左侧的字符为值，用于遇到右侧字符时，弹出站的第一个元素，匹配键对应的值是否与弹出元素的值相同
        self.__dick = {char: all_key[i - 1] for i, char in enumerate(all_key) if i % 2 == 1}
        self.ls = LinkStack()
        self.temp = None

    def traversal_str(self, text):
        if text == '':
            return
        index = 0
        while True:
            # 当下标的进度及当前字符串不在被检查的字符中时，下标往后移动一位
            while index < len(text) and text[index] not in self.__all_key:
                index += 1
            if index < len(text):
                # 当前的字符是左侧字符时，将左侧字符入站
                if text[index] in self.__left_key:
                    self.ls.push((text[index], index))
                # 当前的字符是右侧字符时，栈中第一个元素出栈
                elif text[index] in self.__dick:
                    self.temp = None
                    if not self.ls.is_empty():
                        # 栈中第一个元素出栈
                        self.temp = self.ls.pop()
                        # 栈中第一个元素与当前字符的键对应的值不相等时，将左侧元素返回
                        if self.temp.value[0] != self.__dick[text[index]]:
                            yield self.temp
                    else:
                        yield LinkNode((text[index], index))
                index += 1
            else:
                # 　字符串被匹配完后，判断栈中是否存在未匹配上的元素
                if not self.ls.is_empty():
                    yield self.ls.pop()
                else:
                    return

    def check_result(self, text):
        for node in self.traversal_str(text):
            print(node.value[0], node.value[1])


if __name__ == '__main__':
    ck = CheckCharPair()
    ck.check_result(
        ']})(本)(教[[)程适合}想从零(开始)学习( Python [编程语]言的开发人员)。{当然《本教程}也《会》《对《一些模块》》进行深入，{让你更好的了解} Python 的应用。本教程主要针对 Pytho[n] 2.x 版本的学习，如果你使用的是 (Python 3.x 版本请)移步至Python 3.X 版本的教程。本教程所有实例基于 Python2.7。')
