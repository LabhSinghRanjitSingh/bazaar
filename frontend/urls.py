from django.conf.urls import url, include
from django.views.generic import TemplateView
from rest_framework import routers
from frontend import views




router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'brands', views.BrandViewSet)
router.register(r'pieces', views.PieceViewSet)
router.register(r'clothTypes', views.ClothTypeViewSet)
router.register(r'pieceImages', views.PieceImageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

pageView = views.PageView()

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$',pageView.home,name='home'),
    url(r'^api/books/(?P<id>[0-9]*)/views$',pageView.book,name='book'),
    url(r'^books/$',pageView.books,name='books'),
    url(r'^contactus/$',pageView.contactus,name='contactus'),
    url(r'^shopingcart/$',pageView.shoppingCart,name='shopingCart'),
]
