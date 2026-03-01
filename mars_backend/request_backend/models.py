from django.db import models
from django.contrib.auth.models import AbstractUser

class Staff(AbstractUser):
    staff_id = models.CharField(max_length=20, unique=True, blank=True, default='')
    department = models.CharField(max_length=100, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, default='')

    REQUIRED_FIELDS = ['email', 'staff_id', 'full_name']

    def __str__(self):
        return self.username


class FileRequest(models.Model):
    SEX_CHOICES = [('Male', 'Male'), ('Female', 'Female')]

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100)
    suffix = models.CharField(max_length=20, blank=True, default='')
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    year_graduated = models.CharField(max_length=10)
    strand = models.CharField(max_length=100)
    birthdate = models.DateField()
    lrn_number = models.CharField(max_length=20, blank=True, default='')
    request_code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    permanent_address = models.TextField()
    requested_files = models.JSONField(default=list)  # e.g. ['Form 138', 'Form 137']
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.submitted_at.strftime('%Y-%m-%d')}"
