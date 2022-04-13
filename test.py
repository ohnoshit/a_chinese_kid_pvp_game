huang




        
        while True:
            huang = 1
            for self.shop_thing_name, self.shop_thing_price in self.shop_things.items():
                print(str(huang) + ':' + self.shop_thing_name + ' 价格为 ' + self.shop_thing_price)
                huang += 1

            while True:
                huang = input('请' + self.second_player_name + '输入数字以购买商品')

                if huang == '1':
                    if ai_settings.second_player_coins >= 20:
                        ai_settings.second_player_coins = ai_settings.second_player_coins - 20
                        print('玩家 ' + self.second_player_name + ' 还有 ' + str(ai_settings.second_player_coins) + ' 个硬币')
                        ai_settings.second_player_hp = ai_settings.second_player_hp + 10
                        print('玩家 ' + self.second_player_name + ' 血量为 ' + str(ai_settings.second_player_hp) + ' 点')
                    else:
                        print('您的硬币不足')

                elif huang == '2':
                    if ai_settings.second_player_coins >= 35:
                        ai_settings.second_player_coins = ai_settings.second_player_coins - 35
                        print('玩家 ' + self.second_player_name + ' 还有 ' + str(ai_settings.second_player_coins) + ' 个硬币')
                        ai_settings.second_player_hp = ai_settings.second_player_hp + 20
                        print('玩家 ' + self.second_player_name + ' 血量为 ' + str(ai_settings.second_player_hp) + ' 点')
                    else:
                        print('您的硬币不足')

                elif huang == '3':
                    if ai_settings.second_player_coins >= ai_settings.primary_healing_potion_p:
                        if len(self.first_player_potions) < 9:
                            self.second_player_potions.append('一级治疗药水')
                            ai_settings.second_player_coins = ai_settings.second_player_coins - ai_settings.primary_healing_potion_p
                            print(self.second_player_name + '成功购买一级治疗药水')
                            for self.second_player_potion in ai_settings.second_player_potions:
                                print('-' + self.second_player_potion)
                        else:
                            print('不得够买超过9瓶药水')
                    else:
                        print('您的硬币不足')
                
                elif huang == '4':
                    if ai_settings.second_player_coins >= ai_settings.secondary_healing_potion_h:
                        if len(self.first_player_potions) < 9:                        
                            self.second_player_potions.append('二级治疗药水')
                            ai_settings.second_player_coins = ai_settings.second_player_coins - ai_settings.secondary_healing_potion_h
                            print(self.second_player_name + '成功购买 二级治疗药水')
                            for self.second_player_potion in ai_settings.second_player_potions:
                                print('-' + self.second_player_potion)
                        else:
                            print('不得够买超过9瓶药水')
                    else:
                        print('您的硬币不足')

                elif huang == '5':
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

                elif huang == '6':
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

                elif huang == '7':
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
                    print('玩家 ' + self.second_player_name + ' 结束购买')
                    break
                else:
                    print('你输入有误，请重新输入')