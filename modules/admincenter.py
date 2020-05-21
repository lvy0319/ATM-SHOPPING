# -*- coding:utf-8 -*-
#管理模块
import os,json

#获取当前项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#封装数据文件路径
__db_users_dict = BASE_DIR +'\\database\\users_dict'
__creditcard_dict = BASE_DIR +'\\database\\creditcard_dict'

def User_create(address='None',creditcard=0,locked=0):
    #创建用户
    while True:
        print('开始创建用户!')
        with open(__db_users_dict,'r+') as f_users_dict:
            users_dict  = json.loads(f_users_dict.read())
            #print(users_dict)
            for key in users_dict :
                print('已有用户名：{}'.format(key))
            is_create = input('是否创建新的用户 确定【y】/返回【b】:')
            if is_create == 'y':
                username = input("输入要添加账户的用户名：")
                password = input("输入添加账户的密码：")
                if username not in users_dict :
                    if len(username) > 0:
                        if len(password) > 0:
                            users_dict[username]={"username":username,"password":password,"creditcard":creditcard,"address":address,\
                                                 "locked":locked}
                            dict_u = json.dumps(users_dict)
                            f_users_dict.seek(0)
                            f_users_dict.truncate(0)
                            f_users_dict.write(dict_u)
                            print('用户创建成功！用户名:{}'.format(username))
                        else:
                            print('密码为空')
                    else:
                        print('用户名为空')
                else:
                    print('用户名已存在')
            elif is_create == 'b':
                break
            else:
                print('输入有误，请重新输入')





def Lock_user():
    #锁定用户
    while True:
        with open(__db_users_dict,'r+') as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            for keys in users_dict:
                print('用户名：{},当前状态：{}'.format(keys,users_dict[keys]['locked']))
            is_lock = input('请输入要锁定的用户名，按【b】返回：')
            if is_lock in users_dict:
                if users_dict[is_lock]['locked'] == 0:
                    users_dict[is_lock]['locked'] = 1
                    print('用户{}已锁定'.format(is_lock))
                    users_lock = json.dumps(users_dict)
                    f_users_dict.seek(0)
                    f_users_dict.truncate(0)
                    f_users_dict.write(users_lock)
                else:
                    print('该用户已是锁定状态')
            elif is_lock == 'b':
                break
            else:
                print('无此用户')



def Unlock_user():
    #解锁用户
    while True:
        with open(__db_users_dict,'r+') as f_users_dict:
            users_dict = json.loads(f_users_dict.read())
            for keys in users_dict:
                print('用户名：{},当前状态：{}'.format(keys,users_dict[keys]['locked']))
            is_lock = input('请输入要锁定的用户名，按【b】返回：')
            if is_lock in users_dict:
                if users_dict[is_lock]['locked'] == 1:
                    users_dict[is_lock]['locked'] = 0
                    print('用户{}已解锁'.format(is_lock))
                    users_lock = json.dumps(users_dict)
                    f_users_dict.seek(0)
                    f_users_dict.truncate(0)
                    f_users_dict.write(users_lock)
                else:
                    print('该用户未被锁定')
            elif is_lock == 'b':
                break
            else:
                print('无此用户')


