# tests/test_models.py
from django.test import TestCase
from django.contrib.auth.models import User
from expenses.models import Expense

class ExpenseModelTest(TestCase):

    def setUp(self):
        # Create a user to associate with the expense
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        # Create an expense
        self.expense = Expense.objects.create(
            user=self.user,
            category='Lunch',
            amount=50.00,
            description='Lunch with friends'
        )

    def test_expense_creation(self):
        """Test if the expense object is correctly created"""
        self.assertEqual(self.expense.user, self.user)
        self.assertEqual(self.expense.category, 'Lunch')
        self.assertEqual(self.expense.amount, 50.00)
        self.assertEqual(self.expense.description, 'Lunch with friends')
    
    def test_expense_string_representation(self):
        """Test string representation of the expense"""
        expected_str = f"{self.expense.category}: {self.expense.amount}"
        self.assertEqual(str(self.expense), expected_str)

    def test_expense_default_date(self):
        """Test if the default date is set to today"""
        import datetime
        today = datetime.date.today()
        self.assertEqual(self.expense.date.date(), today)

    def test_category_choices(self):
        """Test if the category choices are valid"""
        self.assertIn((self.expense.category, self.expense.category), Expense._meta.get_field('category').choices)
