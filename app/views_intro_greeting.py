from django.shortcuts import render, redirect

from app.form_intro import GreetingsForm
from app.models_intro import Greeting
from app.views import loginA


def greeting(request):
    if request.user.is_authenticated:
        return render(request, 'intro/input_greeting.html')
    else:
        return loginA(request)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = GreetingsForm(request.POST)
            print(form)
            if form.is_valid():
                greetings = form.save(commit=False)
                greetings.image = request.FILES['image']
                greetings.save()
                return render(request, 'intro/input_greeting.html', {'form': form})
        else:
            form = GreetingsForm()
        return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                greetings = Greeting.objects.filter(id__in=delete_id)
                greetings.delete()
            except Greeting.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                greetings = Greeting.objects.get(id=edit_id)
                print(greetings.description)
                return render(request, 'intro/update_greeting.html', {'greetings': greetings,
                                                                      "id": edit_id})

            except Greeting.DoesNotExist:
                pass

        greetings = Greeting.objects.all()

        return render(request, 'intro/tables_greeting.html', {'greetings': greetings})

    return render(request, 'intro/tables_greeting.html', {'greetings': None})


def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        stt = request.POST.get('stt')
        description = request.POST.get('description')
        image = request.POST.get('image')
        greetings = Greeting(
            title=title,
            id=id,
            stt=stt,
            description=description,
            image=image,
        )
        greetings.image = request.FILES['image']
        greetings.save()
        return redirect('list_greeting')
    return render(request, 'app/base.html')
