from django.db import models

# Create your models here.

class Bills(models.Model):
    """
    creates a table in sqlite3 database
    automatically generates sql queries

    :params models.Model: what the class inherits from
    """
    name = models.CharField(max_length=55, blank=True)
    energy_supplier = models.CharField(max_length=55)
    num_of_people = models.IntegerField()
    heating_source = models.CharField(max_length=55)
    message = models.TextField(blank=True)
    impact = models.IntegerField()

    def __str__(self):
        """
        returns the class objects as a string

        :return: str 
        """
        return self.energy_supplier


class Veg(models.Model):
    """
    creates a table in sqlite3 database
    automatically generates sql queries

    :params models.Model: what the class inherits from
    """
    name = models.CharField(max_length=55, blank=True)
    current_meals = models.IntegerField()
    veggie_meals = models.CharField(max_length=55)
    co_impact = models.DecimalField(max_digits=10, decimal_places=3)
    water_impact = models.DecimalField(max_digits=10, decimal_places=3)
    waste_impact = models.DecimalField(max_digits=10, decimal_places=3)
    message = models.TextField(blank=True )

    def __str__(self):
        """
        returns the class objects as a string

        :return: str 
        """
        return self.veggie_meals
