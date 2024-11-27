from django.db import models


NATIONALITY_CHOICES = (
    ('BRAZIL', 'BRASIL'),
    ('USA', 'ESTADOS UNIDOS'),
    ('CA', 'CANADÁ'),
    ('CN', 'CHINA'),
    ('FR', 'FRANÇA'),
    ('MX', 'MÉXICO'),
    ('ZA', 'ÁFRICA DO SUL'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=200,
        choices=NATIONALITY_CHOICES
    )

    def __str__(self):
        return self.name
