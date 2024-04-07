from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime
from .models import Customer


@shared_task
def send_birthday_greetings():
    today = datetime.today()
    customers = Customer.objects.filter(
        birth_date__month=today.month, birth_date__day=today.day
    )
    send_mail(
        "Happy Birthday from Naxa!",
        "\n\nDear Customer,\n\nWe noticed that today is your special day! "
        "Here at Naxa, we want to wish you a very happy birthday. "
        "May your day be filled with joy and happiness. "
        "\n\nBest wishes,\nNaxa Team",
        "EMAIL_HOST_USER",
        [customer.email for customer in customers],
        fail_silently=False,
    )
