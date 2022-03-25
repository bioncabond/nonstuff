from django.urls import path
from .views import NonstuffList, NonstuffDetail

urlpatterns =[
    path('', NonstuffList.as_view(), name='nonstuff_list'),
    path('<int:pk>/', NonstuffDetail.as_view(), name='nonstuff_detail'),
]