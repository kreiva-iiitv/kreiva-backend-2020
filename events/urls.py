from django.urls import include, path
from rest_framework import routers
from events.views import *

router = routers.DefaultRouter()
router.register('event', EventViewSet)
router.register('event_member', MemberViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('lamp', LampStatus.as_view(), name="lamp"),
    path('lampp', LampStatusPost.as_view(), name='lampp')
]
