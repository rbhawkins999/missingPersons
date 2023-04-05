from django.urls import path
from .views import indexPageView, tablePageView, aboutPageView

urlpatterns = [
    path("", indexPageView, name = "index"),
    path("table/", tablePageView, name = "table"),
    path("about/", aboutPageView, name = "about")
]