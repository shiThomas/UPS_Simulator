from django.contrib import admin

# Register your models here.
from myapp.models import package, Profile, truck, survey

admin.site.register(Profile)


class packageAdmin(admin.ModelAdmin):
    list_display = ('package_id', 'destination_x','destination_y','package_status')


admin.site.register(package)


class truckAdmin(admin.ModelAdmin):
    list_display = ('truck_id', 'truck_status')



admin.site.register(truck)


class surveyAdmin(admin.ModelAdmin):
    list_display = ('package_id','satisfied')

admin.site.register(survey)
