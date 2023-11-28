from django.urls import path

from bany.views import get_page1

urlpatterns = [
    path('page1/', get_page1, name='page1')
]