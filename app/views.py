from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .form import BlogForm, CreateUserForm, PhotoForm
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout


def save_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)  # Lưu form nhưng chưa commit vào cơ sở dữ liệu
            blog.image = request.FILES['image']
            blog.save()  # Lưu dữ liệu từ form vào bảng Blog
            return render(request, 'app/input_blog.html', {'form': form})  # Chuyển hướng đến trang thành công sau khi lưu dữ liệu
    else:
        form = BlogForm()
    return render(request, 'app/base.html', {'form': form})


def save_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            photos = form.save(commit=False)  # Lưu form nhưng chưa commit vào cơ sở dữ liệu
            photos.image = request.FILES['image']
            photos.save()
            # Lưu dữ liệu từ form vào bảng Blog
            return render(request, 'app/input_photo.html', {'form': form})  # Chuyển hướng đến trang thành công sau khi lưu dữ liệu
    else:
        form = BlogForm()
    return render(request, 'app/base.html', {'form': form})


def blog(request):
    return render(request, 'app/input_blog.html')


def base(request):
    return render(request, 'app/base.html')


def photo(request):
    return render(request, 'app/input_photo.html')


def table(request):
    if request.user.is_authenticated:
        photos = Photo.objects.all()
        if photos:
            return render(request, 'app/tables_photo.html', {'photos': photos})
    return render(request, 'app/tables_photo.html', {'photos': photos})


def tables(request):
    if request.user.is_authenticated:
        photos = Blog.objects.all()
        if photos:
            return render(request, 'app/tables_blog.html', {'photos': photos})
    return render(request, 'app/tables_blog.html', {'photos': photos})


def category_blog(request):
    categories = CategoryBlog.objects.filter(is_sub=False)
    active_category = request.GET.get('category', '')
    if active_category:
        products = Blog.objects.filter(category__slug=active_category)
    context = {'categories': categories, 'products': products, 'active_category': active_category}
    return render(request, 'app/category.html', context)


# def search(request):
#     if request.method == "POST":
#         searched = request.POST["searched"]
#         keys = Product.objects.filter(name__contains=searched)
#
#     if request.user.is_authenticated:
#         customer = request.user
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#     else:
#         items = []
#         order = {'get_cart_items': 0, 'get_cart_total': 0}
#         cartItems = order['get_cart_items']
#     products = Product.objects.all()
#     return render(request, 'app/search.html', {"searched": searched,
#                                                "keys": keys,
#                                                'products': products,
#                                                'cartItems': cartItems}
#                   )


def register(request):
    form = CreateUserForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'app/register.html', context)


def loginA(request):
    if request.user.is_authenticated:
        return render(request, 'app/base.html')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'app/base.html')
        else:
            messages.info(request, 'user or pass not correct!')
    context = {}
    return render(request, 'app/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')


# def home(request):
#     if request.user.is_authenticated:
#         customer = request.user
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#         user_not_login = "hidden"
#         user_login = "show"
#     else:
#         items = []
#         order = {'get_cart_items': 0, 'get_cart_total': 0}
#         cartItems = order['get_cart_items']
#         user_not_login = "show"
#         user_login = "hidden"
#     products = Product.objects.all()
#     categories = Category.objects.filter(is_sub=False)
#     context = {'categories': categories, 'products': products, 'cartItems': cartItems, 'user_not_login': user_not_login,
#                'user_login': user_login}
#     return render(request, 'app/home.html', context)
#
#
# def cart(request):
#     global order
#     if request.user.is_authenticated:
#         customer = request.user
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#         user_not_login = "hidden"
#         user_login = "show"
#     else:
#         items = []
#         order = {'get_cart_items': 0, 'get_cart_total': 0}
#         cartItems = order['get_cart_items']
#         user_not_login = "show"
#         user_login = "hidden"
#     categories = Category.objects.filter(is_sub=False)
#     context = {'categories': categories,
#                'items': items,
#                'order': order, 'cartItems': cartItems,
#                'user_not_login': user_not_login,
#                'user_login': user_login}
#     return render(request, 'app/cart.html', context)
#
#
# def checkout(request):
#     global order
#     if request.user.is_authenticated:
#         customer = request.user
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#         user_not_login = "show"
#         user_login = "hidden"
#     else:
#         items = []
#         order = {'get_cart_items': 0, 'get_cart_total': 0}
#         cartItems = order.get_cart_items
#         user_not_login = "hidden"
#         user_login = "show"
#     categories = Category.objects.filter(is_sub=False)
#     context = {'categories': categories,
#                'items': items,
#                'order': order, 'cartItems': cartItems,
#                'user_not_login': user_not_login,
#                'user_login': user_login}
#     return render(request, 'app/checkout.html', context)
#
#
# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     customer = request.user
#     product = Product.objects.get(id=productId)
#     order, created = Order.objects.get_or_create(customer=customer, complete=False)
#     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
#     if action == 'add':
#         orderItem.quantity += 1
#     elif action == 'remove':
#         orderItem.quantity -= 1
#     orderItem.save()
#     if orderItem.quantity <= 0:
#         orderItem.delete()
#     return JsonResponse('added', safe=False)
# Create your views here.




