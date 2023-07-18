from rest_framework import serializers
from .models_partner import Partner
from .models_library import LibraryReferences, LibraryLaw, LibraryText
from .models_event import IntroEvent
from .models_profile import Coach, Athlete, Referee
from .models_competition import Competition
from .models_group import Group
from .models_intro import IntroMission, IntroEvolution, IntroFederation, Greeting
from .models import Photo, Blog


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class LibraryReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryReferences
        fields = '__all__'


class LibraryLawSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryLaw
        fields = '__all__'


class LibraryTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryText
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroEvent
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'


class AthleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Athlete
        fields = '__all__'


class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = '__all__'


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class IntroMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroMission
        fields = '__all__'


class IntroEvolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroEvolution
        fields = '__all__'


class IntroFederationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroFederation
        fields = '__all__'


class GreetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greeting
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

