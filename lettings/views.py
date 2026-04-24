"""Views for the lettings application."""

import logging
from django.shortcuts import render
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """Display the list of all lettings."""

    lettings_list = Letting.objects.all()
    logger.info("Affichage de la liste des lettings.")
    logger.error("Ceci est une erreur de test pour le logging.")
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
    logger.info("Affichage des détails pour le letting id=%s.", letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
