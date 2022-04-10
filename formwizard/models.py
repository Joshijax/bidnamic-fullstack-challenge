from django.db import models
from django.contrib.auth.models import  User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.
BIDDING_OPTIONS =(
    ("High", "High"),
    ("Medium", "Medium"),
    ("Low", "Low"),
)


class UserType(models.Model): #user onetoonefield for profile
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    dob = models.DateTimeField(
                   null=True, blank=True,
                   verbose_name=u'Fecha')
    bid_settings = models.CharField(max_length=100)
    googleId = models.CharField(max_length=100)

    
    # url = models.URLField("Website", blank=True)
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

@receiver(post_save, sender= settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        UserType.objects.create(user=instance)