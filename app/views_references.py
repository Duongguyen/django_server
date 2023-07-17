import os

from django.shortcuts import render, redirect

from app.form_library import LibraryReferencesForm
from app.models_library import LibraryReferences
from app.views import loginA
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes


def reference(request):
    if request.user.is_authenticated:
        return render(request, 'library/input_references.html')
    else:
        return loginA(request)


def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = LibraryReferencesForm(request.POST)
            if form.is_valid():
                references = form.save(commit=False)
                references.uploaded_file = request.FILES['uploaded_file']
                references.save()
                return render(request, 'library/input_references.html', {'form': form})
        else:
            form = LibraryReferencesForm()
        return render(request, 'app/base.html', {'form': form})


def list(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            delete_id = request.POST.getlist('delete_id')

            try:
                references = LibraryReferences.objects.filter(id__in=delete_id)
                references.delete()
            except LibraryReferences.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                references = LibraryReferences.objects.get(id=edit_id)
                return render(request, 'library/update_references.html', {'references': references,
                                                                          "id": edit_id})

            except LibraryReferences.DoesNotExist:
                pass

        if request.method == 'POST' and 'download_id' in request.POST:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            download_id = request.POST['download_id']
            print(download_id)
            print("x")
            filepath = base_dir + '/app/static/images/' + download_id
            thefile = filepath
            filename = os.path.basename(thefile)
            chunk_size = 8192
            reponse = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'), chunk_size),
                                            content_type=mimetypes.guess_type(thefile)[0])
            reponse['Content-Length'] = os.path.getsize(thefile)
            reponse['Content-Disposition'] = "Attachment;filename=%s" % filename
            return reponse

        references = LibraryReferences.objects.all()

        return render(request, 'library/tables_references.html', {'references': references})

    return render(request, 'library/tables_references.html', {'references': None})


def update(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        create_at = request.POST.get('create_at')
        tag = request.POST.get('tag')
        uploaded_file = request.POST.get('uploaded_file')
        references = LibraryReferences(
            id=id,
            name=name,
            create_at=create_at,
            tag=tag,
            uploaded_file=uploaded_file,
        )
        references.uploaded_file = request.FILES['image']
        references.save()
        return redirect('list_references')
    return render(request, 'app/base.html')
