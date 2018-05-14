from django.contrib import admin
from customer.models import Customer, Maid, Reserve,Money,Review
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

class MoneyAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Money._meta.fields]
admin.site.register(Money,MoneyAdmin)

class ReviewAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Review._meta.fields]
admin.site.register(Review,ReviewAdmin)
