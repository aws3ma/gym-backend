from django.db import models
from authentication.models import User
# Create your models here.


class BodyBuilder(models.Model):
    full_name = models.TextField(max_length=150,null=False)
    phone = models.TextField(max_length=8,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self) -> str:
        return self.full_name