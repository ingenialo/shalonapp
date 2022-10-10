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

    created_at = models.DateTimeField(
        'created at',
        null=True,
        blank=True,
        auto_now_add=True,
        help_text='fecha cuando fue creado el registro.',
    )
    updated_at = models.DateTimeField(
        'updated at',
        null=True,
        blank=True,
        auto_now=True,
        help_text='fecha cuando fue actualizado el registro.',
    )

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created_at'
        ordering = ['-created_at', '-updated_at']


def update_model(model, save_update=True, **kwargs):
    """Updates the specified model instance using the keyword arguments as the model
    property attributes and values.
    Example usage:
        update_model(mymodel, save_update=True, **some_dictionary)
    """
    for attr, val in kwargs.items():
        setattr(model, attr, val)
    if save_update:
        model.save()
    return model