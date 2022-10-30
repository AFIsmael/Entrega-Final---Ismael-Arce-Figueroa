from django.urls import path

from trainers import views

app_name = "trainer"
urlpatterns = [
    path("trainers", views.trainers, name="trainer-list"),
    path("trainer/add", views.create_trainer, name="trainer-add"),
]
