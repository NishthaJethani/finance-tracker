from django.urls import path
from .views import ExpenseCreateView, ExpenseListView

app_name = 'expenses'

urlpatterns = [
    path('', ExpenseListView.as_view(), name='home'),
    path('create/', ExpenseCreateView.as_view(), name='expense-create'),
]