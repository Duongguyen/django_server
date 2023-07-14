from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .form import BlogForm, CreateUserForm, PhotoForm, UserUpdateForm, CustomerForm
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def save_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            if form.is_valid():
                blogs = form.save(commit=False)
                blogs.image = request.FILES['image']
                blogs.save()  # Lưu dữ liệu từ form vào bảng Blog
                return render(request, 'app/customer.html', {'form': form})
        else:
            form = CustomerForm()
        return render(request, 'app/base.html', {'form': form})


def save_photo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PhotoForm(request.POST)
            if form.is_valid():
                blog = form.save(commit=False)
                blog.image = request.FILES['image']
                blog.save()
                return render(request, 'app/input_photo.html', {'form': form})
        else:
            form = PhotoForm()
        return render(request, 'app/base.html', {'form': form})


def save_customer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                customers = form.save(commit=False)
                customers.save()
                return render(request, 'app/customer.html', {'form': form})
        else:
            form = PhotoForm()
        return render(request, 'app/base.html', {'form': form})


def customer_tables(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                customers = Customer.objects.filter(id__in=delete_id)
                customers.delete()
            except Customer.DoesNotExist:
                pass
        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                customers = Customer.objects.get(id=edit_id)

                return render(request, 'app/update_customer.html', {'customers': customers,
                                                                    "id": edit_id})

            except Customer.DoesNotExist:
                pass

        customers = Customer.objects.all()

        return render(request, 'app/tables_customer.html', {'customers': customers})

    return render(request, 'app/tables_customer.html', {'customers': None})


# //EDIT CUSSTOMER
def edit_customer(request):
    cus = Customer.objects.all()

    context = {
        'cus': cus,
    }
    return render(request, 'app/update_customer.html', context)


def update_customer(request, id):

    if request.method == 'POST':
        print("y")
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cus = Customer(id=id,
                       name=name,
                       email=email,
                       phone=phone
                       )
        cus.save()
        return redirect('push')
    return render(request, 'app/base.html')


def blog(request):
    if request.user.is_authenticated:
        return render(request, 'app/input_blog.html')
    else:
        return loginA(request)


def base(request):
    if request.user.is_authenticated:
        user_not_login = "hidden"
        user_login = "show"
    else:
        user_not_login = "show"
        user_login = "hidden"
    context = {'user_not_login': user_not_login,
               'user_login': user_login}

    return render(request, 'app/base.html', context)


def photo(request):
    if request.user.is_authenticated:
        return render(request, 'app/input_photo.html')
    else:
        return loginA(request)


def customer(request):
    if request.user.is_authenticated:
        return render(request, 'app/customer.html')
    else:
        return loginA(request)


def table(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                photo = Photo.objects.filter(id__in=delete_id)
                photo.delete()
            except Photo.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                photo = Photo.objects.get(id=edit_id)
                if request.method == 'POST':
                    photo = Photo.objects.get(id=edit_id)
                    photo.delete()
                    save_blog(request)
                    return redirect('photo')

                return render(request, 'app/input_photo.html', {'photo': photo})
            except Photo.DoesNotExist:
                pass

        photos = Photo.objects.all()

        return render(request, 'app/tables_photo.html', {'photos': photos})

    return render(request, 'app/tables_photo.html', {'photos': None})


def tables(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            # Lấy id của dữ liệu cần xóa từ request.POST
            delete_id = request.POST.getlist('delete_id')

            try:
                photo = Blog.objects.filter(id__in=delete_id)
                photo.delete()
            except Blog.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                photo = Blog.objects.get(id=edit_id)
                if request.method == 'POST':
                    photo = Blog.objects.get(id=edit_id)
                    stt = request.POST.get('stt')
                    category = request.POST.get('category')
                    title = request.POST.get('title')
                    image = request.POST.get('image')
                    source = request.POST.get('source')
                    description = request.POST.get('description')
                    publication_date = request.POST.get('publication_date')
                    name = request.POST.get('name')
                    save_blog(request)
                    return redirect('input')

                return render(request, 'app/input_blog.html', {'photo': photo})
            except Blog.DoesNotExist:
                pass

        photos = Blog.objects.all()

        return render(request, 'app/tables_blog.html', {'photos': photos})

    return render(request, 'app/tables_blog.html', {'photos': None})


def users(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')
            print(delete_id)
            try:
                user = User.objects.filter(id__in=delete_id)
                user.delete()
            except User.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            print(request.POST)
            try:
                edit_id = request.POST['edit_id']
                photos = User.objects.get(id=edit_id)
                form = UserUpdateForm(request.POST, instance=request.user)
                print(form)
                return render(request, 'app/edit_user.html', {'form': form,
                                                              'photos': photos})
            except User.DoesNotExist:
                pass

        users = User.objects.all()
        return render(request, 'app/user.html', {'users': users})
    return render(request, 'app/user.html', {'users': None})


def update_user(request):
    form = UserUpdateForm(instance=request.user)  # Khởi tạo form với instance là request.user
    value = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form': form}
            user = User.objects.filter(username=value)
            user.delete()
            return render(request, 'app/user.html', context)
    context = {'form': form}
    return render(request, 'app/user.html', context)


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'app/register.html', context)


def category_blog(request):
    categories = CategoryBlog.objects.filter(is_sub=False)
    active_category = request.GET.get('category', '')
    if active_category:
        products = Blog.objects.filter(category__slug=active_category)
    context = {'categories': categories, 'products': products, 'active_category': active_category}
    return render(request, 'app/category.html', context)


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
