from django.contrib import messages
from django.shortcuts import render

from students.models import Student
from students.forms import StudentForm


def get_student(request):
    students = Student.objects.all()
    return students

def create_student(request):
    if request.method == "POST":
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            data = student_form.cleaned_data
            actual_objects = Student.objects.filter(
                name=data["name"],
                last_name=data["last_name"],
                email=data["email"],
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El student {data['name']} - {data['last_name']} ya está creado",
                )
            else:
                student = Student(
                    name=data["name"],
                    last_name=data["last_name"],
                    email=data["email"],
                )
                student.save()
                messages.success(
                    request,
                    f"student {data['name']} - {data['last_name']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"students": get_student(request)},
                template_name="student/student_list.html",
            )

    student_form = StudentForm(request.POST)
    context_dict = {"form": student_form}
    return render(
        request=request,
        context=context_dict,
        template_name="student/student_form.html",
    )


def students(request):
    students = Student.objects.all()

    context_dict = {"students": students}

    return render(
        request=request,
        context=context_dict,
        template_name="student/student_list.html",
    )
