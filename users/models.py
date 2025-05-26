from django.db import models
from django.contrib.auth.models import User

salary_small = "зарплата 10 000 сом"
salary_normal = "зарплата 50 000 сом"
salary_big = "зарплата 100 000 сом"

class CustomUser(User):
    GENDER = (
        ('male', 'male'),
        ('female', 'female'),
    )
    phone_number = models.CharField(max_length=18)
    experience = models.PositiveBigIntegerField(default=0)
    gender = models.CharField(max_length=100, choices=GENDER)
    salary = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.experience < 1:
            self.salary = 'должен иметься опыт работы'
        elif 1 <= self.experience < 3:
            self.salary = salary_small 
        elif 3 <= self.experience < 5:
            self.salary = salary_normal
        elif 5 <= self.experience <= 10:
            self.salary = salary_big
        else:
            self.salary = 'Ваш опыт слишком высокий, извините!'
        super().save(*args, **kwargs)

