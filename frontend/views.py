from django.shortcuts import render
from django.contrib.auth.models import User, Group
from wholesale.models import Book,Brand,Piece,ClothType,PieceImage
from rest_framework import viewsets
from frontend.serializers import UserSerializer, GroupSerializer,BookSerializer,BrandSerializer,PieceSerializer,ClothTypeSerializer,PieceImageSerializer
from frontend.models import Slider,Scroller
from django.db.models import Count


class PageView:
    def __init__(self):
        pass

    def home(self, request):
        slides = Slider.objects.all()
        tags = Scroller.objects.values('tag').annotate(dcount=Count('tag'))
        brands = Brand.objects.all()
        tagsData = {}
        for tag in tags:
            tagsData[tag["tag"]] = [ x.book for x in Scroller.objects.filter(tag=tag["tag"])]
        data = {"slides":slides,"tagsData":tagsData,"tags":tags,"brands":brands}
        print(tagsData)
        return render(request, 'wholesale/index.html',data)

    def book(self,request,id):
        book = Book.objects.get(pk=int(id))
        data = {"book":book}
        return render(request, 'wholesale/book.html',data)

    def books(self,request):
        books = Book.objects.all()
        brands = Brand.objects.all()
        data = {"books":books,"brands":brands}
        return render(request, 'wholesale/books.html',data)

    def contactus(self,request):
        return render(request,'wholesale/contactus.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Book to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BrandViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Book to be viewed or edited.
    """
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class PieceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Book to be viewed or edited.
    """
    queryset = Piece.objects.all()
    serializer_class = PieceSerializer

class ClothTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Book to be viewed or edited.
    """
    queryset = ClothType.objects.all()
    serializer_class = ClothTypeSerializer


class PieceImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Book to be viewed or edited.
    """
    queryset = PieceImage.objects.all()
    serializer_class = PieceImageSerializer
