from django.db import models


# Create your models here.
GENDER_CHOICES = (
   ('Male', 'Male'),
   ('Female', 'Female')
)

class Babysitter(models.Model):
   first_name = models.CharField(max_length=20)
   last_name = models.CharField(max_length=20)
   date_of_birth = models.DateField(max_length=20)
   nin = models.CharField(max_length=20)
   phone_number = models.CharField(max_length=20)
   email = models.CharField(max_length=20,)
   district = models.CharField(max_length=20, )
   address = models.CharField(max_length=20, )
   gender = models.CharField(choices=GENDER_CHOICES, max_length=128, name= "gender", null=True)
    
   def __str__(self):
      return self.first_name


GENDER_CHOICES = (
   ('Male', 'Male'),
   ('Female', 'Female')
)

class Baby(models.Model):
   id = models.AutoField(primary_key=True)
   first_name = models.CharField(max_length=20)
   last_name = models.CharField(max_length=20)
   date_of_birth = models.DateField(max_length=20)
   age = models.FloatField(max_length=20)
   parent_name = models.CharField(max_length=20)
   guardian_name = models.CharField(max_length=20)
   parent_phonenummber = models.CharField(max_length=20)
   guardian_phonenumber = models.CharField(max_length=20)
   gender = models.CharField(choices=GENDER_CHOICES, max_length=128, name="gender", null=True)
   
   def __str__(self):
      return f"{self.first_name} {self.last_name}"


class Procure(models.Model):
   item = models.CharField(max_length=10)
   unit_price = models.FloatField(max_length=10)
   qty = models.FloatField(max_length=10)
   date_created = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.item
   
   @property
   def Total(self):
      return self.unit_price * self.qty

class Dollsdashboard(models.Model):
   customer_name = models.CharField(max_length=20)
   dollsbought =  models.FloatField(max_length=5)
   datebought = models.DateTimeField(auto_now_add=True)
   totaldolls = models.FloatField(max_length=5 ,blank=True, null=True)

   def __str__(self):
      return self.customer_name


class Schoolfees(models.Model):
      STUDY_CHOICES = [
         ('day', 'Day'),
         ('halfday', 'Halfday')
      ]
      baby = models.ForeignKey(Baby, on_delete=models.CASCADE, blank=True, null=True) 
      type_of_payment = models.CharField(choices=STUDY_CHOICES, max_length=128, null=True)
      amount_paid = models.FloatField(max_length=5)
      date_of_payment = models.DateTimeField(auto_now_add=True)

      def __str__(self):
         return f"{self.baby.first_name}"