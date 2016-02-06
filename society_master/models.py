from django.db import models

# Create your models here.
class Lane(models.Model):
	Lane_No = models.CharField(max_length=50,blank=False,null=False)
	Lane_Name = models.CharField(max_length=50,blank=False,null=False)

	def __unicode__(self):
		return self.Lane_Name

class Shop(models.Model):
	Lane_Name = models.ForeignKey(Lane,verbose_name='Select Lane')
	Shop_No = models.CharField(max_length=120,blank=False,null=False)
	Shop_Name = models.CharField(max_length=120,blank=False,null=False)
	Shop_Owner = models.CharField(max_length=120,blank=False,null=False)
	Mobile_No = models.IntegerField(blank=False,null=False)

	def __unicode__(self):
		return self.Shop_Name

class Owner(models.Model):
	Gender_Choices = (
    ('F', 'Female'),
    ('M', 'Male'),
	)
	Blood_choices = (
		('A','A'),
		('B','B'),
		('A+','A+'),
		('B+','B+'),
		('O','O'),
		('O+','O+'),
		('AB','AB'),
		('AB+','AB+'),
	)
	vehicle_choices = (
		('','Two Wheeler'),
		('','Four_wheeler'),
	)
	watertank_choices = (
		('','Underground'),
		('','Overhead'),
	)
	Date = models.DateField()
	Owner_Name = models.CharField(max_length=120,blank=False,null=False)
	Gender = models.CharField(max_length=1,choices=Gender_Choices)
	Blood_group = models.CharField(max_length=3,choices=Blood_choices)
	DOB = models.DateField()
	Phone_No = models.IntegerField(blank=False,null=False)
	Age = models.IntegerField(blank=False,null=False)
	Education = models.CharField(max_length=120)
	Email_id = models.EmailField()
	Profession = models.CharField(max_length=120)

	def __unicode__(self):
		return self.Owner_Name

class Body_Member(models.Model):
	designation_choices = (
		('SH','Society Head'),
	)
	Member = models.ForeignKey(Owner)
	Designation = models.CharField(max_length=120,choices=designation_choices)
	Contact_no = models.IntegerField()
	Email_id = models.EmailField()

	def __unicode__(self):
		return unicode(self.Member)

class CollectionType(models.Model):
	pay_choice = (
		('Annually','Annually'),
		('Monthly','Monthly'),
	)
	collection_type = models.CharField(max_length=150,blank=False,null=False)
	Pay_type = models.CharField(max_length=120,choices=pay_choice,blank=False,null=False)
	Amount = models.IntegerField()

	def __unicode__(self):
		return unicode(self.collection_type)

class MaintenanceType(models.Model):
	maintenance_type = models.CharField(max_length=150,blank=False,null=False)
	Amount = models.IntegerField(blank=False,null=False)

	def __unicode__(self):
		return unicode(self.maintenance_type)

class Meeting(models.Model):
	Date = models.DateField()
	Time = models.TimeField()
	Subject = models.CharField(max_length=200)
	Minute_reports = models.TextField(help_text="Feedback in Metting")

	def __unicode__(self):
		return unicode(self.Subject)