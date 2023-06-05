from django.urls import path
from .views import PaiementView,PaiementStats


urlpatterns = [
    path("", PaiementView.as_view(), name="list"),
    path("/stats", PaiementStats.as_view(), name="stats"),

]