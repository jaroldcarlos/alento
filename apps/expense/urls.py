from django.urls import path

from . import views

app_name = "expense"
urlpatterns = [
    path('',                views.expense_list,     name='expense_list'),
    path('create/',         views.expense_create,   name='expense_create'),
    path('detail/<int:pk>', views.expense_detail,   name='expense_detail'),
    path('update/<int:pk>', views.expense_update,   name='expense_update'),
    path('delete/<int:pk>', views.expense_delete.as_view(), name='expense_delete'),
]
