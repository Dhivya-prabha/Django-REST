from rest_framework import serializers
from .models import Positions, Ships


class VesselPositionsSerializer(serializers.ModelSerializer):

  class Meta():
    model = Positions
    exclude = ('created', 'updated')


class ShipsSerializer(serializers.ModelSerializer):

  class Meta():

    model = Ships
    exclude = ('created', 'updated')

