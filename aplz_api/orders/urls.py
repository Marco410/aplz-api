from django.urls import path # type: ignore
from orders.views import HomeView, BranchView,HistoryView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("branches/", BranchView.as_view(), name="branches"),
    path("history/", HistoryView.as_view(), name="history"),
]
