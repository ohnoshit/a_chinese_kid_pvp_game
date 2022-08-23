from random import randint as ra

class Game():
    
    def __init__(self):
        p_name_active = False

        while p_name_active == False:   

            self.p_name = input('请输入你的名字:')

            print('玩家的名字是：' + self.p_name + ' 。')
            huang = input('请确认你的姓名(y/n)')

            if huang == 'y':
                print('完成名字选择')
                p_name_active = False
                break
            elif huang == 'n':
                print('\n请重新输入名字')
            else:
                print('\n选择错误,请重新输入')

        # 定义数值

        # 伤害
        
        # 普攻（平A）伤害
        self.s_r_A_l = 5
        self.s_r_A_h = 7
        self.z_j_A_l = 10
        self.z_j_A_h = 15
        self.l_f_A_l = 3
        self.l_f_A_h = 4 

        # 暴击伤害(倍数) critical strike damage
        self.p_c_d = 1.5

        
        # 玩家血量
        self.p_hp = 50

        # 几率
        # 平A暴击概率
        self.s_r_A_o = 5                           
        self.z_j_A_o = 7
        self.l_f_A_o = 3

        # 冷锋麻痹几率
        self.l_f_A_p_o = 40

        # 药水无效几率                               
        self.p_p_m_o = 15                                   
        self.s_p_m_o = 25
        self.t_p_m_o = 40

        # 商店 shop
        # 玩家硬币
        self.p_coins = 100

        # 分商店名称
        self.sh_pl_hp = '催逝员老冯'
        self.sh_pl_potion = '女巫的房子'
        self.sh_pl_weapon = '打铁匠'
        self.sh_pl_skill = '训练师'
        self.sh_pl_armon = '牛头丸' 

        # 药水 potion
        # 治疗药水 healing potion
        self.pri_hepo_p = 1                  # 1级治疗药水价格
        self.pri_hepo_l = 1                  # 1级治疗药水回复最低血量
        self.pri_hepo_h = 2                  # 1级治疗药水回复最高血量

        self.sec_hepo_p = 5                # 2级治疗药水价格
        self.sec_hepo_l = 5                # 2级治疗药水回复最低血量
        self.sec_hepo_h = 7                # 2级治疗药水回复最高血量

        self.ter_hepo_p = 15                  # 三级治疗药水
        self.ter_hepo_l = 17
        self.ter_hepo_h = 22

        # 恢复药水 recovery potion
        self.pri_repo_p = 3
        self.pri_repo_l = 1
        self.pri_repo_h = 2

        # 力量药水 power potion
        self.pri_popo_p = 3
        self.pri_popo_l = 3
        self.pri_popo_h = 4

        # 武器

        # 轻剑（双刃）
        '''铁剑的购买可以最小代价使用双刃回旋(无特殊功能)'''
        self.铁剑 = 3
        '''吸血剑有30%回复普攻伤害的50%,5%概率回复普攻伤害的100%(不可叠加回复，先进行回复100%的判定)'''
        self.吸血剑 = 30
        '''造成最高伤害时额外造成2点伤害'''
        self.鱼鳞剑 = 10

        # 重剑（重剑）
        '''增加30%暴击率，0.5暴击率'''
        self.华金 = 65

        # 匕首（冷锋）
        '''攻击有80%概率额外造成1点伤害'''
        self.高频匕首 = 10
        '''攻击有20%概率额外造成1点伤害'''
        self.低频匕首 = 3
        '''增加10%暴击率'''
        self.暴击匕首 = 20
        '''初始增加20%麻痹率，每攻击一次减少2%的几率（至多20%）'''
        self.寒冰 = 20
        '''麻痹一次对手回复2点血量'''
        self.饮刃 = 30

        # 防具

        # 通用
        '''增加1点物理防御'''
        self.皮革衣 = 18

        # 双刃
        '''增加10%抗性,3%暴击概率'''
        self.树叶手套 = 7
        '''增加1点物理防御,每当你受到药水效果,获得1-2点瞬时护盾(护盾最高积累至3点)'''
        self.魔抗衣 = 40

        # 重剑
        '''当你蓄力时,提供70%物理抗性'''
        self.精钢盾牌 = 50
        '''增加50%的物理抗性'''
        self.锁子甲 = 70

        # 冷锋
        '''增加1点物理抗性,增加100%吸血回复血量'''
        self.嗜血血衣 = 40

        # 附魔

        # 通用
        self.一级暴击概率提升 = 3
        self.二级暴击概率提升 = 10
        
        self.一级暴击伤害提升 = 3
        self.二级暴击伤害提升 = 10

        # 技能
        
        # 双刃
        self.双刃回旋 = 5
        self.防御 = 5

        # 重剑
        self.重剑突击 = 10     
        self.格挡 = 6

        # 冷锋
        self.无影无踪 = 15
        self.斩杀 = 7


    def game_ready(self):
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

        # 角色伤害和武器定义
        if self.p_pro == '1':
            self.p_A_h = self.s_r_A_h
            self.p_A_l = self.s_r_A_l

            self.p_wes = ['勇者之剑']   # 定义武器栏
            self.p_ars = []            # 定义装备栏
            self.p_pos = []            #定义药水栏
        elif self.p_pro == '2':
            self.p_A_h = self.z_j_A_h
            self.p_A_l = self.z_j_A_l

            self.p_wes = ['沉重的玄铁剑']
            self.p_ars = [] 
            self.p_pos = []
        else:
            self.p_A_h = self.l_f_A_h
            self.p_A_l = self.l_f_A_l

            self.p_wes =['师傅的匕首']
            self.p_ars = []
            self.p_pos = []

    def shop(self):
        # 欢迎语
        print('欢迎来到商店')
        print('请你选择想要的商品')
        print('购买商品需要花费硬币')
        print("输入'q'退出")
        print('商品如下:')

        self.sh_pls = [self.sh_pl_hp, self.sh_pl_potion,self.sh_pl_weapon,
            self.sh_pl_armon, self.sh_pl_skill]

        # 商品名称及价格设置
        self.sh_pos = {
                '一级治疗药水' : str(self.pri_hepo_p),
                '二级治疗药水' : str(self.sec_hepo_p),
                '三级治疗药水' : str(self.ter_hepo_p),
                '一级恢复药水' : str(self.pri_repo_p),
                '一级力量药水' : str(self.pri_popo_p),                
            }     

        self.sh_s_r_wes = {
            '铁剑' : str(self.铁剑),
            '吸血剑' : str(self.吸血剑),
            '鱼鳞剑' : str(self.鱼鳞剑),
            } 

        self.sh_z_j_wes = {
                '华金' : str(self.华金),
            }

        self.sh_l_f_wes = {
                '低频匕首' : str(self.低频匕首),
                '高频匕首' : str(self.高频匕首),
                '暴击匕首' : str(self.暴击匕首),
                '寒冰' : str(self.寒冰),
                '饮刃' : str(self.饮刃),
            }

        self.sh_s_r_sks = {
                '双刃回旋': self.双刃回旋,
                "防御": self.防御
            } 

        self.sh_z_j_sks = {
                '重剑突击': self.重剑突击,
                "格挡": self.格挡
            }

        self.sh_l_f_sks = {
                '无影无踪': self.无影无踪,
                '斩杀': self.斩杀
            }

        while True:
            self.huang = 1
            for self.shop_place in self.sh_pls:
                print(str(self.huang) + ':' + self.shop_place)
                self.huang += 1                                  
            self.huang = input('请' + self.p_name + ' 选择购买人、地:\n')  

            # 创建药水数量标志——当药水数量=9瓶时，停止卖药
            self.p_pos_num_active = False

            # 创建药水数量标志——当药水数量=9瓶时，停止卖药
            self.p_pos_num_active = False

            if self.huang == '1':
                print("老冯去世了！还是改日吧！")
                if ra(1,100) <= 30:
                    huang = input("是否为老冯投一枚硬币许愿？(y/n)")
                    if huang == 'y' and self.p_coins > 0:
                        self.p_coins = self.p_coins - 1
                        print("老冯感谢你!")
                        if ra(1,10) <= 5:
                            print("天皇比啥！\n老冯重获新生!")
                            print("开发ing(恭喜你解锁隐藏彩蛋！)")
                            
                        

            elif self.huang == '2':
                while self.p_pos_num_active == False:
                    self.huang = 1
                    for self.sh_th_na, self.sh_th_pr in self.sh_pos.items():
                        print(str(self.huang) + ':' + self.sh_th_na + ' 价格为 ' + self.sh_th_pr)
                        self.huang += 1   
                    self.huang = input('请' + self.p_name + '输入数字以购买商品')    

                    if self.huang == '1':
                        if self.p_coins >= self.pri_hepo_p:
                            self.p_pos.append('一级治疗药水')
                            self.p_coins = self.p_coins - self.pri_hepo_p
                            print(self.p_name + '成功购买 一级治疗药水')
                            print(self.p_name + ' 还有 ' + str(self.p_coins) + ' 个硬币')
                            print(self.p_name + ' 拥有的药水:')
                            for self.p_po in self.p_pos:
                                print('-' + self.p_po)
                        else:
                            print('您的硬币不足')

                    elif self.huang == '2':
                        if self.p_coins >= self.sec_hepo_p:
                            self.p_pos.append('二级治疗药水')
                            self.p_coins = self.p_coins - self.sec_hepo_p
                            print(self.p_name + '成功购买 二级治疗药水')
                            print(self.p_name + ' 还有 ' + str(self.p_coins) + ' 个硬币')
                            print(self.p_name + ' 拥有的药水:')
                            for self.p_po in self.p_pos:
                                print('-' + self.p_po)          

                        else:
                            print('您的硬币不足')       

                    elif self.huang == '3':
                        if self.p_coins >= self.ter_hepo_p:                                               
                            self.p_pos.append('三级治疗药水')
                            self.p_coins = self.p_coins - self.ter_hepo_p
                            print(self.p_name + '成功购买 三级治疗药水')
                            print(self.p_name + ' 还有 ' + str(self.p_coins) + ' 个硬币')
                            print(self.p_name + ' 拥有的药水:')
                            for self.p_po in self.p_pos:
                                print('-' + self.p_po)          
                        else:
                            print('您的硬币不足')       

                    elif self.huang == '4':
                        if self.p_coins >= self.pri_repo_p:                                                  
                            self.p_pos.append('一级恢复药水')
                            self.p_coins = self.p_coins - self.pri_repo_p
                            print(self.p_name + '成功购买 一级恢复药水')
                            print(self.p_name + ' 还有 ' + str(self.p_coins) + ' 个硬币')
                            print(self.p_name + ' 拥有的药水:')
                            for self.p_po in self.p_pos:
                                print('-' + self.p_po)          
                        else:
                            print('您的硬币不足')           

                    elif self.huang == '5':
                        if self.p_coins >= self.pri_popo_p:                                                
                            self.p_pos.append('一级力量药水')
                            self.p_coins = self.p_coins - self.pri_popo_p
                            print(self.p_name + '成功购买 一级力量药水')
                            print(self.p_name + ' 还有 ' + str(self.p_coins) + ' 个硬币')
                            print(self.p_name + ' 拥有的药水:')
                            for self.p_po in self.p_pos:
                                print('-' + self.p_po)          
                        else:
                            print('您的硬币不足')  

                    if len(self.p_pos) == 9:
                        print("药水栏已满！")
                        self.p_pos_num_active = True

                else:
                    print("药水栏已满！你无法再购买药水！")


            elif self.huang == '3':
                print('欢迎来到打铁铺! ' + self.p_name + '!')    

                try:
                    if self.p_pro== '1':
                        while True:
                            self.huang = 1
                            for self.shop_weapon_name, self.shop_weapon_price in self.sh_s_r_wes.items():
                                print(str(self.huang) + '-' + self.shop_weapon_name + ':' + self.shop_weapon_price)
                                self.huang += 1
                            self.huang = input('请输入数字以购买武器:')

                            if int(self.huang) == 1:
                                if self.p_coins >= self.铁剑:
                                    if len(self.p_wes) == 2:
                                        self.huang = input(self.p_name + ' 已有武器，你确定要更换武器吗?(y/n)')
                                        if self.huang == 'y':
                                            self.p_coins -= self.铁剑
                                            self.huang = input('请选择要替换那一只手的武器（',self.p_wes[1],' ',self.p_wes[2],')')
                                            self.p_wes[1] = '铁剑'
                                            print(self.p_name + ' 的武器为: ')
                                            for self.first_player_weapon in self.p_wes:
                                                print('- ' + self.first_player_weapon)
                                            print(self.p_name + ' 的硬币数量为： ' + 
                                                str(self.p_coins))
                                        elif self.huang == 'n':
                                            print(self.p_name + ' 取消了购买')
                                            print(self.p_name + ' 的武器为: ')
                                            for self.p_we in self.p_wes:
                                                print('- ' + self.p_we)
                                        else:
                                            print('输入错误')

                                    else:
                                        self.p_coins -= self.铁剑
                                        self.p_wes.append('铁剑')
                                        print(self.p_name + ' 的武器为: ')
                                        for self.p_we in self.p_wes:
                                            print('- ' + self.p_we)
                                        print(self.p_name + ' 的硬币数量为： ' + 
                                            str(self.p_coins))
                                else:
                                    print(self.p_name + ' 硬币不足')

                except:
                    pass