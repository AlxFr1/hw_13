
from django.urls import path

from hw_13.views import *
urlpatterns = [
    path('', home, name='quotes'),
    path('quote/', quote, name='quotes'),
    path('authors/', authors, name='authors'),
    path('authors/<int:pk>', authors_info, name='author-detail')
]
