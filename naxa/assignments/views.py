from rest_framework import generics, status
from rest_framework.response import Response
from django.http import HttpResponse

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import json

from .tasks import send_birthday_greetings
from .models import Customer
from .serializers import CustomerSerializer


class CustomerCreateAPIView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AgeGroupDistributionAPIView(generics.ListAPIView):
    """
    API view to get the age group distribution of customers.

    This view returns the age group distribution of customers by categorizing their ages into different groups.
    It calculates the count of customers in each age group and generates a plot based on the distribution.

    Endpoint: /api/age-group-distribution/

    HTTP Methods:
        - GET: Returns the age group distribution and a plot JSON.

    Response Format:
        {
            "age_group_distribution": {
                "1-20": 10,
                "20-40": 20,
                "40+": 5
            },
            "plot_json": "<plot JSON data>"
        }
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve the age group distribution and plot JSON.

        Returns:
            A Response object containing the age group distribution and plot JSON.
        """
        queryset = self.get_queryset()
        df = pd.DataFrame(queryset.values())

        bins = [0, 20, 40, np.inf]
        labels = ["1-20", "20-40", "40+"]
        df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)

        age_distribution = df["age_group"].value_counts().to_dict()
        plot_json = get_age_group_distribution_plot(age_distribution)

        return Response(
            {
                "age_group_distribution": age_distribution,
                "plot_json": plot_json,
            },
            status=status.HTTP_200_OK,
        )


def get_age_group_distribution_plot(age_distribution):
    fig = go.Figure(
        data=[
            go.Bar(
                name="Age Distribution",
                x=list(age_distribution.keys()),
                y=list(age_distribution.values()),
            )
        ]
    )

    fig.update_layout(
        title_text="Age Distribution of Customers",
        xaxis_title="Age Group",
        yaxis_title="Count",
    )

    # fig.show()  # uncomment to show the plot in a browser

    fig_json = json.loads(fig.to_json())

    return fig_json


def send_birthday_greetings_view(request):
    send_birthday_greetings.delay()
    return HttpResponse(
        "Birthday greetings will be sent if it is any customer's birthday today."
    )
