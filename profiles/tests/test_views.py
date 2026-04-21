"""Test for profiles views."""

from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User

import pytest


@pytest.mark.django_db
def test_profiles_index_view(client):
    """Test profile index page."""
    response = client.get(reverse("profiles:index"))
    assert response.status_code == 200
    assert "profiles/index.html" in [template.name for template in response.templates]


@pytest.mark.django_db
def test_profile_detail_view(client):
    """Test profile detail page."""
    user = User.objects.create(
        username="Toto",
        password="testpass",
        first_name="Toto",
        last_name="Titi",
        email="bastien@exemple.com",
    )
    profile = Profile.objects.create(user=user, favorite_city="Cannes")
    response = client.get(reverse("profiles:profile", args=[user.username]))
    assert response.status_code == 200
    assert "profiles/profile.html" in [template.name for template in response.templates]
    assert response.context["profile"].favorite_city == "Cannes"
