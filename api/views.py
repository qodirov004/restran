from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import BasePermission
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from blog.models import (
    BannerStage, ServiceStar, AboutStage, Contact, Comment, 
    UserProfile, TeamStage, Category, MenuItem, CartItem, Orders
)
from .serializers import (
    BannerStageSerializer, ServiceStarSerializer, AboutStageSerializer, 
    ContactSerializer, CommentSerializer, UserProfileSerializer, 
    TeamStageSerializer, CategorySerializer, MenuItemSerializer, 
    CartItemSerializer, OrdersSerializer
)

class BannerView(ListAPIView) :
    queryset = BannerStage.objects.all()
    serializer_class = BannerStageSerializer

class ServieView(ListAPIView) :
    queryset = ServiceStar.objects.all()
    serializer_class = ServiceStarSerializer 

class AboutView(ListAPIView) :
    queryset = AboutStage.objects.all()
    serializer_class = AboutStageSerializer

class ContactView(ListAPIView) :
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class CommentView(ListAPIView) :
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class UserView(ListAPIView) :
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileListView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class TeamView(ListAPIView) :
    queryset = TeamStage.objects.all() 
    serializer_class = TeamStageSerializer

class CategoryView(ListAPIView) :
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MenuPagination(PageNumberPagination) :
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 6

class MenuViews(ListAPIView) :
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    pagination_class = MenuPagination

class MenuItemListView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class CartView(ListAPIView) :
    queryset = CartItem.objects.all() 
    serializer_class = CartItemSerializer

class CartItemListView(RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class OrdersView(ListAPIView) :
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

