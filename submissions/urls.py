from django.urls import include, path
from rest_framework import routers
from submissions.views import *

router = routers.DefaultRouter()
router.register('team_sub', TeamSubmissionViewSet)
router.register('photo_sub', IndividialPhotoSubmissionViewSet)
router.register('video_sub', IndividialVideoSubmissionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
