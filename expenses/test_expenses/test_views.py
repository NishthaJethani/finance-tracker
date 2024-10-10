from django.urls import reverse
from django.test import TestCase
from expenses.models import Expense
from django.contrib.auth.models import User
from decimal import Decimal


class ExpenseViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_expense(self):
        response = self.client.post(reverse('expenses:expense-create'), {
            'category': 'Lunch',
            'amount': '50.00',
            'date': '2024-10-09',
            'description': 'Lunch at restaurant'
        })
        self.assertEqual(response.status_code, 302)  # Check for successful redirect
        self.assertEqual(Expense.objects.count(), 1)  # Ensure one expense is created
        self.assertEqual(Expense.objects.first().description, 'Lunch at restaurant')

    def test_list_expenses(self):
        Expense.objects.create(user=self.user, category='Dinner', amount=Decimal('30.00'), date='2024-10-09', description='Dinner at home')
        response = self.client.get(reverse('expenses:expense-home'))
        self.assertEqual(response.status_code, 200)  # Check for successful response
        self.assertContains(response, 'Dinner at home')  # Check if the expense is listed

    def test_update_expense(self):
        expense = Expense.objects.create(user=self.user, category='Snacks', amount=Decimal('10.00'), date='2024-10-09', description='Snack time')
        response = self.client.post(reverse('expenses:expense-edit', args=[expense.id]), {
            'category': 'Snacks',
            'amount': '15.00',
            'date': '2024-10-10',
            'description': 'Updated snack time'
        })
        self.assertEqual(response.status_code, 302)  # Check for successful redirect
        expense.refresh_from_db()  # Refresh the instance from the database
        self.assertEqual(expense.amount, Decimal('15.00'))  # Check if amount is updated
        self.assertEqual(expense.description, 'Updated snack time')  # Check if description is updated

    def test_delete_expense(self):
        expense = Expense.objects.create(user=self.user, category='Entertainment', amount=Decimal('100.00'), date='2024-10-09', description='Movie night')
        response = self.client.post(reverse('expenses:expense-delete', args=[expense.id]))
        self.assertEqual(response.status_code, 302)  # Check for successful redirect
        self.assertEqual(Expense.objects.count(), 0)  # Ensure the expense is deleted

    def test_dashboard_view(self):
        Expense.objects.create(user=self.user, category='Lunch', amount=Decimal('50.00'), date='2024-10-09', description='Lunch')
        Expense.objects.create(user=self.user, category='Dinner', amount=Decimal('70.00'), date='2024-10-09', description='Dinner')
        response = self.client.get(reverse('expenses:dashboard'))
        self.assertEqual(response.status_code, 200)  # Check for successful response
        self.assertIn('monthly_expenses', response.context)  # Check if monthly expenses are in context
        self.assertIn('daily_expenses', response.context)  # Check if daily expenses are in context

