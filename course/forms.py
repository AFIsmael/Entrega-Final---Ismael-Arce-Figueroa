from django import forms


class CourseForm(forms.Form):
    name = forms.CharField(
        label="Name Course",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "course-name",
                "placeholder": "name course",
                "required": "True",
            }
        ),
    )
    code = forms.IntegerField(
        label="Code:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "course-code",
                "placeholder": "code course",
                "required": "True",
            }
        ),
    )
