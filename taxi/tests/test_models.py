from django.test import TestCase
from taxi.models import Manufacturer, Driver, Car


class ModelsTests(TestCase):
    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(name="Audi",
                                                   country="Germany")

        self.assertEqual(str(manufacturer),
                         f"{manufacturer.name} {manufacturer.country}")

    def test_driver_str(self):
        driver = Driver.objects.create(username="test_user",
                                       license_number="AAA00000",
                                       first_name="Test",
                                       last_name="User")

        self.assertEqual(str(driver),
                         f"{driver.first_name} {driver.last_name}: {driver.username}")

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(name="TESLA",
                                                   country="USA")
        car = Car.objects.create(model="MODEL X",
                                 manufacturer=manufacturer)

        self.assertEqual(str(car), car.model)

    def test_create_driver_as_user_with_license_number(self):
        username = "Admin"
        password = "secret-password"
        first_name = "Admin"
        last_name = "Admin"
        license_number = "AAA00000"

        driver = Driver.objects.create_user(username=username,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name,
                                            license_number=license_number)

        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.first_name, first_name)
        self.assertEqual(driver.last_name, last_name)
        self.assertEqual(driver.license_number, license_number)
