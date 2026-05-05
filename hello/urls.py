from django.urls import path
from hello import views

urlpatterns = [
    path("", views.HomeListView.as_view(), name="home"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("report/", views.feedback_report, name="feedback_report"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]