"""Views for the profiles application."""

from django.shortcuts import render
from .models import Profile


def index(request):
    """Display the list of all profiles."""

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

    profile_obj = Profile.objects.get(user__username=username)
    context = {"profile": profile_obj}
    return render(request, "profiles/profile.html", context)
