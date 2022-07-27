from django.urls import include, path
from rest_framework import routers
from public import views


company_view = views.CompanyView.as_view({'get': 'retrieve'})
blog_list = views.BlogList.as_view()
blog_view = views.BlogDetail.as_view()
podcast_list = views.PodcastList.as_view()
podcast_view = views.PodcastDetail.as_view()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('about/', company_view),
    path('blog/', blog_list),
    path('blog/<int:pk>/', blog_view),
    path('podcast/', podcast_list),
    path('podcast/<int:pk>/', podcast_view),
]