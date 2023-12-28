from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    # 定義資料庫
    class Meta:
        # 排序方式
        ordering = ['name']
        # 多欄位聯合索引
        indexes = [models.Index(fields=['name'])]
        # 設置models可讀名稱
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    # on_delete=CASCADE: 級聯刪除,刪除主表數據的時候從表中的數據也一起刪除
    # blank=True 可為空字符串
    # DecimalField 設定精度的十進制數字,max_digits為允許最大位數,decimal_places為小數點後位數
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/&m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    # auto_now_add=True之後修改不會更新,故用default
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        # 聯合索引
        index_together = ['id', 'slug']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
