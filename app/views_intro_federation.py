from django.shortcuts import render, redirect

from app.form_intro import IntroFederationForm
from app.models_intro import IntroFederation
from app.views import loginA


def federation(request):
    if request.user.is_authenticated:
        return render(request, 'intro/input_federation.html')
    else:
        return loginA(request)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = IntroFederationForm(request.POST)
            print(form)
            if form.is_valid():
                federations = form.save(commit=False)
                federations.image = request.FILES['image']
                federations.save()
                return render(request, 'intro/input_federation.html', {'form': form})
        else:
            form = IntroFederationForm()
        return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                federations = IntroFederation.objects.filter(id__in=delete_id)
                federations.delete()
            except IntroFederation.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                federations = IntroFederation.objects.get(id=edit_id)
                print(federations.description)
                return render(request, 'intro/update_federation.html', {'federations': federations,
                                                                        "id": edit_id})

            except IntroFederation.DoesNotExist:
                pass

        federations = IntroFederation.objects.all()

        return render(request, 'intro/tables_federation.html', {'federations': federations})

    return render(request, 'intro/tables_federation.html', {'federations': None})


def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.POST.get('image')
        federations = IntroFederation(
            title=title,
            id=id,
            description=description,
            image=image,
        )
        federations.image = request.FILES['image']
        federations.save()
        return redirect('list_federation')
    return render(request, 'app/base.html')
