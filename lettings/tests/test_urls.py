"""Test for lettings URLs."""

from django.urls import reverse, resolve
from lettings.views import index, letting


def test_lettings_index_url():
    """Test URL resolution for the lettings index page."""

    path = reverse("lettings:index")
    assert resolve(path).func == index


def test_letting_detail_url():
    """Test URL resolution for the letting detail page."""

    path = reverse("lettings:letting", args=[1])
    assert resolve(path).func == letting
