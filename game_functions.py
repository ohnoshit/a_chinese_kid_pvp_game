# 游戏主要代码

import random as ran

import time

class Huangame():

        def __init__(self):
        # 获得两位玩家姓名
            huang = False

            while huang == False:
                self.first_player_name = input('请输入第一位玩家的名字:')
                self.second_player_name = input('请输入第二位玩家的名字:')

                print('第一位玩家的名字是：' + self.first_player_name + '。')
                print('第二位玩家的名字是：' + self.second_player_name + '。')
                verification = input('请确认你们的姓名（y/n）')

                if verification == 'y':
                    print('完成名字选择')
                    huang = True
                elif verification == 'n':
                    print('请重新输入名字:')
                else:
                    print('选择错误，请重新输入')

        # 让玩家选择游戏角色职业
        def role_choice(self):
            print('\n\n比赛开始')
            print('您们可以选择自己的角色职业，职业共三种')
            print('第一种：双刃；\n第二种：重剑\n第三种：冷锋\n')
            while True:
                self.first_player_professional = input('请 ' +
                    self.first_player_name + ' 选择职业\n1:双刃\n2:重剑\n3:冷锋\n')
                print('')
                # 判定玩家选择是否合法
                if self.first_player_professional == '1' or '2' or '3':
                    print('玩家 ' + self.first_player_name + ' 合规')
                    if self.first_player_professional == '1':
                        print('玩家 ' + self.first_player_name + ' 职业为 双刃')
                    if self.first_player_professional == '2':
                        print('玩家 ' + self.first_player_name + ' 职业为 重剑')
                    if self.first_player_professional == '3':
                        print('玩家 ' + self.first_player_name + ' 职业为 冷锋')
                    break
                else:
                    print('请重新输入')
            while True:
                self.second_player_professional  = input('请 ' +
                    self.second_player_name + ' 选择职业\n1:双刃\n2:重剑\n3:冷锋\n')
                if self.second_player_professional == '1' or '2' or '3':
                    print('玩家 ' + self.second_player_name + ' 合规')
                    if self.second_player_professional == '1':
                        print('玩家 ' + self.second_player_name + ' 职业为 双刃')
                    if self.second_player_professional == '2':
                        print('玩家 ' + self.second_player_name + ' 职业为 重剑')
                    if self.second_player_professional == '3':
                        print('玩家 ' + second_player_name + ' 职业为 冷锋')
                    break
                else:
                    print('请重新输入')

        # 初始化角色普攻伤害
        def role_initialize(self):
            if self.first_player_professional == '1':
                self.first_player_normal_attacks = ran.randint(5, 7)
            elif self.first_player_professional == '2':
                self.first_player_normal_attacks = ran.randint(10,15)
            else:
                self.first_player_normal_attacks = ran.randint(3,4)
            if self.second_player_professional == '1':
                self.second_player_normal_attacks = ran.randint(5, 7)
            elif self.second_player_professional == '2':
                self.second_player_normal_attacks = ran.randint(10,15)
            else:
                self.second_player_normal_attacks = ran.randint(3,4)
            print('游戏初始化成功\n')

        # 开始游戏
        def game_start(self):
            print('游戏开始')
            x = 2
            print('\n第 1 回合')
            first_player_hp = 100 - self.second_player_normal_attacks
            second_player_hp = 100 - self.first_player_normal_attacks
            print("第一位玩家血量为" + str(first_player_hp))
            print("第二位玩家血量为" + str(second_player_hp))
            while True:
                print('\n第 ' + str(x) + ' 回合')
                x = x + 1
                first_player_hp = first_player_hp - self.second_player_normal_attacks
                second_player_hp = second_player_hp - self.first_player_normal_attacks
                print("第一位玩家血量为" + str(first_player_hp))
                print("第二位玩家血量为" + str(second_player_hp))
                time.sleep(1)

