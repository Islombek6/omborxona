from django.urls import path

from main.views import *

urlpatterns  = [
    path('', bolimlar_view,name='bolimlar'),
    path('error/', error_view,name='error'),
    path('mahsulotlar/', MaxsulotlarView.as_view(),name='mahsulotlar'),
    path('mahsulotlar/<int:pk>/tahrirlash', MaxsulotlarTaxrirlashView.as_view()),
    path('mahsulot-ochirish/<int:id>/', mahsulot_ochirish, name='mahsulot_ochirish'),

    path('mijozlar/', MijozlarView.as_view(),name='mijozlar'),
    path('mijoz/<int:pk>/tahrirlash', MijozTahrirlashView.as_view()),
    path('mijoz-ochirish/<int:id>/', mijoz_ochirish, name='mijoz_ochirish'),
]