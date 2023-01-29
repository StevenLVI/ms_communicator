from django.db import models
from communicator_api.adapters.models.sql.base import BaseModel

TYPE_URL = (
    ("GENERIC", "Generico"),
    ("UNIQUE", "unico")
)


class ShortUrl(BaseModel):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    hash_id = models.CharField(max_length=60, null=True)  # Hash encontrado al final del short_url -> meli.com/3aE4F
    long_url = models.CharField(max_length=250, null=False)
    short_url = models.CharField(max_length=60, null=True)
    times_clicked = models.IntegerField(default=0)
    type_url = models.CharField(choices=TYPE_URL, null=False, max_length=8)
    active = models.BooleanField(default=True)
    expiration_date = models.DateField()

    class Meta:
        db_table = "short_url"
        verbose_name = "short_url"
        verbose_name_plural = "short_urls"
        unique_together = ("id",)
