class Settings():

    def __init__(self):
        # 玩家背包
        self.first_player_weapons = []   # 玩家一的武器
        self.second_player_weapons = []  # 玩家二的武器
        
        self.first_player_armons = []    # 玩家一的护甲
        self.second_player_armons = []   # 玩家二的护甲

        self.first_player_potions = []   # 玩家一的药水
        self.second_player_potions = []   # 玩家二的药水

        # 玩家血量
        self.first_player_hp = 50
        self.second_player_hp = 50

        # 商店 shop
        # 玩家硬币
        self.first_player_coins = 100
        self.second_player_coins = 100

        #
        self.shop_place_hp = '催逝员老冯'
        self.shop_place_potion = '女巫的房子'
        self.shop_place_weapon = '打铁匠'
        self.shop_place_armon = '附魔带师' 

        # 药水 potion

        # 治疗药水 healing potion
        self.primary_healing_potion_p = 1                  # 1级治疗药水价格
        self.primary_healing_potion_l = 1                  # 1级治疗药水回复最低血量
        self.primary_healing_potion_h = 2                  # 1级治疗药水回复最高血量

        self.secondary_healing_potion_p = 5                # 2级治疗药水价格
        self.secondary_healing_potion_l = 5                # 2级治疗药水回复最低血量
        self.secondary_healing_potion_h = 7                # 2级治疗药水回复最高血量

        self.tertiary_healing_potion_p = 15                  # 三级治疗药水
        self.tertiary_healing_potion_l = 17
        self.tertiary_healing_potion_h = 22

        # 恢复药水 recovery potion
        self.primary_recovery_potion_p = 3
        self.primary_recovery_potion_l = 1
        self.primary_recovery_potion_h = 2

        # 力量药水 power potion
        self.primary_power_potion_p = 3
        self.primary_power_potion_l = 3
        self.primary_power_potion_h = 4

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

        # 伤害

        # 暴击伤害 critical strike damage
        self.f_p_c_d = 1.5
        self.s_p_c_d = 1.5

        # 普攻（平A）伤害
        self.s_r_A_l = 5
        self.s_r_A_h = 7
        self.z_j_A_l = 10
        self.z_j_A_h = 15
        self.l_f_A_l = 3
        self.l_f_A_h = 4

        # 商店血量价格
        self.shop_hp_p = 1

        # 商店伤害价格
        self.shop_s_r_d_p = 12
        self.shop_z_j_d_p = 7
        self.shop_l_f_d_p = 20

        # 商店伤害增加
        self.shop_s_r_d_p_a = 10
        self.shop_z_j_d_p_a = 5
        self.shop_l_f_d_p_a = 15

        # 几率

        # 平A暴击概率
        self.s_r_A_o = 30                              
        self.z_j_A_o = 75
        self.l_f_A_o = 10

        # 冷锋麻痹几率
        self.l_f_A_p_o = 40

        # 药水无效几率                               
        self.p_p_m_o = 15                                   
        self.s_p_m_o = 25
        self.t_p_m_o = 40