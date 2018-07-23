from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.courseList, name="courses"),
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)/$', views.stepDetail, name="step"),
    url(r'(?P<pk>\d+)/$', views.courseDetail, name="detail"),
]