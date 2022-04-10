from django.contrib import admin

from formwizard.models import UserType

# Register your models here.
class ProfileInline(admin.StackedInline):
    model = UserType
    can_delete = False
    verbose_name_plural = 'profile'
    fk_name = 'user'

admin.site.register(UserType)