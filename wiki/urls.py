from django.urls import path
from wiki.views import PageListView, PageDetailView, PageNew


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('submit/', PageNew.as_view(), name="submit-wiki"),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
