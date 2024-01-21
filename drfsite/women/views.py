from django.forms import model_to_dict
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from women.serializers import WomenSerializer
from women.models import Women


class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': WomenSerializer(post_new).data})
