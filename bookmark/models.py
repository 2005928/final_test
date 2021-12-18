from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('site URL')

    def get_absolute_url(self):
        return reverse('bookmark:detail', args=[str(self.id)])

    ## __str__ 매직메서드 : 클래스의 오브젝트를 출력할 때 나타날 내용(제목)을 결정하는 메서드
    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url;