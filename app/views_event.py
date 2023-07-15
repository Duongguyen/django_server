from django.shortcuts import render, redirect

from app.form_event import EventsForm
from app.models_event import Events
from app.views import loginA


def event(request):
    if request.user.is_authenticated:
        return render(request, 'event/input_event.html')
    else:
        return loginA(request)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EventsForm(request.POST)
            print(form)
            if form.is_valid():
                form.save()
                return render(request, 'event/input_event.html', {'form': form})
        else:
            form = EventsForm()
        return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                events = Events.objects.filter(id__in=delete_id)
                events.delete()
            except Events.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                events = Events.objects.get(id=edit_id)
                print(events.description)
                return render(request, 'event/update_event.html', {'events': events,
                                                                   "id": edit_id})

            except Events.DoesNotExist:
                pass

        events = Events.objects.all()

        return render(request, 'event/tables_event.html', {'events': events})

    return render(request, 'event/tables_event.html', {'events': None})


def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        intro = request.POST.get('intro')
        publication_date = request.POST.get('publication_date')
        address = request.POST.get('address')
        publication_time = request.POST.get('publication_time')
        events = Events(
            name=name,
            intro=intro,
            publication_date=publication_date,
            address=address,
            publication_time=publication_time,
        )
        events.save()
        return redirect('list_event')
    return render(request, 'app/base.html')
