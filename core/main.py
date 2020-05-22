#需求：
'''
1. 额度15000或自定义
2. 实现购物商城，加入购物车，调用信用卡接口结账
3. 可以提现，手续费5%  --未实现
4. 每月22号出账单，每月10号为还款日，过期未还，按欠款总额万分之5每日计息  --未实现
5. 支持多账户登录  --未实现
6. 支持账户间转账  --未实现
7. 记录每月日常消费流水  --未实现
8. 提供还款接口
9. ATM记录操作日志
10. 提供管理接口，包括添加账户、用户额度，冻结账户等。。。
11. 用户认证用装饰器
'''

import os,sys
#主程序入口

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep

sys.path.append(BASE_DIR)

from modules import admincenter as ad
from modules import shopping as sh

if __name__ == '__main__':
    while True:
        print('--------------')
        print('''
        1.管理后台
        2.购物流程
        ''')
        choice = input('请输入操作编号:')
        if choice == '1':
            while True:
                is_ad = input('请输入对应操作，1.创建用户 2，锁定用户 3.解锁用户 b.返回：')
                if is_ad == '1':
                    ad.User_create()
                elif is_ad == '2':
                    ad.Lock_user()
                elif is_ad == '3':
                    ad.Unlock_user()
                elif is_ad == 'b':
                    break
                else:
                    print('操作编号错误')
        elif choice == '2':
            while True:
                is_sh = input('请输入对应操作，1.加入购物车 2，查询购物车 3.清空购物车 4.结算 b.返回：')
                if is_sh == '1':
                    sh.Empty_shopping_car()
                    sh.Shopping()
                elif is_sh == '2':
                    sh.Shopping_car()
                elif is_sh == '3':
                    sh.Empty_shopping_car()
                elif is_sh == '4':
                    usercard = input('请输入用户卡号')
                    sh.Pay_shopping(usercard)
                elif is_sh == 'b':
                    break
                else:
                    print('操作编号错误!')
        elif choice == 'q':
            quit()
        else:
            print('操作编号错误!')
