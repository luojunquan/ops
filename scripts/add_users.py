# -*- coding: utf-8 -*-
# @Time    : 2019/12/30 17:07
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : add_users.py
# @Software: PyCharm
import sys,os

project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(project_dir)
#django环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ops.settings")

import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()

def get_users():
    for user in User.objects.all():
        print(user.username)

if __name__ == "__main__":
    get_users()