from django.urls import path
from .views import PaiementView


urlpatterns = [
    path("", PaiementView.as_view(), name="bodybuilder"),

]