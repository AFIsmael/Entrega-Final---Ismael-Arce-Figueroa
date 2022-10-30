from django import forms


class TrainerForm(forms.Form):
    name = forms.CharField(
        label="Name of Trainer",
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
