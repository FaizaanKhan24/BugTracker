from django.urls import path, include
from rest_framework import routers
from . import views

route = routers.DefaultRouter()
route.register(r'UserKind', views.UserKindViewSet)
route.register(r'BugReport', views.BugReportViewSet)
route.register(r'engineers', views.EngineerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(route.urls)),
    path('api-auth',include('rest_framework.urls',namespace='rest_framework'))
]