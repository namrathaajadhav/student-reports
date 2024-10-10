from django.urls import path
from .views import add_student, download_pdf
 
urlpatterns = [
    path('', add_student, name='add_student'),
    path('download_pdf/', download_pdf, name='download_pdf'),
]