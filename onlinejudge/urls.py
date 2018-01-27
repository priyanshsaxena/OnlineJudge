from django.conf.urls import url

from . import views

app_name = 'onlinejudge'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^problems/$', views.problems, name='problems'),
    url(r'^problems/(?P<problem_name>[a-zA-Z]+)/$', views.problem_details, name='problem_details'),
    url(r'^submitted/$', views.new_submission, name='new_submission'),
]

