from django.contrib import admin
from .models import *
from .models_intro import *
from .models_event import *
from .models_group import *
from .models_partner import *
from .models_competition import *
from .models_profile import *
from .models_library import *
# Register your models here.

admin.site.register(Blog)
admin.site.register(CategoryPhoto)
admin.site.register(CategoryBlog)
admin.site.register(Photo)
admin.site.register(Customer)

admin.site.register(Greeting)
admin.site.register(IntroFederation)
admin.site.register(IntroEvolution)
admin.site.register(IntroMission)

admin.site.register(Events)
admin.site.register(IntroEvent)

admin.site.register(Group)
admin.site.register(Athlete)
admin.site.register(Coach)
admin.site.register(Referee)

admin.site.register(LibraryText)
admin.site.register(LibraryLaw)
admin.site.register(LibraryReferences)

admin.site.register(Partner)

admin.site.register(Competition)
