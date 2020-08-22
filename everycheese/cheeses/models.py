from autoslug import AutoSlugField
from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel


class Cheese(TimeStampedModel):
    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"

    name = models.CharField("Name of the Cheese", max_length=255)

    slug = AutoSlugField("Cheese Address", unique=True, always_update=False, populate_from="name")

    description = models.TextField("Description", blank=True)

    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)
