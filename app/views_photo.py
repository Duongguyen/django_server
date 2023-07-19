from django.shortcuts import render, redirect

from .form import PhotoForm
from .models import Photo
from .views import loginA


def photo(request):
    if request.user.is_authenticated:
        return render(request, 'app/input_photo.html')
    else:
        return loginA(request)


def save_photo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PhotoForm(request.POST)
            print(form)
            if form.is_valid():
                photos = form.save(commit=False)
                photos.image = request.FILES['image']
                photos.save()
                return render(request, 'app/input_photo.html', {'form': form})
        else:
            form = PhotoForm()
        return render(request, 'app/base.html', {'form': form})


def table(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                photos = Photo.objects.filter(id__in=delete_id)
                photos.delete()
            except Photo.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                photos = Photo.objects.get(id=edit_id)
                print(photos.description)
                return render(request, 'app/update_photo.html', {'photos': photos,
                                                                 "id": edit_id})

            except Photo.DoesNotExist:
                pass

        photos = Photo.objects.all()

        return render(request, 'app/tables_photo.html', {'photos': photos})

    return render(request, 'app/tables_photo.html', {'photos': None})


def update_photo(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        description = request.POST.get('description')
        image = request.POST.get('image')
        photo = Photo(id=id,
                      name=name,
                      category=category,
                      description=description,
                      image=image,
                      )
        photo.image = request.FILES['image']
        photo.save()
        return redirect('list_photo')
    return render(request, 'app/base.html')
