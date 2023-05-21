from rest_framework.serializers import ModelSerializer
from .models import BodyBuilder


class BodyBuilderSerializer(ModelSerializer):
    class Meta:
        model = BodyBuilder
        fields = ('__all__')