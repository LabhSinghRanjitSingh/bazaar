from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from wholesale.models import Book, Brand, Piece, ClothType, PieceImage
from rest_framework import viewsets
from frontend.serializers import UserSerializer, GroupSerializer, BookSerializer, BrandSerializer, PieceSerializer, \
    ClothTypeSerializer, PieceImageSerializer
from frontend.models import Slider, Scroller
from django.db.models import Count
from django.db.models import Q


class PageView:
    def __init__(self):
        pass

    def init(self):
        self.data = {}
        brands = Brand.objects.all()
        self.data["brands"] = Brand.objects.all()
        self.data["clothtypes"] = ClothType.objects.all()
        self.data["piecesCountList"] = [["1", "1-5"], ["2", "6-10"], ["3", "11-15"], ["4", "16-20"],
                                        ["5", "More than 20"]]
        self.data['filters'] = {}

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
                brandName = request.GET.getlist("brands")
                kargs["brand__name__in"] = brandName
                self.data['filters']["brands"] = brandName

            if request.GET.get("clothtypes"):
                clothtypesName = request.GET.getlist("clothtypes")
                pieces = Piece.objects.filter(clothType__name__in=clothtypesName)
                kargs["pk__in"] = [piece.book.id for piece in pieces]
                self.data['filters']["clothtypes"] = clothtypesName

            if request.GET.get("nopieces"):
                noOfPieces = request.GET.get("nopieces")
                self.data['filters']["nopieces"] = noOfPieces

                if int(noOfPieces) in range(1, 5):
                    a = ((int(noOfPieces) - 1) * 5) + 1
                    b = a + 5
                    _books = Book.objects.annotate(num_pieces=Count('pieces')).filter(num_pieces__gte=a,
                                                                                      num_pieces__lt=b)
                    _books_ids = [book.id for book in _books]
                    kargs["pk__in"] = list(_books_ids)
                else:
                    _books = Book.objects.annotate(num_pieces=Count('pieces')).filter(num_pieces__gt=20)
                    _books_ids = [book.id for book in _books]
                    kargs["pk__in"] = list(_books_ids)

            if request.GET.get("search"):
                query = request.GET.get("search")
                brand_books = Book.objects.filter(
                    Q(brand__name__icontains=query) | Q(name__icontains=query) | Q(tags__name__icontains=query))
                brand_books_ids = [book.id for book in brand_books]
                pieces = Piece.objects.filter(
                    Q(dupattaType__name__icontains=query) | Q(clothType__name__icontains=query))
                book_ids = [piece.book.id for piece in pieces]
                book_ids.extend(brand_books_ids)
                book_ids = set(book_ids)
                kargs["pk__in"] = list(book_ids)

        books = Book.objects.filter(**kargs)

        self.data["books"] = books
        return render(request, 'wholesale/books.html', self.data)

    def contactus(self, request):
        self.init()
        return render(request, 'wholesale/contactus.html', self.data)

    def shoppingCart(self, request):
        self.init()

        return render(request, 'wholesale/shopingcart.html', self.data)

    def createOrder(self, request):
        if request.POST:
            print(request.POST)

        return JsonResponse({'message': 'done'})


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
