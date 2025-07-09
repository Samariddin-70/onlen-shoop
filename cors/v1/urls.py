from django.urls import path
from .views import CategoryViews

urlpatterns=[
    path('test/', CategoryViews.as_view()),
    path('test/<int:id>/', CategoryViews.as_view()),
]