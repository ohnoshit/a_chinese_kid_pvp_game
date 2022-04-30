import game_functions as gf

def run_game():
    p_name_active = False

    while p_name_active == False:
        huang = input('是否自定义名字(y/n)')

        if huang == 'y':
            fp_name = input('请输入第一位玩家的名字:')
            sp_name = input('请输入第二位玩家的名字:')

            print('第一位玩家的名字是：' + fp_name + ' 。')
            print('第二位玩家的名字是：' + sp_name + ' 。')
            huang = input('请确认你们的姓名(y/n)')

            if huang == 'y':
                print('完成名字选择')
                p_name_active = False
                break
            elif huang == 'n':
                print('\n请重新输入名字')
            else:
                print('\n选择错误,请重新输入')
                
        elif huang == 'n':
            fp_name = '玩家1'
            sp_name = '玩家2'
            print('设置成功')
            p_name_active = True
            break

        else:
            print("输入错误")

    # 定义两个玩家类
    fp = gf.Game(fp_name)
    sp = gf.Game(sp_name)

    # 玩家选择职业
    fp.role_choice()
    sp.role_choice()

    fp.initialize_game()
    sp.initialize_game()

