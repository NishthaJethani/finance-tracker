# expenses/test_expenses/test_urls.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from expenses.views import ExpenseCreateView, ExpenseListView, ExpenseUpdateView, ExpenseDeleteView, DashboardView

class UrlsTest(SimpleTestCase):

    def test_expense_home_url_resolves(self):
        url = reverse('expenses:expense-home')
        self.assertEqual(resolve(url).func.view_class, ExpenseListView)

    def test_expense_create_url_resolves(self):
        url = reverse('expenses:expense-create')
        self.assertEqual(resolve(url).func.view_class, ExpenseCreateView)

    def test_expense_edit_url_resolves(self):
        url = reverse('expenses:expense-edit', args=[1])  # Assuming 1 is a valid expense ID
        self.assertEqual(resolve(url).func.view_class, ExpenseUpdateView)

    def test_expense_delete_url_resolves(self):
        url = reverse('expenses:expense-delete', args=[1])  # Assuming 1 is a valid expense ID
        self.assertEqual(resolve(url).func.view_class, ExpenseDeleteView)

    def test_dashboard_url_resolves(self):
        url = reverse('expenses:dashboard')
        self.assertEqual(resolve(url).func.view_class, DashboardView)
