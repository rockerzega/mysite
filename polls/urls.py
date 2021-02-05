from django.conf.urls import url
from . import views

urlpatterns = [
    # estamos en /polls/
    url(r'^$', views.index,name='index'),
    # creamos la ruta /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    # creamos la ruta /polls/5/results
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),
    # creamos la ruta /polls/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name="vote"),

]


