"""Django models utilities."""


# Django
from django.db import models
from django.utils import timezone

class CustomBaseModel(models.Model):
    """Custom basemodel.
    CustomBaseModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created_at (DateTime): Store the datetime the object was created.
        + updated_at (DateTime): Store the last datetime the object was modified.
    """