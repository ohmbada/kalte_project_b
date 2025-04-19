from django.urls import path
from . import views
from .views import FileUploadView

urlpatterns = [
    # path('', views.calc),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]
