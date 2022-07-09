from django.test import TestCase

from taxi.forms import DriverCreateForm, DriverUpdateForm


class FormsDriverTests(TestCase):
    def test_driver_creation_form(self):
        form_data = {"username": "admin",
                     "password": "secret-password",
                     "first_name": "Admin",
                     "last_name": "Test",
                     "email": "example@gmail.com",
                     "license_number": "DDD12345"}
        form = DriverCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_validate_license(self):
        form_items = {"username": "admin",
                      "password": "secret-password",
                      "first_name": "Admin",
                      "last_name": "Test",
                      "email": "example@gmail.com",
                      "license_number": "DDD123456"}
        len_license = DriverCreateForm(data=form_items)
        self.assertFalse(len_license.is_valid())

        form_items["license_number"] = "DDD1234"
        len_license = DriverCreateForm(data=form_items)
        self.assertFalse(len_license.is_valid())

        form_items["license_number"] = "32112345"
        license_letters = DriverCreateForm(data=form_items)
        self.assertFalse(license_letters.is_valid())

        form_items["license_number"] = "ddd12345"
        license_letters = DriverCreateForm(data=form_items)
        self.assertFalse(license_letters.is_valid())

        license_digits = DriverCreateForm(data=form_items)
        self.assertFalse(license_digits.is_valid())

    def test_driver_license_update_form(self):
        form_items = {"first_name": "Admin",
                      "last_name": "Test",
                      "email": "example@gmail.com",
                      "license_number": "DDD12345"}
        form = DriverUpdateForm(data=form_items)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_items)

        form_items["license_number"] = "DDD123456"
        len_license = DriverUpdateForm(data=form_items)
        self.assertFalse(len_license.is_valid())

        form_items["license_number"] = "DDD1234"
        len_license = DriverUpdateForm(data=form_items)
        self.assertFalse(len_license.is_valid())

        form_items["license_number"] = "32112345"
        license_letters = DriverUpdateForm(data=form_items)
        self.assertFalse(license_letters.is_valid())

        form_items["license_number"] = "bbb12345"
        license_letters = DriverUpdateForm(data=form_items)
        self.assertFalse(license_letters.is_valid())

        form_items["license_number"] = "DDDABCDE"
        license_digits = DriverCreateForm(data=form_items)
        self.assertFalse(license_digits.is_valid())
