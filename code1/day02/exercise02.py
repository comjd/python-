from day02.linkstack import LinkStack


class StackTest:
    def __init__(self):
        self.__stack = LinkStack()
        self.numer1 = 0
        self.numer2 = 0

    def operation(self):
        while True:
            str_input = input('')
            for item in str_input.split():
                print(item, '-----')
                if item.isdigit():
                    self.__push(item)
                elif item == '+':
                    self.__calcul('+')
                elif item == '-':
                    self.__calcul('-')
                elif item == '*':
                    self.__calcul('*')
                elif item == '/':
                    self.__calcul('/')
                elif item == 'P':
                    self.__pop()
                elif item == 'f':
                    self.__show()
                elif item == 'p':
                    self.__show_top()

    def __push(self, value):
        self.__stack.push(value)

    def __show(self):
        self.__stack.show()

    def __show_top(self):
        if self.__stack.top is not None:
            print(self.__stack.top.value)

    def __pop(self):
        return self.__stack.pop()

    def __calcul(self, operation):
        if self.__stack.top is not None and self.__stack.top.next is not None:
            if self.__stack.top.value == '0' and operation == '/':
                print('除数不能为0')
            else:
                self.numer2 = self.__pop().value
                self.numer1 = self.__pop().value
                if operation == '-':
                    self.__push((int(self.numer1) - int(self.numer2)))
                elif operation == '+':
                    self.__push((int(self.numer1) + int(self.numer2)))
                elif operation == '*':
                    self.__push((int(self.numer1) * int(self.numer2)))
                elif operation == '/':
                    self.__push(int((int(self.numer1) / int(self.numer2))))


if __name__ == '__main__':
    t = StackTest()
    t.operation()
