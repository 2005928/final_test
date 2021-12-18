from django.contrib import admin
from .models import Bookmark ##models.py 파일에서 정의한 bookmark를 가져다 쓰겠다

# Register your models here.
admin.site.register(Bookmark)