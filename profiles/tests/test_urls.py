"""Tests for the profiles URLs."""

from django.urls import reverse, resolve
from profiles.views import index, profile


def test_profiles_index_url():
    """Test URL resolution for the profiles index page."""

    path = reverse("profiles:index")
    assert resolve(path).func == index


def test_profile_detail_url():
    """Test URL resolution for the profile detail page."""

    path = reverse("profiles:profile", args=["Toto"])
    assert resolve(path).func == profile
