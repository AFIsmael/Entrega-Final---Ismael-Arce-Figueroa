from django.contrib import messages
from django.shortcuts import render

from trainers.models import Trainer
from trainers.forms import TrainerForm


def get_trainers(request):
    trainers = Trainer.objects.all()
    return trainers


def create_trainer(request):
    if request.method == "POST":
        trainer_form = TrainerForm(request.POST)
        if trainer_form.is_valid():
            data = trainer_form.cleaned_data
            actual_objects = Trainer.objects.filter(
                name=data["name"],
                last_name=data["last_name"],
                email=data["email"],
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El trainer {data['name']} - {data['last_name']} ya está creado",
                )
            else:
                trainer = Trainer(
                    name=data["name"],
                    last_name=data["last_name"],
                    email=data["email"],
                )
                trainer.save()
                messages.success(
                    request,
                    f"Trainer {data['name']} - {data['last_name']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"trainers": get_trainers(request)},
                template_name="trainer/trainer_list.html",
            )

    trainer_form = TrainerForm(request.POST)
    context_dict = {"form": trainer_form}
    return render(
        request=request,
        context=context_dict,
        template_name="trainer/trainer_form.html",
    )


def trainers(request):
    return render(
        request=request,
        context={"trainers": get_trainers(request)},
        template_name="trainer/trainer_list.html",
    )
