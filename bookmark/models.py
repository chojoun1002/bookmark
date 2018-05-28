from django.db import models

# 내가 데이터베이스에 어떤 데이터를 어떻게 저장할 것인지 정의
# O.R.M(Object Relrative Management)

# Create your models here.

# Mddels.py >> Views.py >> Urls.py >> Template

# 하나의 테이블을 하나의 모델로 묘사한다.
# 모델은 항상 Class 로 구현한다.

class Bookmark(models.Model):
    # 하나의 필드를 만든다.
    # 컬럼이름 = 컬럼 종류(제약조건)
    site_name = models.CharField(max_length = 100)
    url = models.URLField('url')

    # 모델의 옵션
    class Meta:
        ordering = ['site_name']

    # 메서드
    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        from django.urls import reverse
        # http://localhost:8080/bookmark/detail/4
        # return reverse('bookmark:index', args=[str(self.id)])
        return reverse('bookmark:index')
