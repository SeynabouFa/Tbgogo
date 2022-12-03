from rest_framework import serializers

from .models import TBModel


class TBModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TBModel
        fields = "__all__"