from django.db import models
from cmsapp.models import Multiple_campaign_upload

# Create your models here.
class CampaignInfo(models.Model):
    campaign_id = models.ForeignKey(Multiple_campaign_upload,on_delete=models.CASCADE)
    info = models.TextField()

