from django.db import models

# Create your models here.
class UserVo(models.Model):
    username = models.TextField(primary_key=True)
    name = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=10)
    birth = models.TextField()
    address = models.TextField()

    class Meta:
        manage = True
        db_table = 'users'

    def __str__(self):
        return f'[{self.pk}]{self.username}'

