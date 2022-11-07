from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from course.forms import CommentForm
from course.forms import CourseForm
from course.forms import TaskworkForm
from course.models import Comment
from course.models import Course
from course.models import Taskwork


class CourseListView(ListView):
    model = Course
    paginate_by = 3


class CourseDetailView(DetailView):
    model = Course
    template_name = "course/course_detail.html"
    fields = ["name", "code", "description"]

    def get(self, request, pk):
        course = Course.objects.get(id=pk)
        comments = Comment.objects.filter(course=course).order_by("-updated_at")
        comment_form = CommentForm()
        context = {
            "course": course,
            "comments": comments,
            "comment_form": comment_form,
        }
        return render(request, self.template_name, context)




class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    success_url = reverse_lazy("course:course-list")

    form_class = CourseForm
    # fields = ["name", "code", "description", "image"]

    def form_valid(self, form):
        """Filter to avoid duplicate courses"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Course.objects.filter(
            name=data["name"], code=data["code"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"the course {data['name']} - {data['code']} is already created",
            )
            form.add_error("name", ValidationError("Invalid action"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Course {data['name']} - {data['code']}, created successfully!",
            )
            return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ["name", "code", "description", "image"]

    def get_success_url(self):
        course_id = self.kwargs["pk"]
        return reverse_lazy("course:course-detail", kwargs={"pk": course_id})

    def post(self):
        pass


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy("course:course-list")


class CommentCreateView(LoginRequiredMixin, CreateView):
    def post(self, request, pk):
        course = get_object_or_404(Course, id=pk)
        comment = Comment(
            text=request.POST["comment_text"], owner=request.user, course=course
        )
        comment.save()
        return redirect(reverse("course:course-detail", kwargs={"pk": pk}))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        course = self.object.course
        return reverse("course:course-detail", kwargs={"pk": course.id})




class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy("course:task-list")

    form_class = TaskForm

    def form_valid(self, form):
        """Filter to avoid duplicate task"""
        data = form.cleaned_data
        actual_objects = Task.objects.filter(name=data["name"]).count()
        if actual_objects:
            messages.error(
                self.request,
                f"The task {data['name']} is already created",
            )
            form.add_error("name", ValidationError("Invalid action"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Entregable: {data['name']}. Creado exitosamente!",
            )
            return super().form_valid(form)


class TaskDetailView(DetailView):
    model = Task
    fields = ["name", "due_date", "is_delivered"]


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["name", "due_date", "is_delivered"]

    def get_success_url(self):
        task_id = self.kwargs["pk"]
        return reverse_lazy("course:task-detail", kwargs={"pk": task_id})


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("course:task-list")

