from django.contrib import admin
from .models import *
from .models_intro import *
from .models_event import *
from .models_group import *
from .models_partner import *
# Register your models here.

admin.site.register(Blog)
admin.site.register(CategoryPhoto)
admin.site.register(CategoryBlog)
admin.site.register(Photo)
admin.site.register(Customer)

admin.site.register(Greeting)

admin.site.register(Events)

admin.site.register(Group)

admin.site.register(Partner)
