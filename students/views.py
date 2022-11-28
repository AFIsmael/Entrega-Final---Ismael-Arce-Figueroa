from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from students.models import Student
from students.forms import StudentForm


class StudentListView(ListView):
    model = Student
    template_name = "student/student_list.html"
    paginate_by = 3

class StudentDetailView(DetailView):
    model = Student
    template_name = "student/student_detail.html"
    fields = ["name", "last_name", "email"]


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    template_name = "student/student_form.html"
    success_url = reverse_lazy("student:student-list")

    form_class = StudentForm

    def form_valid(self, form):
        """Filter to avoid duplicate Students"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Student.objects.filter(
            name=data["name"],
            last_name=data["last_name"],
            email=data["email"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"The student {data['name']} {data['last_name']} | {data['email']} is already created",
            )
            form.add_error("name", ValidationError("Invalid action"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Student: {data['name']} - {data['last_name']}. successfully created!",
            )
            return super().form_valid(form)

class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    template_name = "student/student_form.html"
    fields = ["name", "last_name", "email"]

    def get_success_url(self):
        student_id = self.kwargs["pk"]
        return reverse_lazy("student:student-detail", kwargs={"pk": student_id})

class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = "student/student_confirm_delete.html"
    success_url = reverse_lazy("student:student-list")