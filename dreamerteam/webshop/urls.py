from django.conf.urls import url
from django.contrib.auth.forms import AdminPasswordChangeForm

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^games/save/$', views.game_save, name='games_save'),
    url(r'^games/load/$', views.game_load, name='games_load'),
    url(r'^games/highscore/(?P<gameID>\d+)/$', views.game_highscore_get, name='games_highscore_get'), # get high sore
    url(r'^games/highscore/$', views.game_highscore_set, name='games_highscore_set'), #set the high score
    url(r'^games$', views.games, name='games'),
    url(r'^buy/(?P<gameID>\d+)?/?$', views.buy, name='buy'),
    url(r'^game/(?P<gameID>\d+)?/?$', views.game, name='game'),
    url(r'^dev/$', views.dev, name='dev'),
    url(r'^dev/game/(?P<gameID>\d+)/$', views.edit_game, name='edit_game'),
    url(r'^dev/game/add/', views.add_game, name='add_game'),
    url(r'^buy/success/', views.buy_success),
    url(r'^buy/cancel/', views.buy_error),
    url(r'^buy/error/', views.buy_error),
    url(r'^profile/$', views.profile, name='profile'),
    url(
        r'^accounts/password_change/$',
        'django.contrib.auth.views.password_change',
        name='password_change',
        kwargs={
               'template_name': 'registration/password_change_form.html'
               }
    ),
    url(
        r'^accounts/password_change_done/$',
        'django.contrib.auth.views.password_change_done',
        name='password_change_done',
        kwargs={'template_name': 'registration/password_change_done.html'}
    ),
    url(r'^facebook-complete/', views.facebook_complete, name='facebook_complete'),
    url(r'^profile/create/$', views.register_user_group, name='create_group'),
]
