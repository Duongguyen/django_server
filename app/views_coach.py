from django.shortcuts import render, redirect

from app.form_profile import CoachForm
from app.models_profile import Coach
from app.views import loginA


def coach(request):
    if request.user.is_authenticated:
        return render(request, 'profile/input_coach.html')
    else:
        return loginA(request)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CoachForm(request.POST)
            print(form)
            if form.is_valid():
                print('y')
                coachs = form.save(commit=False)
                coachs.image = request.FILES['image']
                coachs.save()
                return render(request, 'profile/input_coach.html', {'form': form})
        else:
            form = CoachForm()
        return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                coachs = Coach.objects.filter(id__in=delete_id)
                coachs.delete()
            except Coach.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                coachs = Coach.objects.get(id=edit_id)
                return render(request, 'profile/update_coach.html', {'coachs': coachs,
                                                                     "id": edit_id})

            except Coach.DoesNotExist:
                pass

        coachs = Coach.objects.all()

        return render(request, 'profile/tables_coach.html', {'coachs': coachs})

    return render(request, 'profile/tables_coach.html', {'coachs': None})


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
        coachs = Coach(
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
        coachs.image = request.FILES['image']
        coachs.save()
        return redirect('list_coach')
    return render(request, 'app/base.html')
