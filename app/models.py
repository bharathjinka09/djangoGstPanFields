from django.conf import settings
from django.db.models import ForeignKey, CASCADE, Model
from gst_field.modelfields import GSTField, PANField


class Tax(Model):
    user = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    gstin = GSTField()
    pan = PANField()

    def __str__(self):
        return f"{user}-{gstin}-{pan}"
