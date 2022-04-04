from django.urls import path

from.views import *

urlpatterns = [
    path('parents/', ParentsAPIlistView.as_view(), name='parent_list'),
    path('parents/create/', ParentsAPIcreateView.as_view(), name='create_parent'),
    path('parents/<int:pk>/update/', ParentsAPIUpdateView.as_view(), name='parent_update'),
    path('parents/<int:pk>/delete/', ParentsAPIdeleteView.as_view(), name='parent_delete'),
    path('parents/<int:pk>/', ParentsAPIdetailView.as_view(), name='parent_detail'),
    path('parents/<int:parent_id>/children/create/', ChildrenCreateAPIView.as_view(), name='create_children'),
    path('parents/<int:parent_id>/children/<int:pk>/', ChildrenAPIDetailView.as_view(), name='create_children'),
    path('parents/<int:parent_id>/children/', ChildrenAPIParentwiseListView.as_view(), name='create_children'),
    path('parents/<int:parent_id>/children/<int:pk>/delete/', ChildrenDeleteAPIView.as_view(), name='create_children'),
    path('parents/<int:parent_id>/children/<int:pk>/update/', ChildrenUpdateAPIView.as_view(), name='create_children'),
    #path('parents/<int:parent_id>/children/create/', ChildrenCreateView.as_view(), name='create_children'),
]
