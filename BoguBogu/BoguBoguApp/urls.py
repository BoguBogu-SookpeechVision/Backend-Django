from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('vowel_recognition/', views.vowel_recognition, name='vowel_recognition'),
    path('vowel_recognition/result/', views.result_view, name='result_view'),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)