from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="shopIndex"),
    path("about/", views.about, name="shopAbout"),
    path("tracker/", views.tracker, name="shopTracker"),
    path("contact/", views.contact, name="contactAbout"),
    path("search/", views.search, name="Search"),
    path("checkout/", views.checkout, name="Checkout"),
    path("products/<int:myid>", views.productView, name="productShop")
]