"""Testfor the lettings models."""

import pytest

from lettings.models import Address, Letting


@pytest.mark.django_db
def test_address_str():
    """Test the string representation of the Address model."""

    address = Address.objects.create(
        number=123,
        street="Rue de la paix",
        city="Paris",
        state="PA",
        zip_code=12345,
        country_iso_code="FRA",
    )
    assert str(address) == "123 Rue de la paix"


@pytest.mark.django_db
def test_address_verbose_name():
    """Test the verbose name of the Address model."""

    assert Address._meta.verbose_name == "Address"
    assert Address._meta.verbose_name_plural == "Addresses"


@pytest.mark.django_db
def test_letting_verbose_name():
    """Test the verbose name of the Letting model."""

    assert Letting._meta.verbose_name == "letting"
    assert Letting._meta.verbose_name_plural == "lettings"


@pytest.mark.django_db
def test_letting_str():
    """Test the string representation of the Letting model."""

    address = Address.objects.create(
        number=123,
        street="Rue de la paix",
        city="Paris",
        state="PA",
        zip_code=12345,
        country_iso_code="FRA",
    )
    letting = Letting.objects.create(title="Appartment centre-ville", address=address)
    assert str(letting) == "Appartment centre-ville"
