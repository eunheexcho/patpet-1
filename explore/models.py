from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


class Reccomendation:
    pass

class CommunicationPost(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    photo = ProcessedImageField(blank=True, upload_to='explore/post/%Y/%m/%d',
                                processors=[Thumbnail(300, 300)],
                                format='JPEG',
                                options={'queality': 60})




    def get_absolute_url(self):
        return reverse('explore:post_detail', args=[self.id])


class CommunicationComment(models.Model):
    post = models.ForeignKey(CommunicationPost, on_delete=models.CASCADE, related_name='comment_set')
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

