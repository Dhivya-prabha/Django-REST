# from django.shortcuts import render
# from django.contrib import messages
# from .models import upload
# import csv
from django.views.generic import TemplateView
from rest_framework import viewsets, generics, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from upload.models import Positions, Ships
from .serializers import VesselPositionsSerializer, ShipsSerializer


class ShipPositionAPIView(generics.RetrieveAPIView):
    serializer_class = VesselPositionsSerializer
    queryset = Positions.objects.all()
    permission_classes = (AllowAny,)

    def get(self, request, uid=None, *args, **kwargs):
        position_data = Positions.objects.filter(imo_number__imo=uid).order_by('-created')
        file_serializer = VesselPositionsSerializer(position_data, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)


class ShipsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ShipsSerializer
    queryset = Ships.objects.all()
    permission_classes = (AllowAny,)


class Index(TemplateView):
    template_name = 'index.html'
