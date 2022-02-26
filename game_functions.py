# 游戏主要代码

class Huangame():

        def __init__(self):
            pass

        def player_name(self):
            huang = False

            while huang == False:
                self.first_player_name = input('请输入第一位玩家的名字:')
                self.second_player_name = input('请输入第二位玩家的名字:')


                print('第一位玩家的名字是：' + self.first_player_name + '。')
                print('第二位玩家的名字是：' + self.second_player_name + '。')
                verification = input('请确认你们的姓名（y/n）')

                if verification == 'y':
                    huang = True
                elif verification == 'n':
                    print('请重新输入名字:')
                else:
                    print('选择错误，请重新输入')

        def role_choice(self):
            print('OK\n\n比赛开始')
            print('您们可以选择自己的角色职业，职业共三种')
