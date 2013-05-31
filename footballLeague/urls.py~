from django.conf.urls import patterns, include, url
from prac2.views import *
from prac2.models import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$', mainpage, name='home'),
	url(r'^representativesList/$', representativesList, name='List of Representative'),
	url(r'^playersList/$', playersList, name='List of Players'),
	url(r'^stadiumsList/$', stadiumsList, name='List of Stadiums'),
	url(r'^coachsList/$', coachsList, name='List of Coachs'),
	url(r'^teamsList/$', teamsList, name='List of Teams'),
	url(r'^leaguesList/$', leaguesList, name='List of Leagues'),
	url(r'^refereesList/$', refereesList, name='List of Referees'),
	url(r'^matchesList/$', matchesList, name='List of Matches'),

	url(r'^representative/(?P<idaux>\d+)/$', representativeModel),
	url(r'^player/(?P<idaux>\d+)/$', playerModel),
	url(r'^stadium/(?P<idaux>\d+)/$', stadiumModel),
    url(r'^coach/(?P<idaux>\d+)/$', coachModel),
	url(r'^team/(?P<idaux>\d+)/$', teamModel),
	url(r'^league/(?P<idaux>\d+)/$', leagueModel),
	url(r'^referee/(?P<idaux>\d+)/$', refereeModel),	
	url(r'^match/(?P<idaux>\d+)/$', matchModel),
#CREATE
	url(r'representative/representative_create/$' ,Create.as_view(model = Representative, form_class = RepresentativeForm, template_name = 'forms.html'), name = 'RepresentativeCreate'),
	url(r'player/player_create/$'   ,Create.as_view(model = Player, form_class = PlayerForm, template_name = 'player_forms.html'), name = 'PlayersCreate'),
	url(r'stadium/stadium_create/$' ,Create.as_view(model = Stadium, form_class = StadiumForm, template_name = 'stadium_forms.html'), name = 'StadiumCreate'),
	url(r'coach/coach_create/$' ,Create.as_view(model = Coach, form_class = CoachForm, template_name = 'forms.html'), name = 'CoachCreate'),
	url(r'team/team_create/$' ,Create.as_view(model = Team, form_class = TeamForm, template_name = 'forms.html'), name = 'TeamCreate'),
	url(r'league/league_create/$' ,Create.as_view(model = League, form_class = LeagueForm, template_name = 'forms.html'), name = 'LeagueCreate'),
	url(r'referee/referee_create/$' ,Create.as_view(model = Referee, form_class = RefereeForm, template_name = 'forms.html'), name = 'RefereeCreate'),
	url(r'match/match_create/$' ,Create.as_view(model = Match, form_class = MatchForm, template_name = 'forms.html'), name = 'MatchCreate'),
#EDIT
	url(r'representative/(?P<pk>\d+)/representative_edit/$' ,Edit.as_view(model = Representative, form_class = RepresentativeForm, 	template_name = 'forms.html')),
	url(r'player/(?P<pk>\d+)/player_edit/$'   ,Edit.as_view(model = Player, form_class = PlayerForm, template_name = 'player_forms.html')),
	url(r'stadium/(?P<pk>\d+)/stadium_edit$' ,Edit.as_view(model = Stadium, form_class = StadiumForm, 	template_name = 'stadium_forms.html')),
	url(r'coach/(?P<pk>\d+)/coach_edit/$' ,Edit.as_view(model = Coach, form_class = CoachForm, 	template_name = 'forms.html')),
	url(r'team/(?P<pk>\d+)/team_edit/$' ,Edit.as_view(model = Team, form_class = TeamForm, 	template_name = 'forms.html')),
	url(r'league/(?P<pk>\d+)/league_edit/$' ,Edit.as_view(model = League, form_class = LeagueForm, 	template_name = 'forms.html')),
	url(r'referee/(?P<pk>\d+)/referee_edit/$' ,Edit.as_view(model = Referee, form_class = RefereeForm, 	template_name = 'forms.html')),
	url(r'match/(?P<pk>\d+)/match_edit/$' ,Edit.as_view(model = Match, form_class = MatchForm, 	template_name = 'forms.html')),
#DELETE
	url(r'representative/(?P<pk>\d+)/delete$' ,Delete.as_view(success_url = '/representativesList/',model = Representative)),	
	url(r'player/(?P<pk>\d+)/delete$' ,Delete.as_view(success_url = '/playersList/',model = Player)),
	url(r'stadium/(?P<pk>\d+)/delete$' ,Delete.as_view(success_url = '/stadiumsList/',model = Stadium),  name = 'Delete'),
	url(r'coach/(?P<pk>\d+)/delete$' ,Delete.as_view(success_url = '/coachsList/',model = Coach)),	
	url(r'team/(?P<pk>\d+)/delete$' ,Delete.as_view(success_url = '/teamsList/',model = Team)),
	url(r'league/(?P<pk>\d+)/delete$' ,Delete.as_view(success_url = '/leaguesList/',model = League)),
	url(r'referee/(?P<pk>\d+)/delete$' ,Delete.as_view(success_url = '/refereesList/',model = Referee)),
	url(r'match/(?P<pk>\d+)/delete$' ,Delete.as_view(success_url = '/matchesList/',model = Match)),



	#url(r'^user/(\w+)/$', userpage),
	url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^$', 'prova.views.home', name='home'),
    # url(r'^prova/', include('prova.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
