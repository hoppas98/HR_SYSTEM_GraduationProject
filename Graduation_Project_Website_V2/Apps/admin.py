from django.contrib import admin
from Apps.models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(ContactUs)
admin.site.register(PostsJobs)


@admin.register(ApplicantCV)
class ApplicantsAdmin(ImportExportModelAdmin):
    pass
