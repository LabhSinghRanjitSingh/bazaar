from django.contrib.auth.models import User, Group
from rest_framework import serializers
from wholesale.models import Book,Brand,Piece,ClothType,PieceImage

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'brand','pieces','cover','description')


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ('name','logo')


class PieceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Piece
        fields = ('name', 'clothType','description')


class ClothTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClothType
        fields = ('name','description')


class PieceImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PieceImage
        fields = ('image','piece')
