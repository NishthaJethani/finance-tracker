from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from expenses.models import Expense
from decimal import Decimal
from django.db.models import Sum

User = get_user_model()

class ExpenseViewsIntegrationTest(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_create_expense(self):
        """Test creating a new expense."""
        response = self.client.post(reverse('expenses:expense-create'), {
            'category': 'Lunch',
            'amount': Decimal('50.00'),
            'date': '2024-10-09',
            'description': 'Lunch at a restaurant',
        })
        self.assertRedirects(response, reverse('expenses:expense-home')) 
        self.assertEqual(Expense.objects.count(), 1) 
        expense = Expense.objects.first()
        self.assertEqual(expense.category, 'Lunch')
        self.assertEqual(expense.amount, Decimal('50.00'))
        self.assertEqual(expense.description, 'Lunch at a restaurant')

    def test_list_expenses(self):
        """Test listing expenses."""
        Expense.objects.create(user=self.user, category='Lunch', amount=Decimal('50.00'), date='2024-10-09', description='Lunch at a restaurant')
        Expense.objects.create(user=self.user, category='Dinner', amount=Decimal('30.00'), date='2024-10-09', description='Dinner at home')

        response = self.client.get(reverse('expenses:expense-home'))
        self.assertEqual(response.status_code, 200)  
        self.assertContains(response, 'Lunch at a restaurant') 
        self.assertContains(response, 'Dinner at home') 

    def test_update_expense(self):
        """Test updating an existing expense."""
        expense = Expense.objects.create(user=self.user, category='Lunch', amount=Decimal('50.00'), date='2024-10-09', description='Lunch at a restaurant')
        
        response = self.client.post(reverse('expenses:expense-edit', args=[expense.id]), {
            'category': 'Dinner',
            'amount': Decimal('30.00'),
            'date': '2024-10-10',
            'description': 'Dinner at home',
        })
        self.assertRedirects(response, reverse('expenses:expense-home'))  
        expense.refresh_from_db() 
        self.assertEqual(expense.category, 'Dinner')
        self.assertEqual(expense.amount, Decimal('30.00'))
        self.assertEqual(expense.description, 'Dinner at home')

    def test_delete_expense(self):
        """Test deleting an existing expense."""
        expense = Expense.objects.create(user=self.user, category='Lunch', amount=Decimal('50.00'), date='2024-10-09', description='Lunch at a restaurant')
        
        response = self.client.post(reverse('expenses:expense-delete', args=[expense.id]))
        self.assertRedirects(response, reverse('expenses:expense-home'))  
        self.assertEqual(Expense.objects.count(), 0) 

    def test_dashboard_view(self):
        """Test the dashboard view for expenses."""
        Expense.objects.create(user=self.user, category='Lunch', amount=Decimal('50.00'), date='2024-10-09', description='Lunch at a restaurant')
        
        response = self.client.get(reverse('expenses:dashboard'))
        self.assertEqual(response.status_code, 200) 
        total_amount = Expense.objects.filter(user=self.user).aggregate(Sum('amount'))['amount__sum']
        self.assertContains(response, total_amount) 
        self.assertContains(response, 'Lunch') 

        self.assertTemplateUsed(response, 'dashboard.html') 
