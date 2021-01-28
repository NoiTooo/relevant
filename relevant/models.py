from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Client(models.Model):
    clt_user = models.OneToOneField(User, verbose_name='相談者', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.clt_user)

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = '相談者'


class Post(models.Model):
    client = models.ForeignKey(Client, verbose_name='相談者', on_delete=models.CASCADE)
    post = models.TextField(verbose_name='相談内容')

    def __str__(self):
        return self.post[:10]

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = '相談内容'


class Adviser(models.Model):
    adv_user = models.OneToOneField(User, verbose_name='回答者', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.adv_user)

    class Meta:
        verbose_name = 'adviser'
        verbose_name_plural = '回答者'


class Answer(models.Model):
    adviser = models.ForeignKey(Adviser, verbose_name='回答者', on_delete=models.CASCADE)
    answer = models.TextField(verbose_name='回答内容')

    def __str__(self):
        return self.answer[:10]

    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = '回答内容'


class Relevant(models.Model):
    user = models.OneToOneField(User, verbose_name='ユーザー', on_delete=models.CASCADE)
    adviser = models.ManyToManyField(Adviser, related_name='adviser', blank=True, null=True)
    client = models.ManyToManyField(Client, related_name='client', blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'relevant'
        verbose_name_plural = 'コミニティ'