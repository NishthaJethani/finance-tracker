from django.test import TestCase
from expenses.forms import ExpenseForm

class ExpenseFormTest(TestCase):
    def test_valid_form(self):
        # Create a valid form input
        form_data = {
            'category': 'Lunch',
            'amount': 50.00,
            'date': '2024-10-09',  # Make sure to format it correctly
            'description': 'Lunch with friends'
        }
        form = ExpenseForm(data=form_data)
        self.assertTrue(form.is_valid())  # Check that the form is valid

    def test_invalid_form_missing_fields(self):
        # Create a form input missing the amount
        form_data = {
            'category': 'Lunch',
            'date': '2024-10-09',
            'description': 'Lunch with friends'
        }
        form = ExpenseForm(data=form_data)
        self.assertFalse(form.is_valid())  # Check that the form is invalid
        self.assertIn('amount', form.errors)  # Ensure 'amount' is a part of the errors

    def test_invalid_form_invalid_amount(self):
        # Create a form input with an invalid amount
        form_data = {
            'category': 'Lunch',
            'amount': 'invalid_amount',  # Invalid input
            'date': '2024-10-09',
            'description': 'Lunch with friends'
        }
        form = ExpenseForm(data=form_data)
        self.assertFalse(form.is_valid())  # Check that the form is invalid
        self.assertIn('amount', form.errors)  # Ensure 'amount' is a part of the errors
