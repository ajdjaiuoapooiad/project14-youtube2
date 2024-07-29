from django.db import models

class Post(models.Model):
    title=models.CharField('タイトル',max_length=50)
    text=models.TextField('詳細')
    thumbnail=models.ImageField('画像',upload_to='media/thumbnail/',null=True,blank=True)
    movie=models.FileField('動画',upload_to='media/uploads/%Y/%m/%d/',null=True,blank=True)
    created_at=models.DateTimeField('作成日',auto_now_add=True)
    good=models.IntegerField('高評価',default=0)
    read=models.IntegerField('閲覧数',default=0)
    usertext=models.CharField(max_length=50,default='a')
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    title=models.CharField('タイトル',max_length=30)
    text=models.TextField('本文')
    good=models.IntegerField('いいね',default=0)
    usertext=models.CharField(max_length=30,default='a')
    username=models.CharField(max_length=30,default='a')
    created_at=models.DateTimeField('日付',auto_now_add=True)
    
    def __str__(self):
        return self.title