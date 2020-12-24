from .models import crud
from rest_framework import serializers


class crudSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = crud
        fields = ['name','se']
