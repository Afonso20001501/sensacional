from django.db import models


# Create your models here.
class Produto(models.Model):
    title = models.CharField(max_length=20)
    imagem = models.ImageField(
        upload_to="img", default='', null=False, blank=False)

    def __str__(self):
        return self.title


class Contacto(models.Model):
    nome = models.TextField()
    email = models.EmailField(max_length=50, null=False)
    address = models.CharField(max_length=50, null=False)
    address_to = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome


class Servicos(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    new_email = models.EmailField(default="", null=False)
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.new_email


class Subscriber(models.Model):
    send_mail = models.EmailField()
