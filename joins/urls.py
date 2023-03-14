from django.urls import path
from joins import views

urlpatterns = [
    path('joins/', views.JoinList.as_view()),
    path('joins/<int:pk>', views.JoinDetail.as_view()),
]
