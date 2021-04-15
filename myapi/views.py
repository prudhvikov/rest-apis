from rest_framework import viewsets

from myapi.serializers import PersonSerializer
from myapi.models import Person


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer
