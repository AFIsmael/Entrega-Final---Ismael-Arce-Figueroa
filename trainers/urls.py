from django.urls import path

from trainers import views

app_name = "trainer"
urlpatterns = [
    path("trainers", views.TrainerListView.as_view(), name="trainer-list"),
    path("trainer/add/", views.TrainerCreateView.as_view(), name="trainer-add"),
    path("trainer/<int:pk>/detail/", views.TrainerDetailView.as_view(), name="trainer-detail"),
    path("trainer/<int:pk>/update/", views.TrainerUpdateView.as_view(), name="trainer-update"),
    path("trainer/<int:pk>/delete/", views.TrainerDeleteView.as_view(), name="profesor-delete"),
]
