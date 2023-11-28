from django.urls import path


from .views import get_page2

urlpatterns = [
    path('page2/', get_page2, name='page2')



]