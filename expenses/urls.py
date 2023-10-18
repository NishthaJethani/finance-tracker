from django.urls import path
from .views import ExpenseCreateView, ExpenseListView, ExpenseUpdateView, ExpenseDeleteView

app_name = 'expenses'

urlpatterns = [

    path('', ExpenseListView.as_view(), name='expense-home'),
    path('create/', ExpenseCreateView.as_view(), name='expense-create'),
    path('edit/<int:pk>/', ExpenseUpdateView.as_view(), name='expense-edit'),
    path('delete/<int:pk>/', ExpenseDeleteView.as_view(), name='expense-delete'),

]