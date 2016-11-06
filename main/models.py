from __future__ import unicode_literals

from django.db import models

class Event(models.Model):
	team1 = models.TextField(max_length=100)
	team2 = models.TextField(max_length=100)
	win1 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	win2 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	draw = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	#date
	def __eq__(self, other):
		#if not isinstance(other, type(self)):
		#	return False
		return ((self.team1, self.team2) == (other.team1, other.team2))

	def __str__(self):
		return '%s - %s' % (self.team1, self.team2)

	class Meta:
		managed = False

class Odds(models.Model):
	event = models.ForeignKey(Event)
	bookmaker = models.TextField(max_length=100)
	win1 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	win2 = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	draw = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	_1X = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	_X2 = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	class Meta:
		managed = False