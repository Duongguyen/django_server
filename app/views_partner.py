from django.shortcuts import render, redirect

from app.form_partner import PartnerForm
from app.models_partner import Partner
from app.views import loginA


def partner(request):
    if request.user.is_authenticated:
        return render(request, 'partner/input_partner.html')
    else:
        return loginA(request)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PartnerForm(request.POST)
            print(form)
            if form.is_valid():
                partners = form.save(commit=False)
                partners.image = request.FILES['image']
                partners.save()
                return render(request, 'partner/input_partner.html', {'form': form})
        else:
            form = PartnerForm()
        return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                partners = Partner.objects.filter(id__in=delete_id)
                partners.delete()
            except Partner.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                partners = Partner.objects.get(id=edit_id)
                return render(request, 'partner/update_partner.html', {'partners': partners,
                                                                       "id": edit_id})

            except Partner.DoesNotExist:
                pass

        partners = Partner.objects.all()

        return render(request, 'partner/tables_partner.html', {'partners': partners})

    return render(request, 'partner/tables_partner.html', {'partners': None})


def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        image = request.POST.get('image')
        phone = request.POST.get('phone')
        social_network = request.POST.get('social_network')
        email = request.POST.get('email')
        partners = Partner(
            id=id,
            name=name,
            address=address,
            image=image,
            phone=phone,
            social_network=social_network,
            email=email,
        )
        partners.image = request.FILES['image']
        partners.save()
        return redirect('list_partner')
    return render(request, 'app/base.html')



