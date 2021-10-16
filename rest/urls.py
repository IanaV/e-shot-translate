from django.urls import path
from . import views

urlpatterns = [
    path('', views.rest_home, name='rest_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.RestDetailView.as_view(), name='rest-detail'),
    path('<int:pk>/update', views.RestUpdateView.as_view(), name='rest-update'),
    path('<int:pk>/delete', views.RestDeleteView.as_view(), name='rest-delete')
]