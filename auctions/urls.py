from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'commerce'
urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("<int:lol>",views.listing,name="listing"),
    path("watchlist", views.watchlist,name="watchlist"),
    path("displayCategory", views.displayCategory, name= "displayCategory"),
    path("bids/<int:id>", views.bids, name="bids"),
    path("comment/<int:postid>/", views.comment, name="comment"),
    path("archive", views.archive, name="archive"),
    path('mylisting', views.mylisting, name='mylisting')
    ]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)