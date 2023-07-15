from django.contrib import messages
from django.shortcuts import render, redirect

from .form import BlogForm, CreateUserForm, PhotoForm, UserUpdateForm, CustomerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
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
    form = UserUpdateForm(instance=request.user)  # Khá»Ÿi táº¡o form vá»›i instance lÃ  request.user
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



