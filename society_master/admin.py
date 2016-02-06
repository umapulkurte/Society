from django import forms
from django.contrib import admin
from .models import Lane,Shop,Owner,Body_Member,CollectionType,MaintenanceType,Meeting
# Register your models here.

class LaneAdmin(admin.ModelAdmin):
	list_display = ["Lane_No","Lane_Name"]
	class meta:
		model = Lane

class ShopAdmin(admin.ModelAdmin):
	list_display = ["Lane_Name","Shop_Name","Shop_Owner"]
	class meta:
		model = Shop

class OwnerAdmin(admin.ModelAdmin):
	list_display = ["Owner_Name","Email_id","Gender"]
	class meta:
		model = Owner

class Body_MemberAdmin(admin.ModelAdmin):
	list_display = ["Member","Designation","Contact_no"]
	class meta:
		model = Body_Member

class CollectionTypeAdmin(admin.ModelAdmin):
	list_display = ["collection_type","Pay_type","Amount"]
	class meta:
		model = CollectionType

class  MaintenanceTypeAdmin(admin.ModelAdmin):
	list_display = ["maintenance_type","Amount"]
	class meta:
		model = MaintenanceType

class MeetingForm(forms.ModelForm):
	
	class Meta:
		model = Meeting
		exclude = ['Time']
class MeetingsAdmin(admin.ModelAdmin):
	exclude = ['Date']
	form = MeetingForm

admin.site.register(Lane,LaneAdmin)
admin.site.register(Shop,ShopAdmin)
admin.site.register(Owner,OwnerAdmin)
admin.site.register(Body_Member,Body_MemberAdmin)
admin.site.register(CollectionType,CollectionTypeAdmin)
admin.site.register(MaintenanceType,MaintenanceTypeAdmin)
admin.site.register(Meeting,MeetingsAdmin)