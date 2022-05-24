from django.urls import path, include, re_path
from rest_framework import routers
from . import views

## For getting an API token from username and password for a user
from rest_framework.authtoken import views as api_auth_views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'food', views.FoodViewSet)
router.register(r'portion', views.PortionViewSet)

app_name = 'api'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^api-token-auth/$', api_auth_views.obtain_auth_token), ## For viewing API tokens
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    ## 
    path('', include(router.urls)),

    ## Get Me
    re_path(r'^me/$', views.MeView.as_view(), name='config'),
    re_path(r'^me_today/$', views.MeTodayView.as_view(), name='config'),
    re_path(r'^hypothetical/$', views.HypotheticalView.as_view(), name='config'),
]