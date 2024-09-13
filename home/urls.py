from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.loginPage),
    path('register/', views.register),
    path('receipe/', views.receipe_page)
]