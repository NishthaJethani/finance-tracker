from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import date, timedelta, datetime
from django.views.generic.base import TemplateView



# Create your views here.

class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense_form.html'
    success_url = reverse_lazy('expenses:expense-home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expense_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            return Expense.objects.filter(user=self.request.user, date__range=(start_date, end_date))
        else:
            # If no dates provided, display all expenses
            return Expense.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        
        if start_date and end_date:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            expenses = Expense.objects.filter(user=self.request.user, date__range=(start_date, end_date))
        else:
            # If no dates provided, display all expenses
            expenses = Expense.objects.filter(user=self.request.user)
        
        total_expenses = sum(expense.amount for expense in expenses)
        context['total_expenses'] = total_expenses
        return context


class ExpenseUpdateView(UpdateView):
    model = Expense
    template_name = 'expense_edit.html'
    fields = ['category', 'amount', 'date', 'description']
    success_url = '/expenses/'

class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'expense_confirm_delete.html'
    success_url = '/expenses/'

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    