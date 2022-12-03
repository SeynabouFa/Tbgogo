from datetime import timedelta

from django.db import models
from django.urls import reverse
from django.db.models import F
from django.db.models import Q

from apps.patients.models import Patient

# Create your models here.

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class TBModel(TimeStampMixin):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Patient")
    case_id = models.CharField(max_length=20, verbose_name="Case ID")
    case_img = models.ImageField(blank=True, upload_to="tb/cases/", verbose_name="Case Image")

    class Meta:
        ordering = ["patient", "case_id"]

    def __str__(self):
        return f"{self.patient}-{self.case_id}"

    def get_absolute_url(self):
        return reverse("tb-detail", kwargs={"pk": self.pk})

    def get_new_cases(self):
        # return all cases from 3 days ago
        return TBModel.objects.filter(updated_at__lt=F('updated_at') + timedelta(days=3))



class TBResult(models.Model):

    RESULTS = [("positive", "Positive"), ("negative", "Negative"), ("not-classified", "Not Classified")]

    tb_case = models.ForeignKey(TBModel, on_delete=models.CASCADE, verbose_name="TB Case")
    description = models.CharField(max_length=200)
    result = models.CharField(max_length=20, choices=RESULTS, default="negative")

    def get_not_classified(self):
        return TBResult.objects.filter(result__eq="not-classified")

    def get_resolved(self):
        return TBResult.objects.filter(Q(result__eq="negative") | Q(result__eq="positive"))

    