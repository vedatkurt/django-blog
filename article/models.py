from django.db import models
from ckeditor.fields import RichTextField

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
    ]
    
class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE, verbose_name="Autor Name")
    title = models.CharField(max_length=50, verbose_name="Article Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Article Create Date")
    status = models.CharField(default="d", max_length=1, choices=STATUS_CHOICES)
    article_image = models.FileField(blank = True,null = True,verbose_name="Add Image")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
        
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE, verbose_name="comment",related_name="comments")
    comment_author = models.CharField(max_length=50, verbose_name="Isim")
    comment_content = models.CharField(max_length=200, verbose_name="comment")
    comment_date = models.DateTimeField(auto_now_add=True, verbose_name="Comment Create Date")
    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']
