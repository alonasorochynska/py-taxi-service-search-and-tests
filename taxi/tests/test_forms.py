from django.test import TestCase

from taxi.forms import DriverCreationForm, DriverSearchForm, CarSearchForm, ManufacturerSearchForm


class DriverCreationFormTests(TestCase):

    def setUp(self):
        self.valid_form_data = {
            "username": "test_user",
            "password1": "test1234!",
            "password2": "test1234!",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "license_number": "ABC12345",
        }

    def get_form(self, **kwargs):
        form_data = self.valid_form_data.copy()
        form_data.update(kwargs)
        return DriverCreationForm(data=form_data)

    def test_driver_creation_form(self):
        form = DriverCreationForm(data=self.valid_form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, self.valid_form_data)

    def test_clean_license_number_valid(self):
        form = self.get_form(license_number="ABC12345")
        self.assertTrue(form.is_valid())

    def test_clean_license_number_invalid(self):
        form = self.get_form(license_number="abc")
        self.assertFalse(form.is_valid())
        self.assertIn("license_number", form.errors)


class SearchFormsTests(TestCase):

    def test_driver_search_form_valid(self):
        form_data = {"username": "test_username"}
        form = DriverSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "test_username")

    def test_driver_search_form_empty(self):
        form_data = {"username": ""}
        form = DriverSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "")

    def test_car_search_form_valid(self):
        form_data = {"model": "test_model"}
        form = CarSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["model"], "test_model")

    def test_car_search_form_empty(self):
        form_data = {"model": ""}
        form = CarSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["model"], "")

    def test_manufacturer_search_form_valid(self):
        form_data = {"name": "test_name"}
        form = ManufacturerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "test_name")

    def test_manufacturer_search_form_empty(self):
        form_data = {"name": ""}
        form = ManufacturerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "")
