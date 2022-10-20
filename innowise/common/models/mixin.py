from django.db import models


class Creatable(models.Model):
    created_date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )

    class Meta:
        abstract = True