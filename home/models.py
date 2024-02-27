from django.db import models

# Create your models here.
class SimpleUsers(models.Model):
    name=models.CharField(max_length=50)
    fcm_token=models.CharField(max_length=200)
    def __str__(self) -> str:
        # fcmToken=str(self.fcm_token)[:10]+...
        try:
            return self.name+' with '+self.fcm_token[:20]+ '...'
        except:
            return self.name
        
        
