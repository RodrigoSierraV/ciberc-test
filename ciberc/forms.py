# Django
from django import forms
from django.db.utils import IntegrityError

# Models
from ciberc.models import FileLoad, Inventory

# pyxlsb
from pyxlsb import open_workbook

# Python
import logging
from datetime import datetime


logger = logging.getLogger(__name__)


class UploadFileForm(forms.ModelForm):

    class Meta:
        """Form settings."""
        model = FileLoad
        fields = ('name', 'file',)

    def process_data(self):
        elements = 0
        total_price = 0
        count = 0
        wb = open_workbook(self.cleaned_data['file'].file)
        with wb.get_sheet(1) as sheet:

            for row in sheet.rows():
                if (
                    isinstance(row[0].v, str)
                    and isinstance(row[1].v, (float, int))
                    and isinstance(row[2].v, (float, int))
                ):
                    serial_number = row[0].v
                    quantity = int(row[1].v)
                    price = row[2].v
                    try:
                        Inventory.objects.create(serial_number=serial_number,
                                                 quantity=quantity,
                                                 price=price)
                        elements += quantity
                        total_price += price
                        count += 1
                    except IntegrityError:
                        Inventory.objects.filter(
                            serial_number=serial_number).update(
                                quantity=quantity, price=price)
                        elements += quantity
                        total_price += price
                        count += 1
                    except Exception as e:
                        print('EXCEPTION', str(e))
                        logger.error(
                            "{}: Row with values ({}, {}, {}) from File ({}) \
                                was not created or updated"
                            .format(datetime.now(),
                                    serial_number,
                                    quantity,
                                    price,
                                    self.cleaned_data['file']._name)
                        )
                else:
                    logger.error(
                        "{}: Row with values ({}, {}, {}) from File ({}) does \
                            not comply with data types"
                        .format(datetime.now(), row[0].v, row[1].v, row[2].v,
                                self.cleaned_data['file']._name)
                    )

        return {'elements': elements, 'average_price': total_price / count}
