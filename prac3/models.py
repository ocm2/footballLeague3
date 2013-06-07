from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

# Create your models here.

class Representative(models.Model):
	name = models.CharField(max_length=50)
	nacionality = models.CharField(max_length=20)
	date = models.DateField(default=date.today)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('List of Representative')
	
class Player(models.Model):
	name = models.CharField(max_length=50)
	bornDate = models.DateField()
	country = models.CharField(max_length=50)
	position = models.CharField(max_length=20)
	representative = models.ForeignKey(Representative)
	date = models.DateField(default=date.today)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.name+ " - "+self.position
	def get_absolute_url(self):
		return reverse('List of Players')

class Stadium(models.Model):
	name = models.CharField(max_length=50)
	constructionYear = models.IntegerField()
	capacity = models.IntegerField()
	date = models.DateField(default=date.today)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('List of Stadiums')

class Coach(models.Model):
	name = models.CharField(max_length=50)	
        nacionality = models.CharField(max_length=50)
	age = models.IntegerField()
	date = models.DateField(default=date.today)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('List of Coachs')

class Team(models.Model):
	name = models.CharField(max_length=50)
	foundationYear = models.IntegerField()
	players = models.ManyToManyField(Player)
	stadium = models.ForeignKey(Stadium)
	coach = models.ForeignKey(Coach)
	date = models.DateField(default=date.today)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('List of Teams')


class League(models.Model):
	name = models.CharField(max_length=50)
	teams = models.ManyToManyField(Team)
	date = models.DateField(default=date.today)
	user = models.ForeignKey(User)

	def averageRating(self):
		totalsum = 0.0
		totalreviews = 0
		for review in self.leaguereview_set.all():
			totalsum += review.rating
			totalreviews += 1
		average = totalsum/totalreviews
		return average	

	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('List of Leagues')

class Referee(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	date = models.DateField(default=date.today)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('List of Referees')

class Match(models.Model):
	day = models.CharField(max_length=10) #Jornada
	numOfMatch = models.CharField(max_length=10) #numero de partit dins la jornada 
	teams = models.ManyToManyField(Team)
	result = models.CharField(max_length=5)
	stadium = models.ForeignKey(Stadium)
	referee = models.ForeignKey(Referee)
	date = models.DateField(default=date.today)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.day+" - "+ self.numOfMatch
	def get_absolute_url(self):
		return reverse('List of Matches')

class Review(models.Model):
    RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=User.objects.get(id=1))
    date = models.DateField(default=date.today)

class LeagueReview(Review):
    league = models.ForeignKey(League)
