from django.urls import path

from course import views

app_name = "course"
urlpatterns = [
    path("courses/", views.CourseListView.as_view(), name="course-list"),
    path("course/add/", views.CourseCreateView.as_view(), name="course-add"),
    path("course/<int:pk>/detail/", views.CourseDetailView.as_view(), name="course-detail"),
    path("course/<int:pk>/update/", views.CourseUpdateView.as_view(), name="course-update"),
    path("course/<int:pk>/delete/", views.CourseDeleteView.as_view(), name="course-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),

    path("tasks", views.TaskListView.as_view(), name="task-list"),
    path("task/add/", views.TaskCreateView.as_view(), name="task-add"),
    path("task/<int:pk>/detail/", views.TaskDetailView.as_view(), name="task-detail"),
    path("task/<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),
]