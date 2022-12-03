from typing import Optional
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import widgets
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.
from .models import Patient


class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    context_object_name: Optional[str] = "patients"
    template_name = "patients/list.html"



class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = "patients/detail.html"
    context_object_name: str = "patients"



class PatientCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Patient
    fields = "__all__"
    success_message = "New patient successfully added."

    def get_form(self):
        """add date picker in forms"""
        form = super(PatientCreateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(
            attrs={"type": "date"})
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        return form



class PatientUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Patient
    fields = "__all__"
    success_message = "Record successfully updated."

    def get_form(self):
        """add date picker in forms"""
        form = super(PatientUpdateView, self).get_form()
        form.fields["date_of_birth"].widget = widgets.DateInput(
            attrs={"type": "date"})
        form.fields["address"].widget = widgets.Textarea(attrs={"rows": 2})
        # form.fields['passport'].widget = widgets.FileInput()
        return form



class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy("patient-list")

