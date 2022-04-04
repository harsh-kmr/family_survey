from rest_framework.serializers import ModelSerializer
from .models import Parents, Childrens

class ParentsSerializer(ModelSerializer):

    class Meta:
        model = Parents
        fields = '__all__'

class ChildrensSerializer(ModelSerializer):

    class Meta:
        model = Childrens
        fields = '__all__'
