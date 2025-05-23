from rest_framework import routers
from .views import JudgeViewSet, ParticipantViewSet, ScoreViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'judges', JudgeViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'scores', ScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
