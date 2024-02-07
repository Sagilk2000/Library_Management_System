from django import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .models import WishList
from .views import BookList, BookDetails, SearchResultListView, BookIssue, add_to_wishlist, wishlist,remove_from_wishlist


urlpatterns = [
    path('', BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetails.as_view(), name='book_details'),
    path('search/', SearchResultListView.as_view(), name='search_results'),
    path('issue/<int:pk>/', BookIssue.as_view(), name='issue'),
    path('wishlist/', wishlist, name='wishes'),
    path('add_to_wishlist/<int:book_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:book_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    # path('book/<int:book_id>/pdf/',views.view_book_pdf,name='view_book_pdf')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
