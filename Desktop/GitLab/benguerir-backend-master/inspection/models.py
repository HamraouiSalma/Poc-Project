from django.db import models
from account.models import Profile


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        abstract = True

STATUS = (
    (0,"In Progress"),
    (1,"Published"),
    (2,"Validated"),
    (3,"Planned"),
)

class Inspection(BaseModel):
    title = models.CharField(max_length=200, unique=True)
    inspection_tag = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(Profile, on_delete= models.CASCADE,related_name='inspections')
    content = models.TextField()
    img = models.ImageField(upload_to="./inspection_img")
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title


class Comment(BaseModel):
    inspection = models.ForeignKey(Inspection,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    #email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


