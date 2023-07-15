from django.shortcuts import render, redirect

from app.form import CustomerForm, BlogForm
from app.models import Blog, CategoryBlog
from app.views import loginA


def save_blog(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            if form.is_valid():
                blogs = form.save(commit=False)
                blogs.image = request.FILES['image']
                blogs.save()  # Lưu dữ liệu từ form vào bảng Blog
                return render(request, 'app/input_blog.html', {'form': form})
        else:
            form = CustomerForm()
        return render(request, 'app/base.html', {'form': form})


def blog(request):
    if request.user.is_authenticated:
        return render(request, 'app/input_blog.html')
    else:
        return loginA(request)


def tables(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and 'delete_id' in request.POST:
            # Lấy id của dữ liệu cần xóa từ request.POST
            delete_id = request.POST.getlist('delete_id')

            try:
                blogs = Blog.objects.filter(id__in=delete_id)
                blogs.delete()
            except Blog.DoesNotExist:
                pass

        if request.method == 'POST' and 'edit_id' in request.POST:
            edit_id = request.POST['edit_id']
            try:
                blogs = Blog.objects.get(id=edit_id)
                print(blogs.description)
                return render(request, 'app/update_blog.html', {'blogs': blogs,
                                                                "id": edit_id})

            except Blog.DoesNotExist:
                pass

        blogs = Blog.objects.all()
        return render(request, 'app/tables_blog.html', {'blogs': blogs})

    return render(request, 'app/tables_blog.html', {'blogs': None})


def category_blog(request):
    categories = CategoryBlog.objects.filter(is_sub=False)
    active_category = request.GET.get('category', '')
    if active_category:
        products = Blog.objects.filter(category__slug=active_category)
    context = {'categories': categories, 'products': products, 'active_category': active_category}
    return render(request, 'app/category.html', context)


def update_blog(request, id):
    if request.method == 'POST':
        stt = request.POST.get('stt')
        category = request.POST.get('category')
        title = request.POST.get('title')
        image = request.POST.get('image')
        source = request.POST.get('source')
        description = request.POST.get('description')
        publication_date = request.POST.get('publication_date')
        poster = request.POST.get('poster')
        blogs = Blog(
            id=id,
            stt=stt,
            category=category,
            title=title,
            image=image,
            source=source,
            description=description,
            publication_date=publication_date,
            poster=poster,
        )
        blogs.image = request.FILES['image']
        blogs.save()
        return redirect('list_blog')
    return render(request, 'app/base.html')
