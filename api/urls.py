
from django.urls import path
from api.views import SiswaList

urlpatterns = [
    path('siswa/', SiswaList.as_view()),
]