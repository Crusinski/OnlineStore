from django.db import models


class Item(models.Model):
    item_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.item_text


class Price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.price_text