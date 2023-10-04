from django.urls import path
from . import views

urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('article/<int:pk>/',views.BlogDetailView.as_view(),name='blogdetail'),
    path('register/', views.register, name="register"),
    path('login/', views.login_request, name="login"),
    path('createblog/',views.AddPostView.as_view(),name='createblog'),
    path('article/edit/<int:pk>/',views.UpdatePostView.as_view(),name='updatepost'),
    path('article/remove/<int:pk>/',views.DeletePostView.as_view(),name='deletepost'),
]


