from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Expense
from .forms import ExpenseForm
# Create your views here.

class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense_form.html'
    success_url = '/expenses/'

class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense_list.html'
    