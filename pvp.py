import time

from settings import Settings

from game_functions import Huangame

def run_game():
    # 定义类名
    setting = Settings()
    huangame = Huangame()

    huangame.role_choice()
    huangame.role_initialize()
    huangame.game_start()

run_game()