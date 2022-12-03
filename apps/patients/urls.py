from django.urls import path

from .views import (
    PatientCreateView,
    PatientDeleteView,
    PatientDetailView,
    PatientListView,
    PatientUpdateView,
)

urlpatterns = [
    path("list", PatientListView.as_view(), name="patient-list"),
    path("<int:pk>/", PatientDetailView.as_view(), name="patient-detail"),
    path("create/", PatientCreateView.as_view(), name="patient-create"),
    path("<int:pk>/update/", PatientUpdateView.as_view(), name="patient-update"),
    path("delete/<int:pk>/", PatientDeleteView.as_view(), name="patient-delete"),
    # path("upload/", PatientBulkUploadView.as_view(), name="patient-upload"),
    # path("download-csv/", DownloadCSVViewdownloadcsv.as_view(), name="download-csv"),
]