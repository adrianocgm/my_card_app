from django.db import models
import uuid

class Client(models.Model):
    id = models.UUIDField(primary_key = True,
                          default = uuid.uuid4,
                          editable = False)
    card_number = models.CharField(max_length=19, null=False)
    issue_date = models.DateField(max_length=10, null=False)
    expiration_date = models.DateField(max_length=10)
    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=60)
    client_since =  models.DateField(max_length=10)
    client_phone = models.CharField(max_length=11, null=True)
    client_email = models.EmailField(null=True)
    