from django.db import models

class Post(models.Model):
    title=models.CharField('タイトル',max_length=50)
    text=models.TextField('詳細')
    thumbnail=models.ImageField('画像',upload_to='media/thumbnail')
    movie=models.FileField('動画',upload_to='uploads/%Y/%m/%d/')
    created_at=models.DateTimeField('作成日',auto_now_add=True)
    good=models.IntegerField('高評価')
    read=models.IntegerField('閲覧数')
    usertext=models.CharField(max_length=50)
    
    def __str__(self):
        return self.title