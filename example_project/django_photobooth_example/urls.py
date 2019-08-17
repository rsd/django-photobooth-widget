from django.contrib import admin
from django.urls import path
from test_app import views

urlpatterns = [

    path('', views.index, name='index'),

    path('new/', views.SelfieCreateView.as_view(), name="new"),
    path('selfie/', views.SelfieDetailView.as_view(), name="selfie"),
    path('selfies/', views.SelfieListView.as_view(), name='selfies'),
    path('admin/', admin.site.urls),
]
