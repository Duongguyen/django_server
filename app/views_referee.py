from django.shortcuts import render, redirect

from app.form_profile import RefereeForm
from app.models_profile import Referee
from app.views import loginA


def referee(request):
    if request.user.is_authenticated:
        return render(request, 'profile/input_referee.html')
    else:
        return loginA(request)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RefereeForm(request.POST)
            print(form)
            if form.is_valid():
                referees = form.save(commit=False)
                referees.image = request.FILES['image']
                referees.save()
                return render(request, 'profile/input_referee.html', {'form': form})
        else:
            form = RefereeForm()
        return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                referees = Referee.objects.filter(id__in=delete_id)
                referees.delete()
            except Referee.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                referees = Referee.objects.get(id=edit_id)
                return render(request, 'profile/update_referee.html', {'referees': referees,
                                                                       "id": edit_id})

            except Referee.DoesNotExist:
                pass

        referees = Referee.objects.all()

        return render(request, 'profile/tables_referee.html', {'referees': referees})

    return render(request, 'profile/tables_referee.html', {'referees': None})


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
        referees = Referee(
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
        referees.image = request.FILES['image']
        referees.save()
        return redirect('list_referee')
    return render(request, 'app/base.html')
