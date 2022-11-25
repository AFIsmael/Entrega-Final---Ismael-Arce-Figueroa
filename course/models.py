from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models
from ckeditor.fields import RichTextField
from trainers.models import Trainer

class Course(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    code = models.IntegerField(null=False, blank=False)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='course', null=True, blank=True)
    owner = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    associated_trainer = models.ForeignKey(Trainer, null= True, blank=False, on_delete= models.CASCADE)
    comments = models.ManyToManyField(
        User, through="Comment", related_name="comments_owned"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            "name",
            "code",
        )
        ordering = ["-created_at"]

    def __str__(self):
        return f"Course: {self.name} | code: {self.code}"


class Comment(models.Model):
    text = models.TextField(
        validators=[
            MinLengthValidator(
                10, "Comment must be longer than 10 characters")
        ]
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task(models.Model):
    name = models.CharField(max_length=40)
    due_date = models.DateField()
    is_delivered = models.BooleanField()
    associated_course = models.ForeignKey(Course, null= True, blank=False, on_delete= models.CASCADE)

    def __str__(self):
        is_delivered = "Yes" if self.is_delivered else "No"
        return f"{self.name} | date: {self.due_date} | delivered: {is_delivered}"
