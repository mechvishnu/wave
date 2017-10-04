from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Port(models.Model):
    port_name=models.CharField(max_length=50 ,unique=True)
    port_code=models.CharField(max_length=20)
    country=models.CharField(max_length=20)

    def __str__(self):
        return self.port_name


class Vessel(models.Model):
    vessel_name=models.CharField(max_length=50,unique=True)
    vessel_type=models.CharField(max_length=50)
    nrt=models.CharField(max_length=50)
    imo=models.CharField(max_length=50)
    dwt=models.CharField(max_length=50)
    grt=models.CharField(max_length=50)
    loa=models.CharField(max_length=50)
    registered=models.CharField(max_length=50)
    displacement=models.CharField(max_length=50)
    bow_thruster=models.CharField(max_length=50)

    def __str__(self):
        return self.vessel_name

class Principal(models.Model):
     principal_name=models.CharField(max_length=50,unique=True)
     email=models.EmailField()
     email_ops=models.EmailField()
     email_da=models.EmailField()
     attention=models.CharField(max_length=50)
     address=models.CharField(max_length=50)
     country=models.CharField(max_length=50)
     state_province=models.CharField(max_length=50)
     city=models.CharField(max_length=50)
     pincode=models.CharField(max_length=50)
     customer_ops_comments=models.CharField(max_length=50)
     customer_da_comments=models.CharField(max_length=50)
     phone=models.CharField(max_length=50)
     fax=models.CharField(max_length=50)

     def __str__(self):
         return self.principal_name


class Ticket(models.Model):
      appointment_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
      my_name=models.ForeignKey(User)
      principal=models.ForeignKey(Principal)
      port=models.ForeignKey(Port)
      last_port=models.CharField(max_length=50)
      next_port=models.CharField(max_length=50)
      vessel_name=models.ForeignKey(Vessel)
      appointment_type=models.CharField(max_length=50)
      master_name=models.CharField(max_length=50)
      voyage_no=models.CharField(max_length=50)
      imo=models.CharField(max_length=50)
      nominator=models.CharField(max_length=50)
      charterer=models.CharField(max_length=50)
      call_purpose=models.CharField(max_length=50)

      def __str__(self):
          return str(self.appointment_id)
