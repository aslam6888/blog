from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('add-blog',views.add_blog),
    path('my-post',views.my_post),
    path('login',views.login_view),
    path('logout',views.logout_view)
]