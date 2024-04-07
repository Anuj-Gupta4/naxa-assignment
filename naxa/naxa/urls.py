from django.contrib import admin
from django.urls import path
from assignments.views import (
    CustomerCreateAPIView,
    CustomerListAPIView,
    AgeGroupDistributionAPIView,
    send_birthday_greetings_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("customer/", CustomerCreateAPIView.as_view(), name="customer_create"),
    path("customers/", CustomerListAPIView.as_view(), name="customer_list"),
    path(
        "age-group-distribution/",
        AgeGroupDistributionAPIView.as_view(),
        name="age_group_distribution",
    ),
    path(
        "send-birthday-greetings/",
        send_birthday_greetings_view,
        name="send_birthday_greetings",
    ),  #
]
