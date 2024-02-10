from django.forms import model_to_dict
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    UpdateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from women.serializers import WomenSerializer
from women.models import Women


class WomenViewSet(ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# class WomenAPIList(ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIUpdate(UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
