from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("gml/", views.gml, name="gml"),
    path("fcbk/", views.fcbk, name="fcbk"),
    path("insta/", views.insta, name="instgrm")
]
