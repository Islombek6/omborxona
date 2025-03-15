from django.urls import path
from .views import *

urlpatterns = [
    path('', SotuvlarView.as_view(), name="sotuvlar"),
    path('sotuvlar/<int:pk>/tahrirlash/', SotuvTahrorlashView.as_view()),
    path('sotuv-ochirish/<int:id>/', sotuv_ochirish, name='sotuv_ochirish'),
]
