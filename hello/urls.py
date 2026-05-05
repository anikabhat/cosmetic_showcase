from django.urls import path
from hello import views
from hello.models import Review
home_list_view = views.HomeListView.as_view(
    queryset=Review.objects.order_by("-log_date")[:5], # :5 limits the results to the five
    context_object_name="review_list",
    template_name="hello/home.html",
)
urlpatterns = [
    path("", home_list_view, name="home"),
    path('hello/<str:name>/', views.hello_there, name='hello_there'),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path('review/', views.submit_review, name='submit_review')
]
