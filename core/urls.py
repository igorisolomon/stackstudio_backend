from django.urls import include, path
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'company', views.CompanyViewSet)
router.register(r'blog', views.BlogViewSet)
router.register(r'podcast', views.PodcastViewSet)

company_view = views.CompanyView.as_view({'get': 'retrieve'})

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('about-view', company_view)
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]