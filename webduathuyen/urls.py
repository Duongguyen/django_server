"""
URL configuration for webduathuyen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from .router import router


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('app.urls')),
    path('customer/', include('app.urls_customer')),
    path('photo/', include('app.urls_photo')),
    path('blog/', include('app.urls_blog')),
    path('intro/greeting/', include('app.urls_greeting')),
    path('intro/federation/', include('app.urls_federation')),
    path('intro/evolution/', include('app.urls_evolution')),
    path('intro/mission/', include('app.urls_mission')),
    path('event/', include('app.urls_event')),
    path('profile/group/', include('app.urls_group')),
    path('profile/athlete/', include('app.urls_athlete')),
    path('profile/coach/', include('app.urls_coach')),
    path('profile/referee/', include('app.urls_referee')),
    path('library/text/', include('app.urls_text')),
    path('library/law/', include('app.urls_law')),
    path('library/references/', include('app.urls_references')),
    path('partner/', include('app.urls_partner')),
    path('competition/', include('app.urls_competition')),
    path('contact/', include('app.urls_contact')),
    path('GET/', include(router.urls))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
