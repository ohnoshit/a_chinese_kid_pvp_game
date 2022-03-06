class Settings():

    def __init__(self):
        # 玩家血量
        self.first_player_hp = 100
        self.second_player_hp = 100

        # 商店 shop
        # 玩家硬币
        self.first_player_coins = 100
        self.second_player_coins = 100


        # 药水 potion

        # 治疗药水 healing potion
        self.first_player_primary_healing_potion = 0       # 第一位玩家的1级治疗药水数量
        self.second_player_primary_healing_potion = 0      # 第二位玩家的1级治疗药水数量
        self.primary_healing_potion_l = 1                  # 1级治疗药水回复最低血量
        self.primary_healing_potion_h = 2                  # 1级治疗药水回复最高血量
        self.first_player_secondary_healing_potion = 0     # 第一位玩家的2级治疗药水数量
        self.second_player_secondary_healing_potion = 0    # 第二位玩家的2级治疗药水数量
        self.secondary_healing_potion_l = 5                # 2级治疗药水回复最低血量
        self.secondary_healing_potion_h = 7                # 2级治疗药水回复最高血量

        # 普攻（平A）伤害
        self.s_r_A_l = 5
        self.s_r_A_h = 7
        self.z_j_A_l = 10
        self.z_j_A_h = 15
        self.l_f_A_l = 3
        self.l_f_A_h = 4

        # 几率
        self.l_f_A_o = 40