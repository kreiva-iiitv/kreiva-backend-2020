from django.urls import include, path
from rest_framework import routers
from teams.views import *

router = routers.DefaultRouter()
router.register('team', TeamViewSet)
router.register('team_member', MemberViewSet)

urlpatterns = [
    path('', include(router.urls))
]
