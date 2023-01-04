from django.contrib import admin
from .models import Colour, Fiber, YarnType, StashEntry, Project


admin.site.register([Colour, Fiber, YarnType, StashEntry, Project])
