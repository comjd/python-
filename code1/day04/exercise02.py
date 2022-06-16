"""
    文件复制
"""


class FileOperation:

    def file_copy(self, old_name, new_name):
        """
             复制文件
        :param old_name:
        :param new_name:
        :return:
        """
        try:
            with open(new_name, 'wb'):
                pass
        except FileNotFoundError as e:
            print(e)
            return False
        for line in self.__red_file(old_name):
            self.__write_file(new_name, line)
            # print(line.decode(), end='')
        print('复制成功')
        return True

    @staticmethod
    def __red_file(old_name):
        """
            每次读取一行文件
        :param old_name:
        :return:
        """
        try:
            with open(old_name, 'rb') as fr:
                for line in fr:
                    yield line
        except FileNotFoundError as e:
            print(e)

    @staticmethod
    def __write_file(new_name, value):
        with open(new_name, 'ab') as wf:
            wf.write(value)


if __name__ == '__main__':
    f = FileOperation()
    f.file_copy('/home/tyler/图片/1.jpeg', '2.jpeg')
