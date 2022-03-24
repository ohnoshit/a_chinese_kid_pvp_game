class Settings():

    def __init__(self):
        # 玩家背包
        self.first_player_weapon = []   # 玩家一的武器
        self.second_player_weapon = []  # 玩家二的武器
        
        self.first_player_armon = []    # 玩家一的护甲
        self.second_player_armon = []   # 玩家二的护甲

        self.first_player_potions = []   # 玩家一的药水
        self.second_player_potions = []   # 玩家二的药水

        # 玩家血量
        self.first_player_hp = 100
        self.second_player_hp = 100

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


        # 普攻（平A）伤害
        self.s_r_A_l = 5
        self.s_r_A_h = 7
        self.z_j_A_l = 10
        self.z_j_A_h = 15
        self.l_f_A_l = 3
        self.l_f_A_h = 4

        # 几率
        self.l_f_A_o = 40                                 # 冷锋重复攻击几率