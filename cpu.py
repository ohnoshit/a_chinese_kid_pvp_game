import game_functions as gf

def run_game():
    # 定义两个玩家类
    fp = gf.Game()
    sp = gf.Game()

    # 玩家选择职业和初始化
    fp.game_ready()
    sp.game_ready()

    print(str(fp.p_pro))

    fp.shop()