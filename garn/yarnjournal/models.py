from django.db import models


class Colour(models.Model):
    name = models.CharField(unique=True, max_length=200)
    def __str__(self):
        return self.name

class Fiber(models.Model):
    name = models.CharField(unique=True, max_length=200)
    def __str__(self):
        return self.name

class YarnType(models.Model):
    brand = models.CharField(max_length=200)
    base = models.CharField(max_length=200)
    meterage = models.IntegerField()
    fiber = models.ForeignKey(Fiber, on_delete=models.PROTECT)

    class Meta:
        unique_together = ('brand', 'base')

    def __str__(self):
        return f"🧶 {self.brand} - {self.base} 🐑 {self.fiber} 📏 {self.meterage} m/100g"


class Project(models.Model):
    name = models.CharField(max_length=200)
    main_needle = models.FloatField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    finishing_time = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    recipient = models.CharField(max_length=200, null=True, blank=True)
    size = models.CharField(max_length=200, null=True, blank=True)
    status_options = [("planned","Planned"), ("in progress", "In progress"), ("finished", "Finished"), ("frogged", "Frogged")]
    status = models.CharField(max_length=200, choices=status_options)
    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"


class StashEntry(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    yarn = models.ForeignKey(YarnType, on_delete=models.PROTECT)
    colour = models.ForeignKey(Colour, on_delete=models.PROTECT)
    weight = models.IntegerField()
    colour_code = models.CharField(max_length=200, null=True, blank=True)
    dye_lot = models.CharField(max_length=200, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        meters = self.weight * self.yarn.meterage/100
        return f"🧶 {self.yarn.brand} - {self.yarn.base} 🌈 {self.colour} ⚖️ {self.weight} g 📏 {meters} m 📅 {self.time.date()} - {self.project} "



#pattern
#description
#picture
    
