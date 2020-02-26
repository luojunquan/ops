
from django.contrib.auth import get_user_model
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import viewsets, permissions, response
from rest_framework import mixins
# Create your views here.
from rest_framework.response import Response

from users.serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend

User = get_user_model()
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    retrieve:
        返回指定用户信息
    list:
        返回用户列表
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_fields = ('username',)
    # authentication_classes = (SessionAuthentication,)
    extra_perm_map = {
        "GET":['auth.view_user']
    }

class UserInfoViewset(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    def list(self, request, *args, **kwargs):
        data = {
            "username": "admin",
            # "name": "rock"
        }
        return response.Response(data)

class DashboardStatusViewset(viewsets.ViewSet):
    '''
    list:
        获取dashboard状态数据
    '''
    permission_classes = (IsAuthenticated,)
    def list(self, request, *args, **kwargs):
        data = self.get_content_data()
        return Response(data)
    def get_content_data(self):
        return {
            "aa":11,
            "bb":22
        }
    '''
    #原始搜索
    def get_queryset(self):
        queryset = super(UserViewSet, self).get_queryset()
        username = self.request.query_params.get('username',None)
        if username:
            queryset = queryset.filter(username__icontains=username)
        return queryset
    '''

