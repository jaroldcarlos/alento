from django.urls import path

from apps.worker.views import create_worker, list_worker
from apps.patient.views import create_patient, list_patient
from apps.blog.views import create_blog, list_blog
from apps.schedule.views import create_event, list_event, print_event
from .views import home, calendar


app_name = "dashboard"
urlpatterns = [

    path('administration/create_worker/', create_worker, name='create_worker'),
    path('administration/list_worker/', list_worker, name='list_worker'),
    path('administration/view_worker/<dni>', list_worker, name='list_worker'),

    path('administration/create_patient/', create_patient, name='create_patient'),
    path('administration/list_patient/', list_patient, name='list_patient'),
    path('administration/view_patient/<dni>', list_worker, name='list_patient'),

    path('schedule/', calendar, name='calendar'),
    path('schedule/create_event/', create_event, name='create_event'),
    path('schedule/list_event/', list_event, name='list_event'),
    path('schedule/print_event/<year>/<month>/<patient>', print_event, name='print_event'),

    path('blog/create-blog/', create_blog, name='create_blog'),
    path('blog/list-blog/', list_blog, name='list_blog'),
    path('blog/view-blog/<pk>', list_blog, name='list_blog'),

    path('', home, name='home'),
]
