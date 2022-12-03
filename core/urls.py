# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path('api-auth/', include('rest_framework.urls')), # Allow to use the django restframework browsable API,
    path("patients/", include("apps.patients.urls")),
    # path("tb_cases/", include("apps.tb.urls")),

    # ADD NEW Routes HERE

    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
]
