"""Views for the lettings application."""

from django.shortcuts import render
from .models import Letting


def index(request):
    """Display the list of all lettings."""

    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """Display details for a specific letting.

    Args:
        request: The HTTP request object.
        letting_id: The ID of the letting.

    Returns:
        HttpResponse: Rendered letting detail page.
    """

    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
