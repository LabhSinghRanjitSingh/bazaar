from django.shortcuts import render
from django.contrib.auth.models import User, Group
from wholesale.models import Book, Brand, Piece, ClothType, PieceImage
from rest_framework import viewsets
from frontend.serializers import UserSerializer, GroupSerializer, BookSerializer, BrandSerializer, PieceSerializer, \
    ClothTypeSerializer, PieceImageSerializer
from frontend.models import Slider, Scroller
from django.db.models import Count


class PageView:
    def __init__(self):
        pass

    def init(self):
        self.data = {}
        brands = Brand.objects.all()
        self.data["brands"] = Brand.objects.all()
        self.data["clothtypes"] = ClothType.objects.all()
        self.data["piecesCountList"] = ["1-5", "6-10", "11-15", "16-20", "More than 20"]

    def home(self, request):
        self.init()
        slides = Slider.objects.all()
        tags = Scroller.objects.values('tag').annotate(dcount=Count('tag'))
        tagsData = {}
        for tag in tags:
            tagsData[tag["tag"]] = [x.book for x in Scroller.objects.filter(tag=tag["tag"])]

        self.data["slides"] = slides
        self.data["tagsData"] = tagsData
        self.data["tags"] = tags

        return render(request, 'wholesale/index.html', self.data)

    def book(self, request, id):
        self.init()
        book = Book.objects.get(pk=int(id))
        self.data["book"] = book
        return render(request, 'wholesale/book.html', self.data)

    def books(self, request):
        self.init()
        kargs = {}
        if request.GET:
            if request.GET.get("brands"):
                brandName = request.GET.get("brands").split(",")
                kargs["brand__name__in"] = brandName

            if request.GET.get("clothtypes"):
                clothtypesName = request.GET.get("clothtypes").split(",")
                pieces = Piece.objects.filter(clothType__name__in=clothtypesName)
                kargs["pk__in"] = [piece.book.id for piece in pieces]

        books = Book.objects.filter(**kargs)

        self.data["books"] = books
        return render(request, 'wholesale/books.html', self.data)

    def contactus(self, request):
        self.init()
        return render(request, 'wholesale/contactus.html', self.data)

    def shoppingCart(self, request):
        self.init()
        return render(request, 'wholesale/shopingcart.html', self.data)


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
