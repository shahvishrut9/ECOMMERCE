
from django.urls import path
from .import views

urlpatterns = [
    path('', views.store1, name='store1'),
    path('<slug:category_slug>/', views.store1, name='produts_by_category')
]
