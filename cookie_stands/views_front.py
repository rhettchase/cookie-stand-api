from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.shortcuts import render

def permission_denied_view(request, exception):
    return render(request, 'errors/403.html', status=403)


class CookieStandList(LoginRequiredMixin, ListView):
    template_name = "cookie_stands/cookie_stand_list.html"
    model = CookieStand
    context_object_name = "cookie_stands"


class CookieStandDetail(LoginRequiredMixin, DetailView):
    template_name = "cookie_stands/cookie_stand_detail.html"
    model = CookieStand
    context_object_name = "cookie_stand"
    permission_classes = [IsAuthenticated]


class CookieStandUpdate(LoginRequiredMixin, UpdateView):
    template_name = "cookie_stands/cookie_stand_update.html"
    model = CookieStand
    fields = ["location", "description", "minimum_customers_per_hour", "maximum_customers_per_hour", "average_cookies_per_sale"]

    def get_object(self, queryset=None):
        """Override get_object to check object ownership."""
        obj = super().get_object(queryset=queryset)  # Get the object
        if obj.owner != self.request.user:
            messages.error(self.request, "You do not have permission to edit this Cookie Stand.")
            raise PermissionDenied
        return obj

class CookieStandCreate(LoginRequiredMixin, CreateView):
    template_name = "cookie_stands/cookie_stand_create.html"
    model = CookieStand
    fields = ["location", "description", "minimum_customers_per_hour", "maximum_customers_per_hour", "average_cookies_per_sale"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)



class CookieStandDelete(LoginRequiredMixin, DeleteView):
    template_name = "cookie_stands/cookie_stand_delete.html"
    model = CookieStand
    success_url = reverse_lazy("cookie_stand_list")

    def get_object(self, queryset=None):
        """Override get_object to check object ownership."""
        obj = super().get_object(queryset=queryset)  # Get the object
        if obj.owner != self.request.user:
            messages.error(self.request, "You do not have permission to edit this Cookie Stand.")
            raise PermissionDenied
        return obj
