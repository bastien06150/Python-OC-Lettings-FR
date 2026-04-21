"""Test for main site views."""

from django.urls import reverse


def test_home_view(client):
    """Test that the home page returns HTTP 200."""

    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert "index.html" in [template.name for template in response.templates]
