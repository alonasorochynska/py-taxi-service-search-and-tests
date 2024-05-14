from django.test import TestCase

from taxi.forms import DriverCreationForm


class DriverCreationFormTests(TestCase):
    def test_driver_creation_form_with_license_number_first_last_name_is_valid(
            self
    ):
        form_data = {
            "username": "new_user",
            "password1": "test1234!",
            "password2": "test1234!",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "license_number": "ABC12345",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
