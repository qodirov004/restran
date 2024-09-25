from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import BannerStage, CartItem, ServiceStar, Contact, Comment, TeamStage, Category, MenuItem, BookingStage, BookingMedia, Orders
from django.contrib import messages
from django.http import HttpResponse

def HomePage(request):
    bannerstage = BannerStage.objects.all()
    servicestar = ServiceStar.objects.all()
    categories = Category.objects.all()
    teamstage = TeamStage.objects.all()
    menuitem = MenuItem.objects.all()[:4]
    categories = Category.objects.prefetch_related('menuitem_set').all()
    video_files = BookingMedia.objects.all()
    if request.method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        datetime = request.POST.get('datetime')
        people_quantity = request.POST.get('people_quantity')
        requests = request.POST.get('requests')
        BookingStage.objects.create(name=name, email=email, datetime=datetime, people_quantity=people_quantity, requests=requests)

        return redirect('home')
    
    context = {
        'bannerstage' : bannerstage,
        'servicestar' : servicestar,
        'cotegories' : categories,
        'menuitem' : menuitem,
        'teamstage' : teamstage,
        'categories' : categories,
        'video_files' : video_files,
    }
    return render(request, 'index.html', context)

def PostList(request) :
    if request.method == 'POST' :
        comment = request.POST.get('commentpost')
        user = request.user
        if len(comment) != 0 :
            Comment.objects.create(author=user, comment=comment)
        athor = Comment.objects.select_related('author')
        print(athor)
    return reversed('contact')

def ContactPage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        
        return redirect('home')

    return render(request, 'contact.html')

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        messages.error(request, 'Savatchangiz bo\'sh. Iltimos, avval mahsulot qo\'shing.')
        return redirect('menu')  

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phoneNumber')
        address = request.POST.get('address')

        total_price = sum(item.quantity * item.item.price for item in cart_items)


        order = Orders.objects.create(
            user=request.user,
            name=name,
            phone=phone,
            address=address,
        )
        
        order.cart_items.set(cart_items)  
        order.save()

        messages.success(request, 'Buyurtma muvaffaqiyatli yuborildi!')
        return redirect('menu')

    if not cart_items.exists():
        total_price = 0
    else:
        for item in cart_items:
            item.total_price = item.quantity * item.item.price

        total_price = sum(item.total_price for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def MenuPage(request):
    menuitems = MenuItem.objects.all()
    categories = Category.objects.prefetch_related('menuitem_set').all()

    context = {
        'categories': categories,   
        'menuitem': menuitems,
    }

    return render(request, 'menu.html', context)

def create_order(request):
    cart_items = CartItem.objects.filter(user=request.user)

    

    return render(request, 'admin_page.html', {'cart_items': cart_items})

def ItemDetailView(request, item_id):
    if request.method == "POST":
        if request.user.is_authenticated:
            soni = request.POST.get("quantity")
            op = CartItem.objects.filter(user=request.user, item__id=item_id)
            
            if op.exists():
                cart_item = op.first()
                cart_item.quantity += int(soni)
                cart_item.total = cart_item.price * cart_item.quantity
                cart_item.save()
            else:
                item = MenuItem.objects.get(id=item_id)
                new_cart_item = CartItem.objects.create(
                    user=request.user,
                    item=item,
                    quantity=int(soni),
                    price=item.price, 
                )
                new_cart_item.save()

            return redirect('cart')
        else:
            return redirect('/login/')
    else:
        if request.user.is_authenticated:
            if MenuItem.objects.filter(id=item_id).exists():
                r = MenuItem.objects.get(id=item_id)
                return render(request, 'item_detail.html', {"item": r})
            else:
                return render(request, 'item_detail.html', {"item": None})
        else:
            return redirect('/')



def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect('cart')

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart')

def order_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phoneNumber')
        address = request.POST.get('address')
        CartItem.objects.filter(user=request.user).delete()
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.item.price * item.quantity for item in cart_items)

        if name and phone and address and cart_items.exists():
            # Yangi buyurtma yaratish (bu yerda Order modelini ishlatasiz)
            new_order = Orders.objects.create(
                user=request.user,
                name=name,
                phone=phone,
                address=address,
                total_price=total_price
            )

            # Savatdagi har bir elementni buyurtmaga bog'lang
            for cart_item in cart_items:
                new_order.items.add(cart_item)

            # Savatni tozalash
            CartItem.objects.filter(user=request.user).delete()
            # Muvaffaqiyatli xabar
            messages.success(request, 'Buyurtmangiz muvaffaqiyatli qabul qilindi!')
            return redirect('success') 
        context = {
            'phone' : phone,
            'adress' : address,
            'cart_items': cart_items,
            'total_price': total_price,

        }
        return redirect('success')
    return redirect('cart', context)

def delete_order(request, order_id):
    order = CartItem.objects.get(id=order_id)
    order.delete()
    return redirect('admin_page')

def admin_page(request):
    if request.user.is_superuser:
        cart_items = CartItem.objects.filter(user=request.user)
        orders = Orders.objects.all()  
        booking_table = BookingStage.objects.all()
    
        context = {
            'cart_items': cart_items,
            'orders': orders,
            'booking_table' : booking_table,
        }
        
        return render(request, 'admin_page.html', context)

    else:
        return redirect('home')

def delete_order(request, pk):
    order = get_object_or_404(Orders, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('admin_page')

def delete_booking(request, pk):
    booking = get_object_or_404(BookingStage, id=pk)
    if request.method == "POST":
        booking.delete()
        return redirect('admin_page')  # Redirect to your desired page after deletion

    return HttpResponse(status=405)  

def ServecePage(request) :
    return render(request, 'service.html')

def TeamDetailPage(request, id) :
    team = TeamStage.objects.get(id = id)
    return render(request, 'team.html', {'team' : team})

def TestimonialPage(request) :
    return render(request, 'testimonial.html')

def LoginPage(request):
    if request.method == 'POST':
        if 'login_form' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Specify the backend if there are multiple
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('login')
                
        elif 'signup_form' in request.POST:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 == password2:
                if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                    messages.error(request, 'User already exists.')
                    return redirect('login')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email)
                    user.save()
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    return redirect('home')
            else:
                messages.error(request, "Passwords don't match.")
                return redirect('login')
                
    return render(request, 'signupandlogin.html')


def LogoutFunk(request):
    logout(request)
    return redirect('home')

