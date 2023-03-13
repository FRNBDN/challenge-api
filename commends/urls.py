from django.urls import path
from commends import views

urlpatterns = [
    path('commends/', views.CommendList.as_view()),
    path('commends/<int:pk>', views.CommendDetail.as_view()),
]
