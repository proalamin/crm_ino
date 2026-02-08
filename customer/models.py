from django.db import models


class Personal(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    student = models.ForeignKey(
        Personal,
        on_delete=models.CASCADE,
        related_name='educations'
    )

    degree = models.CharField(max_length=100)
    institution_name = models.CharField(max_length=200)
    passing_year = models.IntegerField()
    result = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student.name} - {self.degree}"
