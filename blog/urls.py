from django.urls import path
from . import views
"""これはDjangoの path 関数と、
blog アプリの全ての ビュー（といっても、今は一つもありません。すぐに作りますけど！）をインポートするという意味です。"""

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
