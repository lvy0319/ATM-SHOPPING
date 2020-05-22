# -*- coding:utf-8 -*-

#购物主程序入口
import json,os,time

#获取程序路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep

#封装数据路径   os.sep返回当前系统的目录斜杠 用作兼容不同系统
__db_product = BASE_DIR  + "database" + os.sep + "product_list"
__db_shoping_car = BASE_DIR + "database" + os.sep + "shopping_car"
__db_users_dict = BASE_DIR + "database" + os.sep + "users_dict"
__db_creditcard_dict = BASE_DIR + "database" + os.sep + "creditcard_dict"

def Fetch():
    pro_list= []
    with open(__db_product, "r", encoding="utf-8") as f_product:
        for item in f_product:
            pro_list.append(item.strip('\n').split())
        print('商品编号\t商品名称\t商品价格')
        for index,items in enumerate(pro_list):
            #打印全部商品
            print('{}\t{}\t{}'.format(index,items[0],items[1]))

def Shopping():
    #加购物车接口
    shopping_list = []
    pro_list = []
    with open(__db_product, "r", encoding="utf-8") as f_product:
        for item in f_product:
            pro_list.append(item.strip('\n').split())
    while True:
        #打印商品列表
        Fetch()
        choice = input('选择要购买的商品编号 【购买 ID】/【返回 b】:')
        if choice.isdigit():
            choice = int(choice)
            if choice < len(pro_list) and choice >=0:
                #加购
                shopping = pro_list[choice]
                print('商品:{}已加入购物车'.format(shopping[0]))
                shopping_list.append(shopping)
            else:
                print('商品编号错误~！')
        elif choice == 'b':
            with open(__db_shoping_car, "r+") as f_shopping_car:
                lists = json.loads(f_shopping_car.read())
                lists.extend(shopping_list)
                f_shopping_car.seek(0)
                f_shopping_car.truncate(0)
                list = json.dumps(lists)
                f_shopping_car.write(list)
            break
        else:
            print('输入错误~')







def Shopping_car():
    #购物清单（包含总额）
    sum = 0
    with open(__db_shoping_car,'r') as f_shoping_car:
        shoping_car = json.loads(f_shoping_car.read())
        print('-----已购清单-----')
        print('商品编号\t商品名称\t商品价格')
        for index,items in enumerate(shoping_car):
            print('{}\t{}\t{}'.format(index,items[0],items[1]))
            sum = sum + int(items[1])
    print('消费：{}'.format(sum))


def Empty_shopping_car():
    #清空购物车
    with open(__db_shoping_car, "w") as f_shopping_car:
        list = json.dumps([])
        f_shopping_car.write(list)

def Pay_shopping(usercard):
    #结算
    sum = 0
    with open(__db_shoping_car, 'r') as f_shoping_car:
        shoping_car = json.loads(f_shoping_car.read())
        print('-----已购清单-----')
        print('商品编号\t商品名称\t商品价格')
        for index, items in enumerate(shoping_car):
            print('{}\t{}\t{}'.format(index, items[0], items[1]))
            sum = sum + int(items[1])
    while True:
            is_pay = input('当前商品总额：{}元 是否进行支付 确定【y】/返回【b】：'.format(sum))
            if is_pay == 'y':
                with open(__db_creditcard_dict,'r+') as f_creditcard_dict:
                    creditcard_dict = json.loads(f_creditcard_dict.read())
                    print(creditcard_dict)
                    limit = creditcard_dict[usercard]['limit'] - sum
                    if limit >= 0:
                        creditcard_dict[usercard]['limit'] = limit
                        dict = json.dumps(creditcard_dict)
                        f_creditcard_dict.seek(0)
                        f_creditcard_dict.truncate(0)
                        f_creditcard_dict.write(dict)
                        print('用户已结算，余额为{}'.format(limit))
                        #结算成功，清空购物车
                        Empty_shopping_car()
                        break
                    else:
                        print('您好，您的余额不足,请充值后购买')


            elif is_pay == 'b':
                break
            else:
                print('输入错误')

