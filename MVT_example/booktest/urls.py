
from django.urls import path
from booktest import views
urlpatterns = [
    path('index/', views.index),
    path('books/', views.show_books),
    path('books/<int:bid>', views.detail),
]
