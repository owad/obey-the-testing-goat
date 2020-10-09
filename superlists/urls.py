from django.conf.urls import url, include
from lists import views, urls as list_urls


urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^lists/', include(list_urls)),
]
