from django.urls import path

from package import views
from webpack import settings

urlpatterns = [


    path('index/', views.showIndex, name='showIndex'),
    path('addClassify/', views.addClassify, name='addClassify'),
    path('subClassify/', views.subClassify, name='subClassify'),
    path('updateClassify/', views.updateClassify, name='updateClassify'),
    path('addWebsite/', views.addWebsite, name='addWebsite'),
    path('delWebsite/', views.delWebsite, name='delWebsite'),
    path('generateQrcode/', views.generateQrcode, name='generateQrcode'),
    path('is_delete_1/', views.is_delete_1, name='is_delete_1'),

]
