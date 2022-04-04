from django.http import Http404
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView
from django.views.generic import CreateView
from family.models import Childrens, Parents
from family.serializers import ChildrensSerializer, ParentsSerializer
# Create your views here.

class ParentsAPIcreateView(CreateAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer

class ParentsAPIlistView(ListAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer

class ParentsAPIdeleteView(DestroyAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer

class ParentsAPIUpdateView(UpdateAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer


class ParentsAPIdetailView(RetrieveAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer

class ChildrenCreateAPIView(CreateAPIView):
    queryset = Childrens.objects.all()
    serializer_class = ChildrensSerializer


    def perform_create(self, serializer):
        p_i = self.kwargs['parent_id']
        Child_Name = self.request.POST['Child_Name']
        serializer.save(parent_id=Parents.objects.get(id = p_i),Child_Name=Child_Name)


# class ChildrenCreateView(CreateView):
#     model = Childrens
#     fields = ['Child_Name']
#     template_name = "form.html"

#     def post(self, request, *args, **kwargs):
#         p_i = Parents.objects.get(pk= self.kwargs['parent_id'])
#         new_child =Childrens.objects.create(parent_id =p_i, Child_Name= self.request.POST['Child_Name'])
#         return new_child

class ChildrenAPIParentwiseListView(ListAPIView):
    serializer_class = ChildrensSerializer

    def get_queryset(self):
        return  Childrens.objects.filter(parent_id = self.kwargs['parent_id'])

class ChildrenAPIDetailView(RetrieveAPIView):
    serializer_class = ChildrensSerializer

    def get_queryset(self):
        return  Childrens.objects.filter(parent_id = self.kwargs['parent_id'])


class ChildrenDeleteAPIView(DestroyAPIView):
    serializer_class = ChildrensSerializer

    def get_queryset(self):
        return  Childrens.objects.filter(parent_id = self.kwargs['parent_id'])


class ChildrenUpdateAPIView(UpdateAPIView):
    serializer_class = ChildrensSerializer

    def get_queryset(self):
        return  Childrens.objects.filter(parent_id = self.kwargs['parent_id'])
