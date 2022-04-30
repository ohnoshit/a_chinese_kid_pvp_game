from settings import Settings

from random import randint as ra

se = Settings()

class Game():
    
    def __init__(self, p_name):
        self.p_name = p_name

    def role_choice(self):
        print('\n\n比赛开始')
        print('您们可以选择自己的角色职业，职业共三种')
        print('第一种：双刃；\n第二种:重剑\n第三种:冷锋\n')
        while True:
            self.p_pro = input('请 ' +
                self.p_name + ' 选择职业\n1:双刃\n2:重剑\n3:冷锋\n')
            # 判定玩家选择是否合法
            if self.p_pro == '1':
                print('玩家 ' + self.p_name + ' 合规')                    
                print('玩家 ' + self.p_name + ' 职业为 双刃')
                break
            elif self.p_pro == '2':
                print('玩家 ' + self.p_name + ' 合规')
                print('玩家 ' + self.p_name + ' 职业为 重剑')
                break
            elif self.p_pro == '3':
                print('玩家 ' + self.p_name + ' 合规')
                print('玩家 ' + self.p_name + ' 职业为 冷锋')
                break
            else:
                print('请重新输入')

    # 初始化数值
    def initialize_game(self):
        # 初始化角色普攻伤害
        if self.p_pro == '1':
            self.p_A_h = se.s_r_A_h
            self.p_A_l = se.s_r_A_l
        elif self.p_pro == '2':
            self.p_A_h = se.z_j_A_h
            self.p_A_l = se.z_j_A_l
        else:
            self.p_A_h = se.l_f_A_h
            self.p_A_l = se.l_f_A_l
    