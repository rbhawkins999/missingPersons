from django.urls import path
from .views import indexPageView, tablePageView, showPersonPageView

urlpatterns = [
    # path("<int:id>/", displayPersonPageView, name= "displayperson"),
    path("<int:id>/", showPersonPageView, name = "person"),
    path("table/", tablePageView, name = "table"),
    path("", indexPageView, name = "index"),
]