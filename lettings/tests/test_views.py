"""Tests for the lettings views."""

import pytest
from django.urls import reverse, resolve
from lettings.models import Address, Letting


@pytest.mark.django_db
def test_lettings_index_view(client):
    """Test the lettings index view."""

    response = client.get(reverse("lettings:index"))
    assert response.status_code == 200
    assert "lettings/index.html" in [template.name for template in response.templates]


@pytest.mark.django_db
def test_letting_detail_view(client):
    """Test the letting detail view."""

    address = Address.objects.create(
        number=123,
        street="Rue de la paix",
        city="Paris",
        state="PA",
        zip_code=12345,
        country_iso_code="FRA",
    )
    letting = Letting.objects.create(title="Appartment centre-ville", address=address)
    response = client.get(reverse("lettings:letting", args=[letting.id]))
    assert response.status_code == 200
    assert "lettings/letting.html" in [template.name for template in response.templates]
    assert response.context["title"] == "Appartment centre-ville"
