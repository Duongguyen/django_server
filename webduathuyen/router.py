from app.viewsets import PartnerViewset, ReferencesViewset, LawViewset, TextViewset, CompetitionViewset,\
    IntroMissionViewset, IntroFederationViewset, IntroEvolutionViewset, GreetingViewset, GroupViewset, AthleteViewset, \
    CoachViewset, RefereeViewset, EventViewset, PhotoViewset, BlogViewset

from rest_framework import routers

router = routers.DefaultRouter()
router.register('partners', PartnerViewset)
router.register('references', ReferencesViewset)
router.register('laws', LawViewset)
router.register('texts', TextViewset)
router.register('competitions', CompetitionViewset)
router.register('missions', IntroMissionViewset)
router.register('federations', IntroFederationViewset)
router.register('evolutions', IntroEvolutionViewset)
router.register('greetings', GreetingViewset)
router.register('groups', GroupViewset)
router.register('athletes', AthleteViewset)
router.register('coachs', CoachViewset)
router.register('referees', RefereeViewset)
router.register('events', EventViewset)
router.register('photos', PhotoViewset)
router.register('blogs', BlogViewset)