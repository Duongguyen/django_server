from django.shortcuts import render, redirect

from .form_contact import ContactForm
from .models_contact import Contact
from .views import loginA


def contact(request):
    if request.user.is_authenticated:
        return render(request, 'contact/input_contact.html')
    else:
        return loginA(request)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'contact/input_contact.html', {'form': form})
        else:
            form = ContactForm()
        return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')
            try:
                contacts = Contact.objects.filter(id__in=delete_id)
                contacts.delete()
            except Contact.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                contacts = Contact.objects.get(id=edit_id)
                return render(request, 'contact/update_contact.html', {'contacts': contacts,
                                                                       "id": edit_id})

            except Contact.DoesNotExist:
                pass

        contacts = Contact.objects.all()

        return render(request, 'contact/tables_contact.html', {'contacts': contacts})

    return render(request, 'contact/tables_contact.html', {'contacts': None})


def update(request, id):
    if request.method == 'POST':
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        contacts = Contact(
            id=id,
            email=email,
            address=address,
            phone=phone,
        )
        contacts.save()
        return redirect('list_contact')
    return render(request, 'app/base.html')

