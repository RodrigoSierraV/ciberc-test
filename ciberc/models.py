from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, FileExtensionValidator


class Inventory(models.Model):

    serial_number = models.CharField(primary_key=True,
                                     max_length=5,
                                     validators=[MinLengthValidator(5)],
                                     help_text="Must be 5 characters. \
                                        Example: SN5ab")
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                help_text='Price in Dollars')

    def __str__(self):
        """Return serial, quantiy and price."""
        return '{}: {} @ {}USD each'.format(self.serial_number,
                                            self.quantity, self.price)


class FileLoad(models.Model):

    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='uploads/',
                            validators=[FileExtensionValidator(
                                allowed_extensions=('xlsb',))])
    summary = models.CharField(max_length=100)

    def __str__(self):
        """Return file and date"""
        return "{} saved @ {}".format(self.file, self.date)
