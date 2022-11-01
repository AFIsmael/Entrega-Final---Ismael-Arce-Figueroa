from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(
        label="Name of Student",
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
        label="Last Name of Student",
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
