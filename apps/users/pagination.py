# -*- coding: utf-8 -*-
# @Time    : 2019/12/30 22:00
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : pagination.py
# @Software: PyCharm
from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    def get_page_size(self, request):
        try:
            #0值为全部
            page_size = int(request.query_params.get('page_size',-1))
            if page_size < 0:
                return self.page_size
            return page_size
        except:
            pass
        return self.page_size