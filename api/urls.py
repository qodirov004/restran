from django.urls import path
from .views import (
    BannerView, ServieView, AboutView, ContactView,
    CommentView, UserProfileListView, UserView,
    TeamView, CategoryListView, CategoryView,
    MenuItemListView, MenuViews, CartItemListView, CartView, OrdersView
)

urlpatterns = [
    path('', AboutView.as_view(), name='about-stage-list'),
    path('banner-list/',BannerView.as_view(), name = 'banner-list'),
    path('service-star/', ServieView.as_view(), name = 'service-star'),
    path('contact/', ContactView.as_view(), name = 'contact-page-list'),
    path('comment/', CommentView.as_view(), name = 'comment-list-view'),
    path('user-profile/<int:pk>/', UserProfileListView.as_view(), name='user-profile-list'),
    path('user-profile/', UserView.as_view(), name = 'user-list'),
    path('team-stage/', TeamView.as_view(), name = 'team-list'),
    path('category/<int:pk>/', CategoryListView.as_view(), name='category-list'),
    path('category/', CategoryView.as_view(), name = 'category'),
    path('menu-item/<int:pk>', MenuItemListView.as_view(), name='menu-item-list'),
    path('menu-item/', MenuViews.as_view(), name='menu-list'),
    path('cart-item/<int:pk>/', CartItemListView.as_view(), name='cart-item-list'),
    path('cart-item/', CartView.as_view(), name = 'cart-list'),
    path('order-view/', OrdersView.as_view(), name='order-list')
]
