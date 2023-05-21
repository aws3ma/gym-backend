from django.urls import path
from .views import BodyBuilderView


urlpatterns = [
    path("", BodyBuilderView.as_view(), name="bodybuilder"),

]