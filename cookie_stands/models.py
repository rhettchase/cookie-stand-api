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
        # Assume business hours are 8 hours long; adjust range as needed
        hourly_sales = []
        for _ in range(14):  # Adjusted for a typical 6am to 8pm range, 14 hours
            customers_this_hour = random.randint(self.minimum_customers_per_hour, self.maximum_customers_per_hour)
            sales_this_hour = customers_this_hour * self.average_cookies_per_sale
            hourly_sales.append(int(sales_this_hour))
        return hourly_sales

    def save(self, *args, **kwargs):
        # Call calculate_hourly_sales to update hourly_sales before saving
        self.hourly_sales = self.calculate_hourly_sales()
        super(CookieStand, self).save(*args, **kwargs)  # Call the "real" save() method


    def __str__(self):
        return self.location

    def get_absolute_url(self):
        return reverse('cookie_stand_detail', args=[str(self.id)])

