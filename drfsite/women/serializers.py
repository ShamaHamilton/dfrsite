from rest_framework.serializers import ModelSerializer

from women.models import Women


class WomenSerializer(ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'cat_id')
