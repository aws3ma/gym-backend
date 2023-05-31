from django.db import models
from authentication.models import User
from bodybuilder.models import BodyBuilder
from datetime import date
# Create your models here.


class Paiement(models.Model):
    amount = models.DecimalField(max_digits=6,decimal_places=1,null=False)
    bodybuilder = models.ForeignKey(BodyBuilder, on_delete=models.CASCADE)
    start_date = models.DateField( null=False,default=date.today)
    due_date = models.DateField( null=False,default=date.today)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # paiement_date = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self) -> str:
        return self.bodybuilder.full_name+" "+str(self.amount)