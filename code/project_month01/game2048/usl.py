import os

from bll import GameCoreController


class GameConsoleView:
    def __init__(self):
        self.__controller = GameCoreController()

    def operation(self):
        while True:
            key_word = input('请输入方向：')
            if key_word == 'w':
                self.__controller.move_up()
                self.draw_view()
            elif key_word == 's':
                self.__controller.move_down()
                self.draw_view()
            elif key_word == 'a':
                self.__controller.move_left()
                self.draw_view()
            elif key_word == 'd':
                self.__controller.move_right()
                self.draw_view()
            self.__controller.generate_new_number()
            if self.__controller.game_over():
                print('游戏结束')

    def game_start(self):
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        self.draw_view()
        self.operation()

    def draw_view(self):
        os.system("clear")
        for line in range(len(self.__controller.map)):
            for item in range(len(self.__controller.map[line])):
                print(self.__controller.map[line][item], end='\t')
            print()

    def main(self):
        self.game_start()
