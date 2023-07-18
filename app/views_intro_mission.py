from django.shortcuts import render, redirect

from app.form_intro import IntroMissionForm
from app.models_intro import IntroMission
from app.views import loginA


def mission(request):
    if request.user.is_authenticated:
        return render(request, 'intro/input_mission.html')
    else:
        return loginA(request)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = IntroMissionForm(request.POST)
            print(form)
            if form.is_valid():
                missions = form.save(commit=False)
                missions.image = request.FILES['image']
                missions.save()
                return render(request, 'intro/input_mission.html', {'form': form})
        else:
            form = IntroMissionForm()
        return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                missions = IntroMission.objects.filter(id__in=delete_id)
                missions.delete()
            except IntroMission.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                missions = IntroMission.objects.get(id=edit_id)
                print(missions.description)
                return render(request, 'intro/update_mission.html', {'missions': missions,
                                                                     "id": edit_id})

            except IntroMission.DoesNotExist:
                pass

        missions = IntroMission.objects.all()
        print(missions.JSON)
        return render(request, 'intro/tables_mission.html', {'missions': missions})

    return render(request, 'intro/tables_mission.html', {'missions': None})


def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.POST.get('image')
        missions = IntroMission(
            title=title,
            id=id,
            description=description,
            image=image,
        )
        missions.image = request.FILES['image']
        missions.save()
        return redirect('list_mission')
    return render(request, 'app/base.html')
