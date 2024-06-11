from django.urls import path
from .views import HomePageView, AboutPageView, upload, FileListView, upload_file, UploadFileView

urlpatterns = [
    path('upload/', upload, name='upload'),
    path('files/', FileListView.as_view(), name='file_list'),
    path('files/upload/', UploadFileView.as_view(), name='upload_file'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home')
]