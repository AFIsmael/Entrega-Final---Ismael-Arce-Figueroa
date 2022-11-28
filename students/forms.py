from django import forms
from students.models import Student


class StudentForm(forms.ModelForm):
    name = forms.CharField(
        label="Name",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "student-name",
                "placeholder": "Name of Student",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Last Name",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "student-last-name",
                "placeholder": "Last Name of Student",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "student-email",
                "placeholder": "email",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Student
        fields = ["name", "last_name", "email"]
