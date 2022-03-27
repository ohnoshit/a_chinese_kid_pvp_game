# -*- coding: utf-8 -*-

# 游戏主要代码


import random as ran

from settings import Settings

from colorama import Fore, Back, Style

class Huangame():
        # 获得两位玩家姓名
        def player_name(self):
            self.player_name_over = False
            while self.player_name_over == False:
                huang = input('是否自定义名字(y/n)')
                if huang == 'y':
                    self.first_player_name = input('请输入第一位玩家的名字:')
                    self.second_player_name = input('请输入第二位玩家的名字:')

                    print('第一位玩家的名字是：' + self.first_player_name + ' 。')
                    print('第二位玩家的名字是：' + self.second_player_name + ' 。')
                    huang = input('请确认你们的姓名(y/n)')

                    if huang == 'y':
                        print('完成名字选择')
                        self.player_name_over = False
                        break
                    elif huang == 'n':
                        print('\n请重新输入名字')
                    else:
                        print('\n选择错误,请重新输入')
                
                elif huang == 'n':
                    self.first_player_name = '玩家1'
                    self.second_player_name = '玩家2'
                    print('设置成功')
                    self.player_name_over = False
                    break

                else:
                    print("输入错误")
            

        # 让玩家选择游戏角色职业
        def role_choice(self):
            print('\n\n比赛开始')
            print('您们可以选择自己的角色职业，职业共三种')
            print('第一种：双刃；\n第二种:重剑\n第三种:冷锋\n')
            while True:
                self.first_player_professional = input('请 ' +
                    self.first_player_name + ' 选择职业\n1:双刃\n2:重剑\n3:冷锋\n')
                # 判定玩家选择是否合法
                if self.first_player_professional == '1':
                    print('玩家 ' + self.first_player_name + ' 合规')                    
                    print('玩家 ' + self.first_player_name + ' 职业为 双刃')
                    break
                elif self.first_player_professional == '2':
                    print('玩家 ' + self.first_player_name + ' 合规')
                    print('玩家 ' + self.first_player_name + ' 职业为 重剑')
                    break
                elif self.first_player_professional == '3':
                    print('玩家 ' + self.first_player_name + ' 合规')
                    print('玩家 ' + self.first_player_name + ' 职业为 冷锋')
                    break
                else:
                    print('请重新输入')
            while True:
                self.second_player_professional  = input('\n请 ' +
                    self.second_player_name + ' 选择职业\n1:双刃\n2:重剑\n3:冷锋\n')
                if self.second_player_professional == '1':
                    print('玩家 ' + self.second_player_name + ' 合规')
                    print('玩家 ' + self.second_player_name + ' 职业为 双刃')
                    break
                elif self.second_player_professional == '2':
                    print('玩家 ' + self.second_player_name + ' 合规')
                    print('玩家 ' + self.second_player_name + ' 职业为 重剑')
                    break
                elif self.second_player_professional == '3':
                    print('玩家 ' + self.second_player_name + ' 合规')
                    print('玩家 ' + self.second_player_name + ' 职业为 冷锋')
                    break
                else:
                    print('你输入有误,请重新输入')


        # 初始化数值
        def initialize_game(self):
            # 将Settings类定义为ai_settings
            ai_settings = Settings()

            # 初始化角色普攻伤害
            if self.first_player_professional == '1':
                self.first_player_A_h = ai_settings.s_r_A_h
                self.first_player_A_l = ai_settings.s_r_A_l
            elif self.first_player_professional == '2':
                self.first_player_A_h = ai_settings.z_j_A_h
                self.first_player_A_l = ai_settings.z_j_A_l
            else:
                self.first_player_A_h = ai_settings.l_f_A_h
                self.first_player_A_l = ai_settings.l_f_A_l

            if self.second_player_professional == '1':
                self.second_player_A_h = ai_settings.s_r_A_h
                self.second_player_A_l = ai_settings.s_r_A_l
            elif self.second_player_professional == '2':
                self.second_player_A_h = ai_settings.z_j_A_h
                self.second_player_A_l = ai_settings.z_j_A_l
            else:
                self.second_player_A_h = ai_settings.l_f_A_h
                self.second_player_A_l = ai_settings.l_f_A_l

            

            print('\n初始化角色普攻伤害成功')

          

        def shop(self):

            ai_settings = Settings()

            # 定义药水背包
            self.first_player_potions = ai_settings.first_player_potions
            self.second_player_potions = ai_settings.second_player_potions  

            # 定义武器和护甲背包
            self.first_player_weapon = ai_settings.first_player_weapon
            self.second_player_weapon = ai_settings.second_player_weapon
            self.first_player_armon = ai_settings.first_player_armon
            self.second_player_armon = ai_settings.second_player_armon

            # 增加伤害标志
            self.first_player_increase_hp = 0
            self.second_player_increase_hp = 0

            # 初始化平A暴击概率
            self.s_r_A_o = ai_settings.s_r_A_o 
            self.z_j_A_o = ai_settings.z_j_A_o
            self.l_f_A_o = ai_settings.l_f_A_o  

            # 初始化暴击伤害
            self.f_p_c_d = ai_settings.f_p_c_d
            self.s_p_c_d = ai_settings.s_p_c_d

            # 初始化血量价格
            self.shop_hp_p = ai_settings.shop_hp_p    

            # 初始化伤害价格
            if self.first_player_professional == '1':
                self.shop_d_p = ai_settings.shop_s_r_d_p
                self.shop_d_p_a = ai_settings.shop_s_r_d_p_a
            elif self.first_player_professional == '2':
                self.shop_d_p = ai_settings.shop_z_j_d_p
                self.shop_d_p_a = ai_settings.shop_z_j_d_p_a
            else:
                self.shop_d_p = ai_settings.shop_l_f_d_p
                self.shop_d_p_a = ai_settings.shop_l_f_d_p_a
    
            

            self.shop_places = [ai_settings.shop_place_hp, ai_settings.shop_place_potion,
                ai_settings.shop_place_weapon, ai_settings.shop_place_armon]

            self.shop_value = {
                '增加1点血量': str(round(self.shop_hp_p)),
                '增加1点攻击': str(self.shop_d_p),                
            }   

            self.shop_potions = {
                '一级治疗药水' : str(ai_settings.primary_healing_potion_p),
                '二级治疗药水' : str(ai_settings.secondary_healing_potion_p),
                '三级治疗药水' : str(ai_settings.tertiary_healing_potion_p),
                '一级恢复药水' : str(ai_settings.primary_recovery_potion_p),
                '一级力量药水' : str(ai_settings.primary_power_potion_p),                
            }        

            self.shop_weapon = {} 


            print('欢迎来到商店')
            print('请你选择想要的商品')
            print('购买商品需要花费硬币')
            print("输入'q'退出")
            print('商品如下:')

            # 注意事项
            print(Fore.CYAN + '注意，药水至多可以买九瓶药水')
            print("按'q'退出")
            print(Style. RESET_ALL)

                
            while True:
                huang = 1
                for self.shop_place in self.shop_places:
                    print(str(huang) + ':' + self.shop_place)
                    huang += 1                                  
                huang = input('请' + self.first_player_name + ' 选择购买人、地:\n')  

                if huang == '1':
                    while True:
                        huang = 1
                        for self.shop_thing_name, self.shop_thing_price in self.shop_value.items():
                            print(str(huang) + ':' + self.shop_thing_name + ' 价格为 ' + self.shop_thing_price)
                            huang += 1

                        huang = input('\n请' + self.first_player_name + '输入数字以购买商品')
                        if huang == '1':
                            if ai_settings.first_player_coins >= round(self.shop_hp_p):
                                print('啊哈哈哈!鸡汤来喽!')
                                ai_settings.first_player_coins = ai_settings.first_player_coins - round(self.shop_hp_p)
                                print('玩家 ' + self.first_player_name + ' 还有 ' + str(ai_settings.first_player_coins) + ' 个硬币')
                                ai_settings.first_player_hp = ai_settings.first_player_hp + 1
                                print('玩家 ' + self.first_player_name + ' 血量为 ' + str(ai_settings.first_player_hp) + ' 点')
                                self.shop_hp_p += 0.5
                                self.shop_value = {
                                    '增加1点血量': str(round(self.shop_hp_p)),
                                    '增加1点攻击': str(self.shop_d_p),                 
                                        }   
                            else:
                                print('您的硬币不足')
                            
                        elif huang == '2':
                            if ai_settings.first_player_coins >= self.shop_d_p:
                                if self.first_player_increase_hp < 3:
                                    print('啊哈哈哈!鸡汤来喽!')
                                    self.first_player_increase_hp += 1
                                    ai_settings.first_player_coins = ai_settings.first_player_coins - self.shop_d_p
                                    print('玩家 ' + self.first_player_name + ' 还有 ' + str(ai_settings.first_player_coins) + ' 个硬币')
                                    self.shop_d_p += self.shop_d_p_a
                                    print(self.first_player_name + ' 的伤害为 ' + str(self.first_player_A_l + self.first_player_increase_hp) +
                                            ' ~ ' + str(self.first_player_A_h + self.first_player_increase_hp))
                                    self.shop_value = {
                                        '增加1点血量': str(round(self.shop_hp_p)),
                                        '增加1点攻击': str(self.shop_d_p),                  
                                            }                                               
                                else:
                                    print(self.first_player_name + ' 已达到增加伤害上限')
                            else:
                                print('您的硬币不足')

                        elif huang == 'q':
                            print('跟我玩阴地是把，那就来吧！')
                            huang = 0
                            break

                        else:
                            print('你输入错了！')

                if huang == '2':
                    while True:
                        huang = 1
                        for self.shop_thing_name, self.shop_thing_price in self.shop_potions.items():
                            print(str(huang) + ':' + self.shop_thing_name + ' 价格为 ' + self.shop_thing_price)
                            huang += 1   
                        huang = input('请' + self.first_player_name + '输入数字以购买商品')    

                        if huang == '1':
                            if ai_settings.first_player_coins >= ai_settings.primary_healing_potion_p:
                                if len(self.first_player_potions) < 9:
                                    self.first_player_potions.append('一级治疗药水')
                                    ai_settings.first_player_coins = ai_settings.first_player_coins - ai_settings.primary_healing_potion_p
                                    print(self.first_player_name + '成功购买一级治疗药水')
                                    print(self.first_player_name + '还有' + str(ai_settings.first_player_coins) + '个硬币')
                                    print(self.first_player_name + '拥有的药水:')
                                    for self.first_player_potion in ai_settings.first_player_potions:
                                        print('-' + self.first_player_potion)
                                else:
                                    print('不得够买超过9瓶药水')
                            else:
                                print('您的硬币不足')
                
                        elif huang == '2':
                            if ai_settings.first_player_coins >= ai_settings.secondary_healing_potion_h:
                                if len(self.first_player_potions) < 9:                        
                                    self.first_player_potions.append('二级治疗药水')
                                    ai_settings.first_player_coins = ai_settings.first_player_coins - ai_settings.secondary_healing_potion_h
                                    print(self.first_player_name + '成功购买 二级治疗药水')
                                    print(self.first_player_name + '拥有的药水:')
                                    for self.first_player_potion in ai_settings.first_player_potions:
                                        print('-' + self.first_player_potion)
                                else:
                                    print('不得够买超过9瓶药水')                                
                            else:
                                print('您的硬币不足')

                        elif huang == '3':
                            if ai_settings.first_player_coins >= ai_settings.tertiary_healing_potion_p:
                                if len(self.first_player_potions) < 9:                        
                                    self.first_player_potions.append('三级治疗药水')
                                    ai_settings.first_player_coins = ai_settings.first_player_coins - ai_settings.tertiary_healing_potion_p
                                    print(self.first_player_name + '成功购买 三级治疗药水')
                                    print(self.first_player_name + '拥有的药水:')
                                    for self.first_player_potion in ai_settings.first_player_potions:
                                        print('-' + self.first_player_potion)
                                else:
                                    print('不得够买超过9瓶药水')                                
                            else:
                                print('您的硬币不足')

                        elif huang == '4':
                            if ai_settings.first_player_coins >= ai_settings.primary_recovery_potion_p:
                                if len(self.first_player_potions) < 9:
                                    self.first_player_potions.append('一级恢复药水')
                                    ai_settings.first_player_coins = ai_settings.first_player_coins - ai_settings.primary_recovery_potion_p
                                    print(self.first_player_name + ' 成功购买 一级恢复药水')                                    
                                    for self.first_player_potion in ai_settings.first_player_potions:
                                        print('-' + self.first_player_potion)
                                else:
                                    print('不得够买超过9瓶药水')                                
                            else:
                                print('您的硬币不足')                            

                        elif huang == '5':
                            if ai_settings.first_player_coins >= ai_settings.primary_healing_potion_p:
                                if len(self.first_player_potions) < 9:
                                    self.first_player_potions.append('一级力量药水')
                                    ai_settings.first_player_coins = ai_settings.first_player_coins - ai_settings.primary_power_potion_p
                                    print(self.first_player_name + '成功购买 一级力量药水')
                                    print(self.first_player_name + '拥有的药水:')
                                    for self.first_player_potion in ai_settings.first_player_potions:
                                        print('-' + self.first_player_potion)
                                else:
                                    print('不得够买超过9瓶药水')                                
                            else:
                                print('您的硬币不足')                            

                        elif huang == 'q':
                            print(self.first_player_name + '?一个有趣的名字')
                            break

                        else:
                            print('你输入有误，请重新输入')  


                elif huang == 'q':
                    print(self.first_player_name + ' 结束购买')
                    break

                else:
                    print('输入有误')

            # 刷新血量价格
            self.shop_hp_p = ai_settings.shop_hp_p

            # 刷新价格
            if self.second_player_professional == '1':
                self.shop_d_p = ai_settings.shop_s_r_d_p
                self.shop_d_p_a = ai_settings.shop_s_r_d_p_a
            elif self.second_player_professional == '2':
                self.shop_d_p = ai_settings.shop_z_j_d_p
                self.shop_d_p_a = ai_settings.shop_z_j_d_p_a
            else:
                self.shop_d_p = ai_settings.shop_l_f_d_p
                self.shop_p_a = ai_settings.shop_l_f_d_p_a  

            while True:
                huang = 1
                for self.shop_place in self.shop_places:
                    print(str(huang) + ':' + self.shop_place)
                    huang += 1                                  
                huang = input('请' + self.second_player_name + ' 选择购买人、地:\n')   

                if huang == '1':
                    while True:
                        huang = 1
                        for self.shop_thing_name, self.shop_thing_price in self.shop_value.items():
                            print(str(huang) + ':' + self.shop_thing_name + ' 价格为 ' + self.shop_thing_price)
                            huang += 1
                        huang = input('请' + self.first_player_name + '输入数字以购买商品') 

                        if huang == '1':
                            if ai_settings.second_player_coins >= round(self.shop_hp_p):
                                print('啊哈哈哈!鸡汤来喽!')
                                ai_settings.second_player_coins = ai_settings.second_player_coins - round(self.shop_hp_p)
                                print('玩家 ' + self.second_player_name + ' 还有 ' + str(ai_settings.second_player_coins) + ' 个硬币')
                                ai_settings.second_player_hp = ai_settings.second_player_hp + 1
                                print('玩家 ' + self.second_player_name + ' 血量为 ' + str(ai_settings.second_player_hp) + ' 点')
                                self.shop_hp_p += 0.5
                                self.shop_value = {
                                    '增加1点血量': str(round(self.shop_hp_p)),
                                    '增加1点攻击': str(self.shop_d_p),                
                                        }                                
                            else:
                                print('您的硬币不足')

                        elif huang == '2':
                            if ai_settings.second_player_coins >= self.shop_d_p:
                                if self.second_player_increase_hp < 3:
                                    print('啊哈哈哈!鸡汤来喽!')
                                    self.second_player_increase_hp += 1
                                    ai_settings.second_player_coins = ai_settings.second_player_coins - self.shop_d_p
                                    print('玩家 ' + self.second_player_name + ' 还有 ' + str(ai_settings.second_player_coins) + ' 个硬币')
                                    self.shop_d_p += self.shop_d_p_a
                                    print(self.second_player_name + ' 的伤害为 ' + str(self.second_player_A_l + self.second_player_increase_hp) +
                                        ' ~ ' + str(self.second_player_A_h + self.second_player_increase_hp))
                                    self.shop_value = {
                                        '增加1点血量': str(round(self.shop_hp_p)),
                                        '增加1点攻击': str(self.shop_d_p),                
                                        }         
                                else:
                                    print(self.second_player_name + ' 已达增加伤害上限')    
                                    
                            else:
                                print('您的硬币不足')

                        elif huang == 'q':
                            print('跟我玩阴地是把，那就来吧！')
                            huang = 0
                            break

                        else:
                            print('你输入错了！')                                

                elif huang == '2':
                    while True:
                        huang = 1
                        for self.shop_thing_name, self.shop_thing_price in self.shop_potions.items():
                            print(str(huang) + ':' + self.shop_thing_name + ' 价格为 ' + self.shop_thing_price)
                            huang += 1                           
                        huang = input('请' + self.second_player_name + '输入数字以购买商品') 

                        if huang == '1': 
                            if ai_settings.second_player_coins >= ai_settings.primary_healing_potion_p:
                                if len(self.second_player_potions) < 9:
                                    self.second_player_potions.append('一级治疗药水')
                                    ai_settings.second_player_coins = ai_settings.second_player_coins - ai_settings.primary_healing_potion_p
                                    print(self.second_player_name + '成功购买一级治疗药水')
                                    for self.second_player_potion in ai_settings.second_player_potions:
                                        print('-' + self.second_player_potion)                                         
                                else:
                                    print('不得够买超过9瓶药水')
                            else:
                                print('您的硬币不足') 

                        elif huang == '2':
                            if ai_settings.second_player_coins >= ai_settings.secondary_healing_potion_h:
                                if len(self.second_player_potions) < 9:                        
                                    self.second_player_potions.append('二级治疗药水')
                                    ai_settings.second_player_coins = ai_settings.second_player_coins - ai_settings.secondary_healing_potion_h
                                    print(self.second_player_name + '成功购买 二级治疗药水')
                                    for self.second_player_potion in ai_settings.second_player_potions:
                                        print('-' + self.second_player_potion)
                                else:
                                    print('不得够买超过9瓶药水')
                            else:
                                print('您的硬币不足') 

                        elif huang == '3':
                            if ai_settings.second_player_coins >= ai_settings.tertiary_healing_potion_p:
                                if len(self.second_player_potions) < 9:                        
                                    self.second_player_potions.append('三级治疗药水')
                                    ai_settings.second_player_coins = ai_settings.second_player_coins - ai_settings.tertiary_healing_potion_p
                                    print(self.second_player_name + '成功购买 三级治疗药水')
                                    print(self.second_player_name + '拥有的药水:')
                                    for self.second_player_potion in ai_settings.second_player_potions:
                                        print('-' + self.second_player_potion)
                                else:
                                    print('不得够买超过9瓶药水')                                
                            else:
                                print('您的硬币不足')   

                        elif huang == '4':
                            if ai_settings.second_player_coins >= ai_settings.primary_recovery_potion_p:
                                if len(self.second_player_potions) < 9:
                                    self.second_player_potions.append('一级恢复药水')
                                    ai_settings.second_player_coins = ai_settings.second_player_coins - ai_settings.primary_recovery_potion_p
                                    print(self.second_player_name + '成功购买 一级恢复药水')
                                    print(self.second_player_name + '拥有的药水:')
                                    for self.second_player_potion in ai_settings.second_player_potions:
                                        print('-' + self.second_player_potion)
                                else:
                                    print('不得够买超过9瓶药水')                                
                            else:
                                print('您的硬币不足')    

                    
                        elif huang == '5':
                            if ai_settings.second_player_coins >= ai_settings.primary_power_potion_p:
                                if len(self.second_player_potions) < 9:                        
                                    self.second_player_potions.append('一级力量药水')
                                    ai_settings.second_player_coins = ai_settings.second_player_coins - ai_settings.primary_power_potion_p
                                    print(self.second_player_name + '成功购买 一级力量药水')
                                    print(self.second_player_name + '拥有的药水:')
                                    for self.second_player_potion in ai_settings.second_player_potions:
                                        print('-' + self.second_player_potion)
                                else:
                                    print('不得够买超过9瓶药水')                                
                            else:
                                print('您的硬币不足')    
                        
                        elif huang == 'q':
                            print(self.second_player_name + '?一个有趣的名字')
                            break                        

                elif huang == 'q':
                    print(self.second_player_name + ' 结束购买')
                    break

                else:
                    print('输入有误')     

        
        def game_start(self):
            print('\n游戏开始\n')


            # 定义游戏状态
            self.game_over_active = True

            # 定义第一回合
            x = 1

            # 定义重剑属性
            self.first_player_professional_zj_active = False
            self.second_player_professional_zj_active = False

            # 将Settings类定义为ai_settings
            ai_settings = Settings()

            # 力量药水增加伤害效果
            self.first_player_strength = 0
            self.second_player_strength = 0

            # 恢复药水
            self.first_player_healing_s_p = 0
            self.second_player_healing_s_p = 0

            # 回合开始标志
            self.first_player_round_begin = True
            self.second_player_round_begin = True

            # 玩家2获得额外血量（追求游戏平衡）
            self.healing = ran.randint(8, 10)
            ai_settings.second_player_hp += self.healing
            print(self.second_player_name + ' 额外获得 ' + str(self.healing) + ' 点血量')

            while self.game_over_active == True:        
                # 显示回合数并增加回合数
                print('\n第 ' + str(x) + ' 回合')
                x = x + 1
                
                # 输入显示

                self.message_1_help = "输入'q': 向下移动2项"
                self.message_1_help += "\n输入'a': 向下移动1项"
                self.message_1_help += "\n输入'e': 向上移动2项"
                self.message_1_help += "\n输入'd': 向上移动1项"
                self.message_1_help += "\n输入'w': 确认"
                self.message_1_help += "\n输入's': 认输"

                self.message_2_help = "输入'4': 向下移动2项"
                self.message_2_help += "\n输入'1': 向下移动1项"
                self.message_2_help += "\n输入'6': 向上移动2项"
                self.message_2_help += "\n输入'3': 向上移动1项"
                self.message_2_help += "\n输入'5': 确认"
                self.message_2_help += "\n输入'2': 认输"

                self.player_sport_mains = ['攻击', '特殊攻击', '药水']

                # 刷新药水效果
                self.second_player_strength = 0

                # 刷新光标
                self.first_player_cursor = 0

                # 刷新药水无效几率
                self.p_m = 0

                # 恢复药水效果
                if self.first_player_healing_s_p > 0:
                    huang = ran.randint(ai_settings.primary_recovery_potion_l,
                        ai_settings.primary_recovery_potion_h)
                    ai_settings.first_player_hp += huang
                    print(self.first_player_name + ' 恢复了 ' + str(huang) +  ' 点血量')
                    print(self.first_player_name + ' 血量为' + str(ai_settings.first_player_hp))

                # 初始化角色普攻伤害
                self.first_player_normal_attacks = ran.randint(self.first_player_A_l, self.first_player_A_h)
                self.first_player_normal_attacks += self.first_player_increase_hp
                self.second_player_normal_attacks = ran.randint(self.second_player_A_l,self.second_player_A_h)
                self.second_player_normal_attacks += self.second_player_increase_hp

                print('\n现在请 ' + self.first_player_name + ' 开始回合:')
                
                while self.first_player_round_begin == True:
                    print(self.message_1_help)

                    for self.player_sport_main in self.player_sport_mains:
                        print('-' + self.player_sport_main)

                    print(self.first_player_name + ' 现在正选择：' + self.player_sport_mains[self.first_player_cursor])
                    huang = input('请输入：')
                    if huang == 'q':
                        if self.first_player_cursor > int(len(self.player_sport_mains) - 2):
                            self.first_player_cursor -= 2
                        else:
                            print('无法进行此操作')         
                    if huang == 'a':
                        if self.first_player_cursor > int(len(self.player_sport_mains) - 1):
                            self.first_player_cursor -= 1
                        else:
                            print('无法进行此操作')  
                    elif huang == 'e':
                        if self.first_player_cursor < int(len(self.player_sport_mains) - 2):
                            self.first_player_cursor += 2
                        else:
                            print('无法进行此操作')   
                    elif huang == 'd':
                        if self.first_player_cursor < int(len(self.player_sport_mains) - 1):
                            self.first_player_cursor += 1
                        else:
                            print('无法进行此操作')

                    elif huang == 'w':
                        if self.first_player_cursor == 0:
                            if self.first_player_professional == '1':
                                if self.s_r_A_o >= ran.randint(1, 100):
                                    self.first_player_normal_attacks = round(self.f_p_c_d * self.first_player_normal_attacks)
                                    print(self.first_player_name + ' 打出了暴击')
                                ai_settings.second_player_hp = ai_settings.second_player_hp - self.first_player_normal_attacks

                            elif self.first_player_professional == '2':
                                if self.first_player_professional_zj_active == False:
                                        self.first_player_professional_zj_active = True
                                        print(self.first_player_name + '蓄力完毕')
                                else:
                                    if self.s_r_A_o >= ran.randint(1, 100):
                                        self.first_player_normal_attacks = round(self.f_p_c_d * self.first_player_normal_attacks)
                                        print(self.first_player_name + ' 打出了暴击')
                                    self.first_player_professional_zj_active = False
                                    ai_settings.second_player_hp = ai_settings.second_player_hp - self.first_player_normal_attacks

                            else:
                                huang = 1
                                if ran.randint(1, 100) <= ai_settings.l_f_A_o:
                                    self.second_player_round_begin = False
                                if self.s_r_A_o >= ran.randint(1, 100):
                                    self.first_player_normal_attacks = round(self.f_p_c_d * self.first_player_normal_attacks)
                                    print(self.first_player_name + ' 打出了暴击')
                                ai_settings.second_player_hp = ai_settings.second_player_hp - self.first_player_normal_attacks

                            if self.first_player_professional == '2' and self.first_player_professional_zj_active == True:
                                print('本回合玩家 ' + self.first_player_name + ' 未造成伤害')
                            else:
                                print('第一位玩家造成了 ' + str(self.first_player_normal_attacks) + ' 点伤害')
                            print("第一位玩家血量为 " + str(ai_settings.first_player_hp))
                            print("第二位玩家血量为 " + str(ai_settings.second_player_hp))
                            break
                        
                        elif self.first_player_cursor == 1:
                            print('选项开发中')

                        elif self.first_player_cursor == 2:
                            while True:
                                if self.first_player_potions:
                                    print(self.first_player_name + ' 拥有的药水为:')
                                    for self.first_player_potion in self.first_player_potions:
                                        print('-' + self.first_player_potion)

                                    # 介绍
                                    print('可以输入相应数字选择药水')
                                    print("可以按'0'退出药水使用")
         
                                    try:
                                        huang = input('请输入序号：')
                                        if int(huang) == 0:
                                            print('已退出购买') 
                                            break

                                        if int(huang) <= int(len(self.first_player_potions)):
                                            if self.first_player_potions[int(int(huang) - 1)] == '一级治疗药水':
                                                self.healing = ran.randint(ai_settings.primary_healing_potion_l,
                                                    ai_settings.primary_healing_potion_h)
                                                # 移除药水
                                                self.first_player_potions.remove('一级治疗药水')
                                                # 增加几率
                                                self.p_m += ai_settings.p_p_m_o
                                                if ran.randint(1, 100) >= self.p_m:
                                                    self.healing = ran.randint(ai_settings.primary_healing_potion_l,
                                                        ai_settings.primary_healing_potion_h)                                                    
                                                    # 回复血量
                                                    ai_settings.first_player_hp += self.healing
                                                    print(self.first_player_name + ' 恢复了 ' + str(self.healing) + ' 点血量')
                                                else:
                                                    print(self.first_player_name +' 使用无效')

                                            elif self.first_player_potions[int(int(huang) - 1)] == '二级治疗药水':
                                                self.first_player_potions.remove('二级治疗药水')  
                                                self.p_m = ai_settings.s_p_m_o                                          
                                                if ran.randint(1, 100) >= self.p_m:
                                                    self.healing = ran.randint(ai_settings.secondary_healing_potion_l,
                                                        ai_settings.secondary_healing_potion_h)                                                    
                                                    # 回复血量
                                                    ai_settings.first_player_hp += self.healing
                                                    print(self.first_player_name + ' 恢复了 ' + str(self.healing) + ' 点血量')
                                                else:
                                                    print(self.first_player_name + ' 使用无效')                                                

                                            elif self. first_player_potions[int(int(huang) - 1)] == '三级治疗药水':
                                                self.first_player_potions.remove('三级治疗药水')
                                                print(self.first_player_name + ' 恢复了 ' + str(self.healing) + ' 点血量')  
                                                self.p_m += ai_settings.t_p_m_o 
                                                if ran.randint(1, 100) >= self.p_m:
                                                    self.healing = ran.randint(ai_settings.tertiary_healing_potion_l,
                                                        ai_settings.tertiary_healing_potion_h)                                                
                                                    # 回复血量
                                                    ai_settings.first_player_hp += self.healing
                                                    print(self.first_player_name + ' 恢复了 ' + str(self.healing) + ' 点血量')
                                                else:
                                                    print(self.first_player_name + ' 使用无效')                                                

                                            elif self.first_player_potions[int(int(huang) - 1)] == '一级力量药水':
                                                self.first_player_normal_attacks += self.first_player_strength
                                                self.first_player_potions.remove('一级力量药水') 
                                                self.p_m += ai_settings.p_p_m_o
                                                if ran.randint(1, 100) >= self.p_m:
                                                    self.first_player_strength = ran.randint(ai_settings.primary_power_potion_l,
                                                        ai_settings.primary_power_potion_h)
                                                    self.first_player_normal_attacks += self.first_player_strength 
                                                    print(self.first_player_name + ' 增加了 ' + str(self.first_player_strength) + ' 点伤害')    
                                                else:
                                                    print(self.first_player_name + ' 使用无效')                                                                                                                                                                                                          

                                            elif self.first_player_potions[int(int(huang) - 1)] == '一级恢复药水':
                                                self.p_m += ai_settings.p_p_m_o
                                                if ran.randint(1, 100) >= self.p_m:
                                                    self.first_player_healing_s_p = 3
                                                    print(self.first_player_name + ' 使用了 一级恢复药水') 
                                                    self.first_player_potions.remove('一级恢复药水')    
                                                else:
                                                    print(self.first_player_name + ' 使用无效')                                                                                 
                                            else:
                                                print(self.first_player_name + ' 没有相应药水')
                                    except:
                                        print(self.first_player_name + ' 选择错误，请重新输入')   
                                else:
                                    print(self.first_player_name + ' 没有药水')
                                    break

                    elif huang == 's':
                        print(self.first_player_name + ' 认输了！')
                        self.game_over_active = False
                        break
                    else:
                        print('输入错误')   

                else:
                    self.first_player_round_begin = True
                    print(self.first_player_name + ' 被麻痹了!')

                # 恢复药水效果
                if self.second_player_healing_s_p > 0:
                    huang = ran.randint(ai_settings.primary_recovery_potion_l,
                        ai_settings.primary_recovery_potion_h)
                    ai_settings.first_player_hp += huang
                    print(self.second_player_name + ' 恢复了 ' + str(huang) + ' 点血量')
                    print(self.second_player_name + ' 血量为 ' + ai_settings.second_player_hp)                                       

                # 刷新光标
                self.second_player_cursor = 0

                # 删除力量药水（顺时）效果
                self.first_player_strength = 0

                # 刷新药水无效几率
                self.p_m = 0

                print('\n现在请 ' + self.second_player_name + ' 开始回合:')
                
                while self.second_player_round_begin == True:
                    
                    print(self.message_2_help)

                    for self.player_sport_main in self.player_sport_mains:
                        print('-' + self.player_sport_main)

                    print(self.second_player_name + ' 现在正选择：' + self.player_sport_mains[self.second_player_cursor])
                    huang = input('请输入：')
                    if huang == '4':
                        if self.second_player_cursor > int(len(self.player_sport_mains) - 2):
                            self.second_player_cursor -= 2
                        else:
                            print('无法进行此操作')         
                    if huang == '1':
                        if self.second_player_cursor > int(len(self.player_sport_mains) - 1):
                            self.second_player_cursor -= 1
                        else:
                            print('无法进行此操作')  
                    elif huang == '6':
                        if self.second_player_cursor < int(len(self.player_sport_mains) - 2):
                            self.second_player_cursor += 2
                        else:
                            print('无法进行此操作')   
                    elif huang == '3':
                        if self.second_player_cursor < int(len(self.player_sport_mains) - 1):
                            self.second_player_cursor += 1
                        else:
                            print('无法进行此操作')
                    elif huang == '5':
                        if self.second_player_cursor == 0:
                            if self.second_player_professional == '1':
                                if self.s_p_c_d >= ran.randint(1, 100):
                                    self.second_player_normal_attacks = round(self.s_p_c_d * self.second_player_normal_attacks)
                                    print(self.second_player_name + ' 打出了暴击')
                                ai_settings.first_player_hp = ai_settings.first_player_hp - self.second_player_normal_attacks

                            elif self.second_player_professional == '2':
                                if self.second_player_professional_zj_active == False:
                                    self.second_player_professional_zj_active = True
                                    print(self.second_player_name + '蓄力完毕')
                                else:
                                    self.second_player_professional_zj_active = False
                                    if self.s_p_c_d >= ran.randint(1, 100):
                                        self.second_player_normal_attacks = round(self.s_p_c_d * self.second_player_normal_attacks)
                                        print(self.second_player_name + ' 打出了暴击')
                                    ai_settings.first_player_hp = ai_settings.first_player_hp - self.second_player_normal_attacks

                            else:
                                huang = 1
                                if ran.randint(1, 100) <= ai_settings.l_f_A_o:
                                    self.first_player_round_begin = False
                                if self.s_p_c_d >= ran.randint(1, 100):
                                        self.second_player_normal_attacks = round(self.s_p_c_d * self.second_player_normal_attacks)
                                        print(self.second_player_name + ' 打出了暴击')
                                ai_settings.first_player_hp =  ai_settings.first_player_hp - self.second_player_normal_attacks
                            if self.second_player_professional == '2' and self.second_player_professional_zj_active == True:
                                print('本回合玩家 ' + self.second_player_name + ' 未造成伤害')
                            else:
                                print('第二位玩家造成了 ' + str(self.second_player_normal_attacks) + ' 点伤害')   
                            print("第一位玩家血量为 " + str(ai_settings.first_player_hp))
                            print("第二位玩家血量为 " + str(ai_settings.second_player_hp))                         
                            break

                        elif self.second_player_cursor == 1:
                            print('选项开发中')

                        elif self.second_player_cursor == 2:

                            while True:
                                if self.second_player_potions:
                                    print(self.second_player_name + ' 拥有的药水为:')
                                    for self.second_player_potion in self.second_player_potions:
                                        print('-' + self.second_player_potion)

                                    # 介绍
                                    print('可以输入相应数字选择药水')
                                    print("可以按'0'退出药水使用")                                        

                                    try:
                                        huang = input('请输入序号：')
                                        
                                        if self.second_player_potions[int(int(huang) - 1)] == '一级治疗药水':
                                            self.second_player_potions.remove('一级治疗药水') 
                                            self.p_m += ai_settings.p_p_m_o
                                            if ran.randint(1, 100) >= self.p_m:
                                                self.healing = ran.randint(ai_settings.primary_healing_potion_l,
                                                    ai_settings.primary_healing_potion_h)
                                                ai_settings.second_player_hp += self.healing                                                                                  
                                                print(self.second_player_name + ' 恢复了 ' + str(self.healing) + ' 点血量')
                                            else:
                                                print(self.second_player_name + ' 使用无效')  

                                        elif self.second_player_potions[int(int(huang) - 1)] == '二级治疗药水':
                                            self.second_player_potions.remove('二级治疗药水') 
                                            self.p_m += ai_settings.s_p_m_o
                                            if ran.randint(1, 100) > self.p_m:
                                                self.healing = ran.randint(ai_settings.secondary_healing_potion_l,
                                                    ai_settings.secondary_healing_potion_h)
                                                ai_settings.second_player_hp += self.healing
                                                print(self.second_player_name + ' 恢复了 ' + str(self.healing) + ' 点血量') 
                                            else:
                                                print(self.first_player_name + ' 使用无效')                                          

                                        elif self.second_player_potions[int(int(huang) - 1)] == '三级治疗药水':
                                            self.second_player_potions.remove('三级治疗药水') 
                                            self.p_m += ai_settings.t_p_m_o
                                            if ran.randint(1, 100) >= self.p_m:
                                                self.healing = ran.randint(ai_settings.tertiary_healing_potion_l,
                                                    ai_settings.tertiary_healing_potion_h)
                                                ai_settings.second_player_hp += self.healing
                                                print(self.second_player_name + ' 恢复了 ' + str(self.healing) + ' 点血量') 
                                            else:
                                                print(self.first_player_name + ' 使用无效')                                                      
                                        
                                        elif self.second_player_potions[int(int(huang) - 1)] == '一级治疗药水':
                                            self.second_player_potions.remove('一级治疗药水')
                                            self.p_m += ai_settings.p_p_m_o
                                            if ran.randint(1, 100) >= self.p_m:
                                                self.second_player_healing_s_p = 3
                                                print(self.second_player_name + ' 饮用了 一级恢复药水。')
                                            else:
                                                print(self.first_player_name + ' 使用无效')  

                                        elif self.second_player_potions[int(int(huang) - 1)] == '一级力量药水':
                                            self.second_player_potions.remove('一级力量药水') 
                                            self.p_m += ai_settings.p_p_m_o
                                            if ran.randint(1, 100) >= self.p_m:
                                                self.second_player_strength = ran.randint(ai_settings.primary_power_potion_l,
                                                    ai_settings.primary_power_potion_h)
                                                self.first_player_normal_attacks += self.second_player_strength
                                                print(self.second_player_name + ' 增加了 ' + str(self.second_player_strength) + ' 点伤害')                                     
                                            else:
                                                print(self.first_player_name + ' 使用无效') 

                                        if int(huang) == 0:
                                            print('已退出购买') 
                                            break

                                        else:
                                            print(self.second_player_name + ' 没有相应药水')                                                                                  
                                    except:                                                                              
                                        print(self.second_player_name + ' 选择错误，请重新输入')
                                else:
                                    print(self.second_player_name + ' 没有药水')
                                    break
                    
                    elif huang == '2':
                        print(self.second_player_name + ' 认输了！')
                        self.game_over_active = False
                        break
                    else:
                        print('输入错误')
                else:
                    self.second_player_round_begin = True
                    print(self.second_player_name + ' 被麻痹了!')

                # 结束判定胜负
                if int(ai_settings.first_player_hp) <= 0 and int(ai_settings.second_player_hp) <= 0:
                    print('\n平局')
                    self.game_over_active = False
                    print('\nGAME OVER')
                    break
                elif int(ai_settings.first_player_hp) <= 0:
                    print('\n' + self.first_player_name + ' 死了')
                    print(self.second_player_name + ' 赢了')
                    self.game_over_active = False
                    print('\nGAME OVER')
                    break
                elif int(ai_settings.second_player_hp) <= 0:
                    print('\n' + self.second_player_name + ' 死了')
                    print(self.first_player_name + ' 赢了')
                    self.game_over_active = False
                    print('\nGAME OVER')
                    break