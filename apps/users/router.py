from rest_framework.routers import DefaultRouter
from .views import UsersViewset, UserInfoViewset, GroupsViewset, UserGroupsViewset, GroupMembersViewset
from .views import PermissionsViewset, GroupsPermViewset

users_router = DefaultRouter()
users_router.register(r'user', UsersViewset, basename="user")
users_router.register(r'userinfo', UserInfoViewset, basename="userinfo")
users_router.register(r'group', GroupsViewset, basename="group")
users_router.register(r'usergroup', UserGroupsViewset, basename="usergroup")
users_router.register(r'groupmembers', GroupMembersViewset, basename="groupmembers")

users_router.register(r'permission', PermissionsViewset, basename="permission")
users_router.register(r'grouppower', GroupsPermViewset, basename="grouppower")
