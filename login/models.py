from django.db import models

# Create your models here.


class Login_user(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=254)

    class Meta:
        db_table = 'Users'

    def __str__(self):
        return f'{self.name}({self.id})'

    def getUser(username):
        try:
            return Login_user.objects.get(username=username)
        except:
            return False
