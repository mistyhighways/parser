from __future__ import unicode_literals

from django.db import models

class Event(models.Model):
	team1 = models.TextField(max_length=100)
	team2 = models.TextField(max_length=100)
	win1 = models.TextField(max_length=15)
	win2 = models.TextField(max_length=15)
	draw = models.TextField(max_length=15)

	#date
	def __eq__(self, other):
		if not isinstance(other, type(self)):
			return False
		return ((self.team1, self.team2) == (other.team1, other.team2))

	def __str__(self):
		return '%s - %s' % (self.team1, self.team2)

# class Odds(models.Model):
