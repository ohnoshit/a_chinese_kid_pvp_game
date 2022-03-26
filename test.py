'''
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

                # 刷新光标
                self.player_cursor = 0

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
                self.second_player_normal_attacks = ran.randint(self.second_player_A_l,self.second_player_A_h)


                print('\n现在请 ' + self.first_player_name + ' 开始回合:')
                print(self.message_1_help)
                
                for self.player_sport_main in self.player_sport_mains:
                    print('-' + self.player_sport_main)
                
                while True:
                    print(self.first_player_name + ' 现在正选择：' + self.player_sport_mains[self.player_cursor])
                    huang = input('请输入：')
                    if huang == 'q':
                        if self.player_cursor > int(len(self.player_sport_mains) - 2):
                            self.player_cursor -= 2
                        else:
                            print('无法进行此操作')         
                    if huang == 'a':
                        if self.player_cursor > int(len(self.player_sport_mains) - 1):
                            self.player_cursor -= 1
                        else:
                            print('无法进行此操作')  
                    elif huang == 'e':
                        if self.player_cursor < int(len(self.player_sport_mains) - 2):
                            self.player_cursor += 2
                        else:
                            print('无法进行此操作')   
                    elif huang == 'd':
                        if self.player_cursor < int(len(self.player_sport_mains) - 1):
                            self.player_cursor += 1
                        else:
                            print('无法进行此操作')

                    elif huang == 'w':
                        if self.player_cursor == 0:
                            if self.first_player_professional == '1':
                                ai_settings.second_player_hp = ai_settings.second_player_hp - self.first_player_normal_attacks

                            elif self.first_player_professional == '2':
                                if self.first_player_professional_zj_active == False:
                                    self.first_player_professional_zj_active = True
                                    print(self.first_player_name + '蓄力完毕')
                                else:
                                    self.first_player_professional_zj_active = False
                                    ai_settings.second_player_hp = ai_settings.second_player_hp - self.first_player_normal_attacks

                            else:
                                huang = 1
                                if ran.randint(1, 100) <= ai_settings.l_f_A_o:
                                    self.first_player_normal_attacks = 2 * self.first_player_normal_attacks
                                    if str(huang) == '2':
                                        print(self.first_player_name + '打出了暴击!')
                                    elif str(huang) > '2':
                                        print('OH,' + self.first_player_name + '打出了第' + str(huang-1) +'次暴击')
                                self.first_player_normal_attacks = huang * self.first_player_normal_attacks
                                ai_settings.second_player_hp = ai_settings.second_player_hp - self.first_player_normal_attacks

                            if self.first_player_professional == '2' and self.first_player_professional_zj_active == True:
                                print('本回合玩家 ' + self.first_player_name + ' 未造成伤害')
                            else:
                                print('第一位玩家造成了 ' + str(self.first_player_normal_attacks) + ' 点伤害')
                            print("第一位玩家血量为 " + str(ai_settings.first_player_hp))
                            print("第二位玩家血量为 " + str(ai_settings.second_player_hp))
                            break
                        
                        elif self.player_cursor == 1:
                            print('选项开发中')

                        elif self.player_cursor == 2:
                            while True:
                                if self.first_player_potions:
                                    print(self.first_player_name + ' 拥有的药水为:')
                                    for self.first_player_potion in self.first_player_potions:
                                        print('-' + self.first_player_potion)

                                    # 介绍
                                    print('可以输入相应数字选择药水')
                                    print("可以按'0'退出药水使用")
                            
                                    huang = input('请输入序号：')
                                    
                                    try:
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

                if self.game_over_active == False:
                    break
'''