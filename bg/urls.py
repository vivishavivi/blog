from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('delete/<int:post_id>/',views.delete,name='delete'),
    path('edit/<int:post_id>/',views.edit,name='edit'),
    path('create/',views.create, name="create"),
    path('register/',views.register, name="register"),
]