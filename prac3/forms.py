from django.forms import ModelForm	
from models	import *

class RepresentativeForm(ModelForm):	
  class	Meta:
	  model	= Representative
	  exclude = ('user', 'date',)	

class PlayerForm(ModelForm):	
  class	Meta:
	  model	= Player
	  exclude = ('user', 'date',)	

class StadiumForm(ModelForm):	
  class	Meta:
	  model	= Stadium
	  exclude = ('user', 'date',)	

class CoachForm(ModelForm):	
  class	Meta:
	  model	= Coach
	  exclude = ('user', 'date',)	

class TeamForm(ModelForm):	
  class	Meta:
	  model	= Team
	  exclude = ('user', 'date',)	

class LeagueForm(ModelForm):	
  class	Meta:
	  model	= League
	  exclude = ('user', 'date',)

class RefereeForm(ModelForm):	
  class	Meta:
	  model	= Referee
	  exclude = ('user', 'date',)	

class MatchForm(ModelForm):	
  class	Meta:
	  model	= Match
	  exclude = ('user', 'date',)		
