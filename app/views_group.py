from django.shortcuts import render, redirect

from app.form_group import GroupForm
from app.models_group import Group
from app.views import loginA


def group(request):
    if request.user.is_authenticated:
        return render(request, 'group/input_group.html')
    else:
        return loginA(request)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = GroupForm(request.POST)
            print(form)
            if form.is_valid():
                groups = form.save(commit=False)
                groups.image = request.FILES['image']
                groups.save()
                return render(request, 'group/input_group.html', {'form': form})
        else:
            form = GroupForm()
        return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                groups = Group.objects.filter(id__in=delete_id)
                groups.delete()
            except Group.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                groups = Group.objects.get(id=edit_id)
                print(groups.description)
                return render(request, 'group/update_group.html', {'groups': groups,
                                                                   "id": edit_id})

            except Group.DoesNotExist:
                pass

        groups = Group.objects.all()

        return render(request, 'group/tables_group.html', {'groups': groups})

    return render(request, 'group/tables_group.html', {'groups': None})


def update(request, id):
    if request.method == 'POST':
        name_group = request.POST.get('name_group')
        subject = request.POST.get('subject')
        image = request.POST.get('image')
        year = request.POST.get('year')
        social_network = request.POST.get('social_network')
        intro = request.POST.get('intro')
        achier = request.POST.get('achier')
        groups = Group(
            name_group=name_group,
            subject=subject,
            image=image,
            year=year,
            social_network=social_network,
            intro=intro,
            achier=achier,
        )
        groups.image = request.FILES['image']
        groups.save()
        return redirect('list_group')
    return render(request, 'app/base.html')
