"""Views for the profiles application."""

import logging
from django.shortcuts import render
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """Display the list of all profiles."""

    logger.info("Afficher la liste des profils.")
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """Display details for a specific user profile.

    Args:
        request: The HTTP request object.
        username: The username of the profile.

    Returns:
        HttpResponse: Rendered profile detail page.
    """
    logger.info("Affichage du profil %s", username)
    profile_obj = Profile.objects.get(user__username=username)
    context = {"profile": profile_obj}
    return render(request, "profiles/profile.html", context)
