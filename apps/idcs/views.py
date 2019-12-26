from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status,viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import generics,mixins

from idcs.models import Idc
from .serializers import IdcSerializer, UserSerializer
from rest_framework.renderers import JSONRenderer


############################Idc版本一#############################
# 重写JSONResponse
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        # 将序列化的转成json
        content = JSONRenderer().render(data)
        super(JSONResponse, self).__init__(content=content, **kwargs)

def idc_list(request, *args, **kwargs):
    if request.method == 'GET':
        # 获取queryset
        queryset = Idc.objects.all()
        # 将queryset给序列化类
        serializer = IdcSerializer(queryset, many=True)
        # content = JSONRenderer().render(serializer.data)
        # return HttpResponse(content,content_type='application/json')
        # 转json
        return JSONResponse(serializer.data)  # 这一行相当于上面两行，重写了JSONResponse
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IdcSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
    return HttpResponse('')

def idc_detail(requset, pk, *args, **kwargs):
    try:
        idc = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist:
        return HttpResponse(status=404)
    if requset.method == 'GET':
        # 进行序列化
        serializer = IdcSerializer(idc)
        return JSONResponse(serializer.data)
    # 修改
    elif requset.method == 'PUT':
        content = JSONParser().parse(requset)
        serializer = IdcSerializer(idc, data=content)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.data, status=400)
    elif requset.method == 'DELETE':
        idc.delete()
        return HttpResponse(status=204)

############################Idc版本二#############################
@api_view(['GET', 'POST'])
def idc_list_v2(request, *args, **kwargs):
    if request.method == 'GET':
        queryset = Idc.objects.all()
        serailizer = IdcSerializer(queryset, many=True)
        return Response(serailizer.data)
    elif request.method == 'POST':
        serailizer = IdcSerializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data, status=status.HTTP_201_CREATED)
        return Response(serailizer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def idc_detail_v2(request, pk, *args, **kwargs):
    try:
        idc = Idc.objects.get(pk=pk)
    except Idc.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = IdcSerializer(idc)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = IdcSerializer(idc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        idc.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def api_root(request, format=None, *args, **kwargs):
    return Response({
        'idcs': reverse('idc_list', request=request, format=format),
        'users': reverse('user_list',request=request,format=format),
    })

############################Idc版本三#############################
class IdcList(APIView):
    def get(self,request,format=None):
        queryset = Idc.objects.all()
        serializer = IdcSerializer(queryset,many=True)
        return Response(serializer.data)
    def post(self,request,format=True):
        serializer = IdcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_404_NOT_FOUND)

class IdcDetail(APIView):
    def get_object(self,pk):
        try:
            Idc.objects.get(pk)
        except Idc.DoesNotExist:
            raise Http404

    def get(self,pk,request,format=None):
        idc = self.get_object(pk)
        serializer = IdcSerializer(idc)
        return Response(serializer.data)

    def put(self,pk,request,format=None):
        idc = self.get_object(pk)
        serializer = IdcSerializer(idc,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def delete(self,pk,request,format=None):
        idc = self.get_object(pk)
        idc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

############################Idc版本三(混合)#############################
class IdcListV2(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

class IdcDetailV2(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):

    queryset = Idc.objects.all()
    serializer_class = IdcSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)
############################Idc版本四(混合)#############################
class IdcListV3(generics.ListCreateAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
class IdcDetailV3(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
############################Idc版本四(ViewSet)#############################
class IdcListDetailViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,
                           mixins.ListModelMixin,mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin,mixins.UpdateModelMixin):
    queryset = Idc.objects.all()
    serializer_class = IdcSerializer
#####################用户序列化#########################################
@api_view(['GET', 'POST'])
def user_list(request, *args, **kwargs):
    if request.method == 'GET':
        queryset = User.objects.all()
        user = UserSerializer(queryset, many=True)
        return Response(user.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, *args, **kwargs):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#####################用户序列化版本二###################################
class UserList(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.post(request,*args,**kwargs)

class UserDetail(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)

#####################用户序列化版本三####################################
class UserListV2(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailV2(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#####################用户序列化版本三(ViewSet)####################################
# class UserListDetailSet(viewsets.GenericViewSet,mixins.CreateModelMixin,
    # #                            mixins.ListModelMixin,mixins.RetrieveModelMixin,
    # #                            mixins.DestroyModelMixin,mixins.UpdateModelMixin):
class UserListDetailSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer