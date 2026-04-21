"""Test for main site URLs."""

from django.urls import reverse, resolve
from oc_lettings_site.views import index


def test_home_url():
    """Test URL resolution for the home page."""

    path = reverse("index")
    assert resolve(path).func == index
