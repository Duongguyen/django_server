from rest_framework import viewsets
from . import serializers
from . import models_partner
from . import models_library
from . import models_competition
from . import models_intro
from . import models_group
from . import models_profile
from . import models_event
from . import models


class PartnerViewset(viewsets.ModelViewSet):
    queryset = models_partner.Partner.objects.all()
    serializer_class = serializers.PartnerSerializer


class ReferencesViewset(viewsets.ModelViewSet):
    queryset = models_library.LibraryReferences.objects.all()
    serializer_class = serializers.LibraryReferencesSerializer


class LawViewset(viewsets.ModelViewSet):
    queryset = models_library.LibraryLaw.objects.all()
    serializer_class = serializers.LibraryLawSerializer


class TextViewset(viewsets.ModelViewSet):
    queryset = models_library.LibraryText.objects.all()
    serializer_class = serializers.LibraryTextSerializer


class CompetitionViewset(viewsets.ModelViewSet):
    queryset = models_competition.Competition.objects.all()
    serializer_class = serializers.CompetitionSerializer


class IntroMissionViewset(viewsets.ModelViewSet):
    queryset = models_intro.IntroMission.objects.all()
    serializer_class = serializers.IntroMissionSerializer


class IntroFederationViewset(viewsets.ModelViewSet):
    queryset = models_intro.IntroFederation.objects.all()
    serializer_class = serializers.IntroFederationSerializer


class IntroEvolutionViewset(viewsets.ModelViewSet):
    queryset = models_intro.IntroEvolution.objects.all()
    serializer_class = serializers.IntroEvolutionSerializer


class GreetingViewset(viewsets.ModelViewSet):
    queryset = models_intro.Greeting.objects.all()
    serializer_class = serializers.GreetingSerializer


class GroupViewset(viewsets.ModelViewSet):
    queryset = models_group.Group.objects.all()
    serializer_class = serializers.GroupSerializer


class AthleteViewset(viewsets.ModelViewSet):
    queryset = models_profile.Athlete.objects.all()
    serializer_class = serializers.AthleteSerializer


class CoachViewset(viewsets.ModelViewSet):
    queryset = models_profile.Coach.objects.all()
    serializer_class = serializers.CoachSerializer


class RefereeViewset(viewsets.ModelViewSet):
    queryset = models_profile.Referee.objects.all()
    serializer_class = serializers.RefereeSerializer


class EventViewset(viewsets.ModelViewSet):
    queryset = models_event.IntroEvent.objects.all()
    serializer_class = serializers.EventSerializer


class PhotoViewset(viewsets.ModelViewSet):
    queryset = models.Photo.objects.all()
    serializer_class = serializers.PhotoSerializer


class BlogViewset(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
