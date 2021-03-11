from django.urls import path
from .views import BlogList

urlpatterns=[
    path('blog/',BlogList.as_view())
]