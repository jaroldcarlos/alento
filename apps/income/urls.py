from django.urls import path

from . import views

app_name = "income"
urlpatterns = [
    path('',                views.income_list,     name='income_list'),
    path('create/',         views.income_create,   name='income_create'),
    path('update/<int:pk>', views.income_update,   name='income_update'),
    path('delete/<int:pk>', views.income_delete.as_view(), name='income_delete'),
]
