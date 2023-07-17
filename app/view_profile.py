from django.shortcuts import render, redirect

from app.form_profile import AthleteForm
from app.models_profile import Athlete
from app.views import loginA


def athlete(request):
    if request.user.is_authenticated:
        return render(request, 'profile/input_athlete.html')
    else:
        return loginA(request)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AthleteForm(request.POST)
            print(form)
            if form.is_valid():
                print('y')
                athletes = form.save(commit=False)
                athletes.image = request.FILES['image']
                athletes.save()
                return render(request, 'profile/input_athlete.html', {'form': form})
        else:
            form = AthleteForm()
        return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                athletes = Athlete.objects.filter(id__in=delete_id)
                athletes.delete()
            except Athlete.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                athletes = Athlete.objects.get(id=edit_id)
                return render(request, 'profile/update_athlete.html', {'athletes': athletes,
                                                                       "id": edit_id})

            except Athlete.DoesNotExist:
                pass

        athletes = Athlete.objects.all()

        return render(request, 'profile/tables_athlete.html', {'athletes': athletes})

    return render(request, 'profile/tables_athlete.html', {'athletes': None})


def update(request, id):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        object = request.POST.get('object')
        image = request.POST.get('image')
        sex = request.POST.get('sex')
        social_network = request.POST.get('social_network')
        date_of_birth = request.POST.get('date_of_birth')
        achier = request.POST.get('achier')
        home_live = request.POST.get('home_live')
        career = request.POST.get('career')
        athletes = Athlete(
            id=id,
            fullname=fullname,
            object=object,
            image=image,
            sex=sex,
            social_network=social_network,
            date_of_birth=date_of_birth,
            achier=achier,
            home_live=home_live,
            career=career,
        )
        athletes.image = request.FILES['image']
        athletes.save()
        return redirect('list_athlete')
    return render(request, 'app/base.html')