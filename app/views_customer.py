from django.shortcuts import render, redirect
from .form import BlogForm, CreateUserForm, PhotoForm, UserUpdateForm, CustomerForm
from .models import Customer
from .views import loginA


def save_customer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                customers = form.save(commit=False)
                customers.save()
                return render(request, 'app/input_customer.html', {'form': form})
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


def update_customer(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cus = Customer(id=id,
                       name=name,
                       email=email,
                       phone=phone
                       )
        cus.save()
        return redirect('list')
    return render(request, 'app/base.html')


def customer(request):
    if request.user.is_authenticated:
        return render(request, 'app/input_customer.html')
    else:
        return loginA(request)