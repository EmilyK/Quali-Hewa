How to work with Models
=======================

How to work with the API; and using the Analyser,
Django provides a wonderful API
Note: this is used only with `python manage.py shell` or 
`python manage.py shell_plus`

CRUD operations

Create:

```console
>>> Analyser.object.create() # creates an empty record
```

We can store this in a variable

```console
>>> analyser = Analyser.objects.create() # our defaults be kawa, you know.
>>> analyser.save() # use the `save()` method to save the analyser
```console

Read:

```console
>>> Analyser.objects.all() # fetches all analysers
```

You can filter or pick a particular set of analysers too

```console
>>> Analyser.objects.filter(id=1) # e.g. by id or primary key (kisumulozo)
>>> Analyser.objects.filter(pk=1)
```

Or search by fields or columns

```console
>>> Analyser.objects.filter(carbonmonoxide_sensor_present=False)
```

How should we approach creation of readings (the long form algorithm), this 
is an example

```python
# get a station
from django.shortcuts import get_object_or_404
# assumption is you are looking for a station with a pk of 1 (note this changes dynamically)
station = get_object_or_404(Station, pk=1) 

# populate readings through the Station's analyser
a_reading = station.analyser.readings.create(
				carbonmonoxide_sensor_reading = 34,
				nitrogendioxide_sensor_reading = 34,
				lpg_gas_sensor_reading = 23					
				)
# save
a_reading.save()
```

If you want to in the future get the readings at a station


```python
other_station = get_object_or_404(Station, pk=2)
# getting all readings in one line
other_station.analyser.readings.all()

# please look at the django ORM API and learn to use it.
```