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
from rest_framework.decorators import action

from women.serializers import WomenSerializer
from women.models import Category, Women


class WomenViewSet(ModelViewSet):
    # queryset = Women.objects.all()  # нужно указать basename, если нет queryset
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)

    # @action(methods=['get'], detail=False)  # добавление нового url
    # def category(self, request):            # .../api/v1/women/category
    #     cats = Category.objects.all()
    #     return Response({'cats': [c.name for c in cats]})

    @action(methods=['get'], detail=True)  # получение конкретной категории
    def category(self, request, pk=None):  # .../api/v1/women/1/category/
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

# class WomenAPIList(ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIUpdate(UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
