from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator

# Create your models here.

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Patient(TimeStampMixin):

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    first_name = models.CharField(max_length=200, verbose_name="First Name")
    last_name = models.CharField(max_length=200, verbose_name="Last Name")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male", verbose_name="Gender")
    date_of_birth = models.DateField(default=timezone.now, verbose_name="Date Of Birth")
    mobile_num_regex = RegexValidator(
        regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!"
    )
    mobile_number = models.CharField(
        validators=[mobile_num_regex], max_length=13, blank=True, verbose_name="Mobile Number"
    )

    address = models.TextField(blank=True, verbose_name="Adress")
    email = models.EmailField(blank=True, verbose_name="Email")

    class Meta:
        ordering = ["first_name", "last_name", "date_of_birth"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - ({self.mobile_number})"

    def get_absolute_url(self):
        return reverse("patient-detail", kwargs={"pk": self.pk})


class PatientBulkUpload(TimeStampMixin):
    date_uploaded = models.DateTimeField(auto_now=True, verbose_name="Date Uploaded")
    csv_file = models.FileField(upload_to="patients/bulkupload/", verbose_name="CSV File")