from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("add-auction", views.add_auction, name="add_auction"),
    path("<int:auction_id>", views.auction, name="auction"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
