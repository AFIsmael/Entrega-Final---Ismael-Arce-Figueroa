from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from trainers.models import Trainer
from trainers.forms import TrainerForm


class TrainerListView(ListView):
    model = Trainer
    template_name = "trainer/trainer_list.html"
    paginate_by = 3


class TrainerDetailView(DetailView):
    model = Trainer
    template_name = "trainer/trainer_detail.html"
    fields = ["name", "last_name", "email"]


class TrainerCreateView(LoginRequiredMixin, CreateView):
    model = Trainer
    template_name = "trainer/trainer_form.html"
    success_url = reverse_lazy("trainer:trainer-list")

    form_class = TrainerForm

    def form_valid(self, form):
        """Filter to avoid duplicate trainers"""
        data = form.cleaned_data
        form.instance.owner = self.request.user
        actual_objects = Trainer.objects.filter(
            name=data["name"],
            last_name=data["last_name"],
            email=data["email"],
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"The trainer {data['name']} {data['last_name']} | {data['email']} is already created",
            )
            form.add_error("name", ValidationError("Invalid action"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Trainer: {data['name']} - {data['last_name']}. successfully created!",
            )
            return super().form_valid(form)


class TrainerUpdateView(LoginRequiredMixin, UpdateView):
    model = Trainer
    template_name = "trainer/trainer_form.html"
    fields = ["name", "last_name", "email"]

    def get_success_url(self):
        trainer_id = self.kwargs["pk"]
        return reverse_lazy("trainer:trainer-detail", kwargs={"pk": trainer_id})

class TrainerDeleteView(LoginRequiredMixin, DeleteView):
    model = Trainer
    template_name = "trainer/trainer_confirm_delete.html"
    success_url = reverse_lazy("trainer:trainer-list")
