from .views import CamListView, CamEditView, IceCreamListView, IceCreamEditView, InView, OutView  
from django.urls import path, include

urlpatterns = [
    path('cams/', CamListView.as_view()),
    path('cams/dit/<int:id>/', CamEditView.as_view()),
    path('ice/', IceCreamListView.as_view()),
    path('ice/edit/<str:code>/', IceCreamEditView.as_view()),
    path('in/<str:code>/', InView.as_view()),
    path('out/<str:code>/', OutView.as_view()),

]
