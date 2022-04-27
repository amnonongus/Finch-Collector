from django.db import models
from django.urls import reverse

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.IntegerField()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})

WALKS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('N', 'Night')
)



class Walk(models.Model):
    date = models.DateField('Walk Date')
    time = models.CharField(
        max_length=1,
        choices=WALKS,
        default=WALKS[0][0]
    )

    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}, for {self.dog.name}"

    class Meta:
        ordering = ['-date']