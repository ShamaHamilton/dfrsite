from rest_framework.generics import ListAPIView
from django.shortcuts import render

from women.serializers import WomenSerializer
from women.models import Women


class WomenAPIView(ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
