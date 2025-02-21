from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()

    def __str__(self):
        return self.name
    


class Expense(models.Model):
    category=models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=6, null=True)
    amount= models.DecimalField(decimal_places=2, max_digits=10)
    description=models.TextField(null=True)
    date=models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.category.name}- {self.amount}"
