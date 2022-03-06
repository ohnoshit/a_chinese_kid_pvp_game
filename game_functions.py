# 游戏主要代码

import random as ran

import time

from settings import Settings

class Huangame():

        def __init__(self):
            pass

        # 开局小知识
        def cold_knowledge(self):
            huang = input('你想要看一些小知识吗？y/n')
            if huang == 'y':
                pass


        # 获得两位玩家姓名
        def player_name(self):
            huang = False

            while True:
                self.first_player_name = input('请输入第一位玩家的名字:')
                self.second_player_name = input('请输入第二位玩家的名字:')

                print('第一位玩家的名字是：' + self.first_player_name + '。')
                print('第二位玩家的名字是：' + self.second_player_name + '。')
                verification = input('请确认你们的姓名（y/n）')

                if verification == 'y':
                    print('完成名字选择')
                    break
                elif verification == 'n':
                    print('\n请重新输入名字')
                else:
                    print('\n选择错误，请重新输入')

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
                self.second_player_professional  = input('\n请 ' +
                    self.second_player_name + ' 选择职业\n1:双刃\n2:重剑\n3:冷锋\n')
                if self.second_player_professional == '1' or '2' or '3':
                    print('玩家 ' + self.second_player_name + ' 合规')
                    if self.second_player_professional == '1':
                        print('玩家 ' + self.second_player_name + ' 职业为 双刃')
                    if self.second_player_professional == '2':
                        print('玩家 ' + self.second_player_name + ' 职业为 重剑')
                    if self.second_player_professional == '3':
                        print('玩家 ' + self.second_player_name + ' 职业为 冷锋')
                    break
                else:
                    print('请重新输入')

        def lf_normal_attacks(self):
            # 实现冷锋的特殊普攻方式
            self.first_player_normal_attacks = random.randint(3, 4)

            y = 1
            while y == 4:
                huang = random.randint(1, 100)
                if huang <= 40:
                    y = y + 1
                    self.first_player_normal_attacks = 2 * self.first_player_normal_attacks
                    print("Wow，你打出了暴击!")
                else:
                    break

        # 初始化角色普攻伤害
        def role_initialize(self):
            ai_settings = Settings()
            if self.first_player_professional == '1':
                self.first_player_normal_attacks = ran.randint(ai_settings.s_r_A_l, ai_settings.s_r_A_h)
            elif self.first_player_professional == '2':
                self.first_player_normal_attacks = ran.randint(ai_settings.z_j_A_l, ai_settings.z_j_A_h)
            else:
                self.first_player_normal_attacks = ran.randint(ai_settings.l_f_A_l, ai_settings.l_f_A_h)
            if self.second_player_professional == '1':
                self.second_player_normal_attacks = ran.randint(ai_settings.s_r_A_l, ai_settings.s_r_A_h)
            elif self.second_player_professional == '2':
                self.second_player_normal_attacks = ran.randint(ai_settings.z_j_A_l, ai_settings.z_j_A_h)
            else:
                self.second_player_normal_attacks = ran.randint(ai_settings.l_f_A_l, ai_settings.l_f_A_h)

            print('\n初始化角色普攻伤害成功')

        # 初始化数值
        def initialize_game(self):
            # 将Settings类定义为ai_settings
            ai_settings = Settings()

            # 初始化两位玩家初始血量
            self.first_player_hp = ai_settings.first_player_hp
            self.second_player_hp = ai_settings.first_player_hp

            # 初始化两位玩家拥有的硬币
            self.first_player_coins = ai_settings.first_player_coins
            self.second_player_coins = ai_settings.second_player_coins

        def shop(self):
            print('欢迎来到商店')
            print('请你选择想要的商品')
            print('购买商品需要花费硬币')
            print("输入'q'退出")

            print('\n1：增加10生命值 20硬币')
            print('2:增加20生命值 35硬币')
            while True:
                huang = input('请' + self.first_player_name + '输入数字以购买商品')
                if huang == '1':
                    if self.first_player_coins >= 20:
                        self.first_player_coins = self.first_player_coins - 20
                        print('玩家 ' + self.first_player_name + ' 还有 ' + str(self.first_player_coins) + ' 个硬币')
                        self.first_player_hp = self.first_player_hp + 10
                        print('玩家 ' + self.first_player_name + ' 血量为 ' + str(self.first_player_hp) + ' 点')
                    else:
                        print('您的硬币不足')
                elif huang == '2':
                    if self.first_player_coins >= 35:
                        self.first_player_coins = self.first_player_coins - 35
                        print('玩家 ' + self.first_player_name + ' 还有 ' + str(self.first_player_coins) + ' 个硬币')
                        self.first_player_hp = self.first_player_hp + 20
                        print('玩家 ' + self.first_player_name + ' 血量为 ' + str(self.first_player_hp) + ' 点')
                    else:
                        print('您的硬币不足')
                elif huang == 'q':
                    print('玩家 ' + self.first_player_name + ' 结束购买')
                    break
                else:
                    print('你输入有误，请重新输入')

            while True:
                huang = input('请' + self.second_player_name + '输入数字以购买商品')
                if huang == '1':
                    if self.second_player_coins >= 20:
                        self.second_player_coins = self.second_player_coins - 20
                        print('玩家 ' + self.second_player_name + ' 还有 ' + str(self.second_player_coins) + ' 个硬币')
                        self.second_player_hp = self.second_player_hp + 10
                        print('玩家 ' + self.second_player_name + ' 血量为 ' + str(self.second_player_hp) + ' 点')
                    else:
                        print('您的硬币不足')
                elif huang == '2':
                    if self.second_player_coins >= 35:
                        self.second_player_coins = self.second_player_coins - 35
                        print('玩家 ' + self.second_player_name + ' 还有 ' + str(self.second_player_coins) + ' 个硬币')
                        self.second_player_hp = self.second_player_hp + 20
                        print('玩家 ' + self.second_player_name + ' 血量为 ' + str(self.second_player_hp) + ' 点')
                    else:
                        print('您的硬币不足')
                elif huang == 'q':
                    print('玩家 ' + self.second_player_name + ' 结束购买')
                    break
                else:
                    print('你输入有误，请重新输入')


        def game_start(self):
            print('\n游戏开始\n')

            # 定义第一回合
            x = 1

            # 定义重剑属性
            self.first_player_professional_zj_active = False
            self.second_player_professional_zj_active = False

            # 将Settings类定义为ai_settings
            ai_settings = Settings()

            while True:
                # 显示回合数并增加回合数
                print('\n第 ' + str(x) + ' 回合')
                x = x + 1


                # 初始化角色普攻伤害
                if self.first_player_professional == '1':
                    self.first_player_normal_attacks = ran.randint(ai_settings.s_r_A_l, ai_settings.s_r_A_h)
                elif self.first_player_professional == '2':
                    self.first_player_normal_attacks = ran.randint(ai_settings.z_j_A_l, ai_settings.z_j_A_h)
                else:
                    self.first_player_normal_attacks = ran.randint(ai_settings.l_f_A_l, ai_settings.l_f_A_h)
                if self.second_player_professional == '1':
                    self.second_player_normal_attacks = ran.randint(ai_settings.s_r_A_l, ai_settings.s_r_A_h)
                elif self.second_player_professional == '2':
                    self.second_player_normal_attacks = ran.randint(ai_settings.z_j_A_l, ai_settings.z_j_A_h)
                else:
                    self.second_player_normal_attacks = ran.randint(ai_settings.l_f_A_l, ai_settings.l_f_A_h)


                if self.first_player_professional == '1':
                    self.second_player_hp = self.second_player_hp - self.first_player_normal_attacks

                elif self.first_player_professional == '2':
                    if self.first_player_professional_zj_active == False:
                        self.first_player_professional_zj_active = True
                        print(self.first_player_name + '蓄力完毕')
                    else:
                        self.first_player_professional_zj_active = False
                        self.second_player_hp = self.second_player_hp - self.first_player_normal_attacks

                else:
                    huang_2 = ran.randint(1, 100)
                    if huang_2 <= ai_settings.l_f_A_o:
                        self.first_player_normal_attacks = 2 * self.first_player_normal_attacks
                        print('OH，' + self.first_player_name + '打出了暴击!')
                    self.second_player_hp = self.second_player_hp - self.first_player_normal_attacks


                if self.second_player_professional == '1':
                    self.first_player_hp = self.first_player_hp - self.second_player_normal_attacks

                elif self.second_player_professional == '2':
                    if self.second_player_professional_zj_active == False:
                        self.second_player_professional_zj_active = True
                        print(self.second_player_name + '蓄力完毕')
                    else:
                        self.second_player_professional_zj_active = False
                        self.first_player_hp = self.first_player_hp - self.second_player_normal_attacks

                else:
                    huang = ran.randint(1, 100)
                    if huang <= ai_settings.l_f_A_o:
                        self.first_player_normal_attacks = 2 * self.first_player_normal_attacks
                        print('OH，' + self.second_player_name + '你打出了暴击!')
                    self.first_player_hp = self.first_player_hp - self.second_player_normal_attacks

                if self.first_player_professional == '2' and self.first_player_professional_zj_active == False:
                    print('本回合玩家 ' + self.first_player_name + ' 未造成伤害')
                else:
                     print('第一位玩家造成了 ' + str(self.first_player_normal_attacks) + ' 点伤害')
                if self.second_player_professional == '2' and self.second_player_professional_zj_active == False:
                    print('本回合玩家 ' + self.second_player_name + ' 未造成伤害')
                else:
                    print('第二位玩家造成了 ' + str(self.second_player_normal_attacks) + ' 点伤害')
                print("第一位玩家血量为 " + str(self.first_player_hp))
                print("第二位玩家血量为 " + str(self.second_player_hp))

                # 结束判定胜负
                if int(self.first_player_hp) <= 0 and int(self.second_player_hp) <= 0:
                    print('\n平局')
                    time.sleep(1)
                    print('\nGAME OVER')
                    break
                elif int(self.first_player_hp) <= 0:
                    print('\n' + self.first_player_name + ' 死了')
                    print(self.second_player_name + ' 赢了')
                    time.sleep(1)
                    print('\nGAME OVER')
                    break
                elif int(self.second_player_hp) <= 0:
                    print('\n' + self.second_player_name + ' 死了')
                    print(self.first_player_name + ' 赢了')
                    time.sleep(1)
                    print('\nGAME OVER')
                    break



