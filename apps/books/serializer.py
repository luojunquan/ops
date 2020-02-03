# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 11:50
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : serializer.py
# @Software: PyCharm
from rest_framework import serializers
from books.models import Publish, Author, Book

class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = "__all__"

    '''
    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        self.Meta.model.objects.filter(id=instance.id).update(**validated_data)
        return instance
    '''

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

    '''
    def create(self, validated_data):
        instance = self.Meta.model.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        self.Meta.model.objects.filter(id=instance.id).update(**validated_data)
        return instance
    '''
class BookSerializer(serializers.ModelSerializer):
    # publisher = PublishSerializer()         # 默认显示PublishSerializer定义的所有列
    # authors = AuthorSerializer(many=True)   # 默认显示AuthorSerializer所有的列
    # publication_date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Book
        fields = "__all__"

    '''
    initial_data和validated_data区分：
    initial_data是客户端穿入没有经过to_internal_value的值,
    而validated_data是经过了to_internal_value方法
    '''
    # 序列化
    def to_author_response(self, author_queryset):
        ret = []
        # 多对多的结果是一个列表对象，需要遍历对象，将需要序列化的内容提出来即可
        for author in author_queryset:
            ret.append({
                'id': author.id,
                'name': author.name,
                'email': author.email
            })
        return ret

    def to_representation(self, instance):
        """将从 Model 取出的数据 parse 给 Api"""
        publisher_obj = instance.publisher
        authors = self.to_author_response(instance.authors.all())
        ret = super(BookSerializer, self).to_representation(instance)
        ret["publisher"] = {
            "id": publisher_obj.id,
            "name": publisher_obj.name,
            "address": publisher_obj.address
        },
        ret["authors"] = authors
        return ret

    def to_internal_value(self, data):
        """将客户端传来的 json 数据 parse 给 Model"""
        # print(data)
        pass

'''
    def create(self, validated_data):
        print(validated_data)  # {'name': '平凡的世界', 'publication_date': datetime.date(2018, 5, 10), 'publisher': <Publish: Publish object>, 'authors': [<Author: Author object>]}
        author_list = validated_data.pop('authors',[])
        instance = self.Meta.model.objects.create(**validated_data)
        # author和book是多对多关系，添加数据时需要单独处理
        instance.authors.set(author_list)
        return instance

    def update(self, instance, validated_data):
        author_list = validated_data.pop('authors', [])
        self.Meta.model.objects.filter(id=instance.id).update(**validated_data)
        # 多对多添加的两种写法
        instance.authors.add(*author_list)
        return instance
'''
