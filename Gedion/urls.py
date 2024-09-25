from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import HomePage, ContactPage, MenuPage, ServecePage, TestimonialPage, LogoutFunk, LoginPage, ItemDetailView, cart, TeamDetailPage,  order_view, delete_order, admin_page, clear_cart, remove_from_cart, delete_booking

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path

schema_view = get_schema_view(
   openapi.Info(
      title="Sizning API'niz nomi",
      default_version='v1',
      description="API tavsifi bu yerda",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="support@example.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage, name="home"),
    path('contact/', ContactPage, name='contact'),
    path('menu/', MenuPage, name='menu'),
    path('item/<int:item_id>/', ItemDetailView, name='item_detail'),
    path('service/', ServecePage, name='service'),
    path('team/<int:id>/', TeamDetailPage, name='team-page'),
    path('testimonial/', TestimonialPage, name='testimonial'),
    path('login/', LoginPage, name='login'),
    path('logout/', LogoutFunk, name="logout"),
    path('cart/', cart, name='cart'), 
    path('order/', order_view, name='order'),
    path('clear-cart/', clear_cart, name='clear_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
    path('api/' , include('api.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin_page/', admin_page, name='admin_page'),
    path('delete_order/<int:pk>/', delete_order, name='delete_order'),
    path('delete_booking/<int:pk>/', delete_booking, name='delete_booking'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)