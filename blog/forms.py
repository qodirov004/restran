from django import forms
from .models import CartItem,BookingMedia, Orders



class AddToCartForm(forms.Form):
    class Meta:
        model= CartItem
        fields='__all__'
        
class Videos(forms.Form):
    class Meta:
        model=BookingMedia
        fields='__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['name', 'phone', 'address']
