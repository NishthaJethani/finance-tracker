from django.shortcuts import render, redirect
from .forms import  TrackProductForm
from .models import TrackedProduct
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.

class TrackProductView(LoginRequiredMixin, View):
    template_name = 'track_product.html'
    form_class = TrackProductForm
    