from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand


class CookieStandList(LoginRequiredMixin, ListView):
    template_name = "cookie_stands/cookie_stand_list.html"
    model = CookieStand
    context_object_name = "cookie_stands"


class CookieStandDetail(LoginRequiredMixin, DetailView):
    template_name = "cookie_stands/cookie_stand_detail.html"
    model = CookieStand
    context_object_name = "cookie_stand"


class CookieStandUpdate(LoginRequiredMixin, UpdateView):
    template_name = "cookie_stands/cookie_stand_update.html"
    model = CookieStand
    fields = "__all__"


class CookieStandCreate(LoginRequiredMixin, CreateView):
    template_name = "cookie_stands/cookie_stand_create.html"
    model = CookieStand
    fields = ["location", "owner", "description", "minimum_customers_per_hour", "maximum_customers_per_hour", "average_cookies_per_sale"]


class CookieStandDelete(LoginRequiredMixin, DeleteView):
    template_name = "cookie_stands/cookie_stand_delete.html"
    model = CookieStand
    success_url = reverse_lazy("cookie_stand_list")
