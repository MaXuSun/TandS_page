from django.db import models

# Create your models here.
class User(models.Model):
    phone = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)

    def __str__(self):
        return "name: %s, phone: %s, pwd: %s" % (self.name, self.phone, self.pwd)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    ques = models.CharField(max_length=150)
    ans = models.TextField()
    author = models.CharField(max_length=20, default="Admin")
    add = models.IntegerField(default=0)
    
    def __str__(self):
        return "id: %d, ques: %s, ans: %s, author: %s" % (self.id, self.ques, self.ans, self.author)