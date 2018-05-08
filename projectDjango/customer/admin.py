from django.contrib import admin
from customer.models import Customer, Maid, Reserve
from django.contrib import admin


# Register your models here.
class MaidAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Maid._meta.fields]
admin.site.register(Maid,MaidAdmin)

class CustomerAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Customer._meta.fields]
admin.site.register(Customer,CustomerAdmin)

class ReserveAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Reserve._meta.fields]
	list_editable=('cost','reserve_date')
admin.site.register(Reserve,ReserveAdmin)

