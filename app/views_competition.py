from django.shortcuts import render, redirect

from app.form_competition import CompetitionForm
from app.models_competition import Competition
from app.views import loginA


# def competition(request):
#     if request.user.is_authenticated:
#         return render(request, 'group/input_group.html')
#     else:
#         return loginA(request)


# def create(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = CompetitionForm(request.POST)
#             if form.is_valid():
#                 competitions = form.save(commit=False)
#                 competitions.image = request.FILES['image']
#                 competitions.save()
#                 return render(request, 'competition/tables_competition.html', {'form': form})
#         else:
#             form = CompetitionForm()
#         return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                competitions = Competition.objects.filter(id__in=delete_id)
                competitions.delete()
            except Competition.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                competitions = Competition.objects.get(id=edit_id)
                return render(request, 'competition/update_competition.html', {'competitions': competitions,
                                                                               "id": edit_id})

            except Competition.DoesNotExist:
                pass

        competitions = Competition.objects.all()
        print("X")
        return render(request, 'competition/tables_competition.html', {'competitions': competitions})

    return render(request, 'competition/tables_competition.html', {'competitions': None})


def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        intro = request.POST.get('intro')
        image = request.POST.get('image')
        law = request.POST.get('law')
        statute = request.POST.get('statute')
        competitions = Competition(
            id=id,
            name=name,
            intro=intro,
            image=image,
            law=law,
            statute=statute
        )
        competitions.image = request.FILES['image']
        competitions.save()
        return redirect('list_competition')
    return render(request, 'app/base.html')
