from django.shortcuts import render, redirect

from app.form_intro import IntroEvolutionForm
from app.models_intro import IntroEvolution
from app.views import loginA


def evolution(request):
    if request.user.is_authenticated:
        return render(request, 'intro/input_evolution.html')
    else:
        return loginA(request)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = IntroEvolutionForm(request.POST)
            print(form)
            if form.is_valid():
                evolutions = form.save(commit=False)
                evolutions.image = request.FILES['image']
                evolutions.save()
                return render(request, 'intro/input_evolution.html', {'form': form})
        else:
            form = IntroEvolutionForm()
        return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                evolutions = IntroEvolution.objects.filter(id__in=delete_id)
                evolutions.delete()
            except IntroEvolution.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                evolutions = IntroEvolution.objects.get(id=edit_id)
                print(evolutions.description)
                return render(request, 'intro/update_evolution.html', {'evolutions': evolutions,
                                                                       "id": edit_id})

            except IntroEvolution.DoesNotExist:
                pass

        evolutions = IntroEvolution.objects.all()

        return render(request, 'intro/tables_evolution.html', {'evolutions': evolutions})

    return render(request, 'intro/tables_evolution.html', {'evolutions': None})


def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.POST.get('image')
        evolutions = IntroEvolution(
            title=title,
            id=id,
            description=description,
            image=image,
        )
        evolutions.image = request.FILES['image']
        evolutions.save()
        return redirect('list_evolution')
    return render(request, 'app/base.html')
