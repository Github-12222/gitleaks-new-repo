from django.db import models
# Create your models here.



class Games(models.Model):
    CHOICES=(
    ('Battle Royale','battle royale'),
    ('Areans','areans'),
    ('RPG','rpg'),
    ('SC_FI','sc_fi'),
    ('Horror','horror'),
    )
    Game_Name = models.CharField(max_length=50,blank=True)
    Game_Content=models.TextField(blank=True)
    Game_Type = models.CharField(max_length=50,choices=CHOICES,default='Battle royale')
    Game_Image = models.ImageField(blank=True)
    
    
secret - cUtYmoAFFXzDFrt7MP6q2SQVeyr1I5GS6uP0brec
access - ASIAQWESQRFOAQXNS7Q7
