from django.urls import path
from .views import EditorPageView

urlpatterns = [
    path('', EditorPageView.as_view(), name='editor')
]