from django.urls import include, path
from rest_framework import routers
# from rest_framework.authtoken import views
from admin import views
from rest_framework.settings import api_settings


router = routers.DefaultRouter()
router.register(r'about', views.CompanyViewSet)
router.register(r'blog', views.BlogViewSet)
router.register(r'podcast', views.PodcastViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.CreateTokenView.as_view()),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]