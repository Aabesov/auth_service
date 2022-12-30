from django.contrib import admin

from company.models import Company, Department, Level, SalaryIncrease

admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Level)


class SalaryIncreaseAdmin(admin.ModelAdmin):
    model = SalaryIncrease
    list_display = ["department", "level", "salary_increment"]


admin.site.register(SalaryIncrease, SalaryIncreaseAdmin)
