"""Test for profiles models."""

import pytest

from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_str():
    """Test the string representation of the Profile model."""

    user = User.objects.create_user(username="Toto", password="testpass")
    profile = Profile.objects.create(user=user, favorite_city="Cannes")
    assert str(profile) == "Toto"
