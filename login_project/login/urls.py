from django.urls import path
# from.models import Creating

from login import views

urlpatterns=[

    path('',views.Creating,name='creating'),
    path('show',views.showlogin,name='show'),
    path('editing/<int:pk>',views.Edit ,name='editing'),
    path('delete/<int:pk>',views.Delete,name='delete'),
]