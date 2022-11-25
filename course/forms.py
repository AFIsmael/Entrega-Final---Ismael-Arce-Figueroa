from ckeditor.widgets import CKEditorWidget
from django import forms

from course.models import Course
from course.models import Task


class CourseForm(forms.ModelForm):
    name = forms.CharField(
        label="Name Course",
        max_length=40,
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

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(),
    )

    image = forms.ImageField(
        required=False
    )

    class Meta:
        model = Course
        fields = ["name", "code", "description", "image"]

class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Enter your comment...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )

class TaskForm(forms.ModelForm):
    name = forms.CharField(
        label="Task name",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "task-name",
                "placeholder": "Task name",
                "required": "True",
            }
        ),
    )

    due_date = forms.DateField(
        label="Delivery due date:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "task-code",
                "placeholder": "Date yyyy-mm-dd",
                "required": "True",
            }
        ),
    )

    is_delivered = forms.BooleanField(
        label="Delivered:",
        required=False,
    )
    course_id = Course.pk
    class Meta:
        model = Task
        fields = ["name", "due_date", "is_delivered", "course_id"]