from django.contrib import admin
from admissions.models import Students_info as Students


class To_table_display(admin.ModelAdmin):
    pass



# Register your models here.
admin.site.register(Students, To_table_display)

