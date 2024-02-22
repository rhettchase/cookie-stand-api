from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import random


class CookieStand(models.Model):
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(blank=True)
    hourly_sales = models.JSONField(default=list, null=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)

    def calculate_hourly_sales(self):
        hourly_sales = []
        for _ in range(8):  # For 8 hours
            # Generate a random number of customers for this hour
            customers_this_hour = random.randint(self.minimum_customers_per_hour, self.maximum_customers_per_hour)
            # Calculate sales for this hour based on the random number of customers
            sales_this_hour = customers_this_hour * self.average_cookies_per_sale
            hourly_sales.append(int(sales_this_hour))  # Append the sales, converted to an integer
        return hourly_sales

    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('cookie_stand_detail', args=[str(self.id)])

