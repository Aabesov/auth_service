from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name="departments")

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SalaryIncrease(models.Model):
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   related_name="increases")
    level = models.ForeignKey(Level,
                              on_delete=models.CASCADE,
                              related_name="salary_increases")
    salary_increment = models.PositiveSmallIntegerField()
