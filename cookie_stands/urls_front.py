from django.urls import path
from .views_front import CookieStandList, CookieStandDetail, CookieStandCreate, CookieStandUpdate, CookieStandDelete


urlpatterns = [
    path("", CookieStandList.as_view(), name="cookie_stand_list"),
    path("<int:pk>/", CookieStandDetail.as_view(), name="cookie_stand_detail"),
    path('<int:pk>/update/', CookieStandUpdate.as_view(), name='cookie_stand_update'),
    path('create/', CookieStandCreate.as_view(), name='cookie_stand_create'),
    path('<int:pk>/delete/', CookieStandDelete.as_view(), name='cookie_stand_delete'),
]
