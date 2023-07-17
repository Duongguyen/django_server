from django.shortcuts import render, redirect

from app.form_event import IntroEventForm
from app.models_event import IntroEvent
from app.views import loginA


def event(request):
    if request.user.is_authenticated:
        return render(request, 'event/input_event.html')
    else:
        return loginA(request)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = IntroEventForm(request.POST)
            print(form)
            if form.is_valid():
                form.save()
                return render(request, 'event/input_event.html', {'form': form})
        else:
            form = IntroEventForm()
        return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')
            try:
                events = IntroEvent.objects.filter(id__in=delete_id)
                events.delete()
            except IntroEvent.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                events = IntroEvent.objects.get(id=edit_id)
                return render(request, 'event/update_event.html', {'events': events,
                                                                   "id": edit_id})

            except IntroEvent.DoesNotExist:
                pass

        events = IntroEvent.objects.all()

        return render(request, 'event/tables_event.html', {'events': events})

    return render(request, 'event/tables_event.html', {'events': None})


def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        intro = request.POST.get('intro')
        dates = request.POST.get('dates')
        address = request.POST.get('address')
        times = request.POST.get('times')
        events = IntroEvent(
            name=name,
            intro=intro,
            dates=dates,
            address=address,
            times=times,
        )
        events.save()
        return redirect('list_event')
    return render(request, 'app/base.html')
