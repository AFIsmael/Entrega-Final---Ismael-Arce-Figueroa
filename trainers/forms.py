from django import forms

from trainers.models import Trainer

class TrainerForm(forms.ModelForm):
    name = forms.CharField(
        label="Name of Trainer",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "trainer-name",
                "placeholder": "Name of Trainer",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Last Name of Trainer",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "trainer-last-name",
                "placeholder": "Last Name of Trainer",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "trainer-email",
                "placeholder": "email",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Trainer
        fields = ["name", "last_name", "email"]
