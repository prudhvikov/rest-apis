from rest_framework import serializers
from myapi.models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'country')