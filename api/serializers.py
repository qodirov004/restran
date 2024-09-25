from rest_framework import serializers
from blog.models import (
    BannerStage, ServiceStar, AboutStage, Contact, Comment, 
    UserProfile, TeamStage, Category, MenuItem, CartItem, Orders
)

class BannerStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerStage
        fields = '__all__'

class ServiceStarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceStar
        fields = '__all__'

class AboutStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutStage
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class TeamStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamStage
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CarttSerializer(serializers.ModelSerializer) :
    model = CartItem
    fields = ['id', 'user', 'item', 'quantity', 'price', 'total_price']

class OrdersSerializer(serializers.ModelSerializer):
    model = Orders
    field = '__all__'
    
