from django.contrib import admin
from django.urls import path
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.chat_view, name='chat'),
    path('api/chat/', views.chat_api, name='chat_api'),
]
