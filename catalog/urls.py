from django.conf.urls import url

from . import views


urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^books/$', views.BookListView.as_view(), name='books'),
               url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
               url(r'^authors/$', views.AuthorsListView.as_view(), name='authors'),
               url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
               url(r'^genres/$', views.GenreListView.as_view(), name='genres'),
               url(r'^genre/(?P<pk>\d+)$', views.GenreDetailView.as_view(), name='genre-detail'),
               url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
               url(r'^borrowed/$', views.LoanedBooksByAllListView.as_view(), name='all-borrowed'),
               url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),]



