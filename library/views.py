import os
from django.conf import settings
from .models import Book
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Book, WishList, WishListItems
# from .models import PDFFile


# Create your views here.

                

class BookList(ListView):
    model = Book  # models le table name
    template_name = 'booklist.html'


class BookDetails(DetailView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'book_details.html'
    
    
    # def view_book_pdf(request, book_id):
    #     book = get_object_or_404(Book, pk = book_id)
        
    #     pdf_path = book.pdf_file.path
        
    #     if  os.path.exists(pdf_path):
    #         with open(pdf_path, 'rb')as pdf_file:
    #             response = HttpResponse(pdf_file.read(),content_type = 'application/pdf')
    #             response['Content-Disposition']= f'inline; filename="{book.title}".pdf"'
    #             return response
        
        
        # with open(book.pdf_files.path, 'rb')as pdf_files:
        #     response = HttpResponse(pdf_files.read(),content_type = 'application,pdf')
        #     response['content-Disposition']= f'inline; filename="{book.title}".pdf"'
        #     return response


class SearchResultListView(ListView):
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(Q(title=query) | Q(author=query))


class BookIssue(DetailView):
    model = Book
    template_name = 'issue.html'


# def view_pdf(request,pdf_files):
#     pdf = PDFFile.objects.get(pk=pdf_files)
#     pdf_url = pdf.pdf_file_url
#
#     return render(request,'view_pdf.html',{'pdf_url': pdf_url,'pdf':pdf})


@login_required
def wishlist(request):
    wish_qs = WishList.objects.filter(user=request.user)
    if wish_qs.exists():
        wish_obj = wish_qs.first()
        wish_items = WishListItems.objects.filter(wishlist=wish_obj)
    else:
        wish_obj = None
        wish_items = []
    context = {
        'wishlist': wish_obj,
        'wish_items': wish_items
    }
    return render(request, 'wish/wishlist.html', context)


@login_required
def add_to_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    wish_qs = WishList.objects.filter(user=request.user)

    if wish_qs.exists():
        wish_obj = wish_qs.first()
    else:
        wish_obj = WishList.objects.create(user=request.user)

    try:
        wish_item, created = WishListItems.objects.get_or_create(book=book, wishlist=wish_obj)
        if not created:
            wish_item.quantity += 1
            wish_item.save()
    except Exception as e:
        # Handle the exception, e.g., log it or return an error response
        pass

    return redirect('wishes')  # Assuming 'wishes' is the name of your wishlist view


@login_required
def remove_from_wishlist(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    wish_qs = WishList.objects.filter(user=request.user)
    if wish_qs.exists():
        wish_obj = wish_qs.first()
        wish_item_qs = WishListItems.objects.filter(book=book, wishlist=wish_obj)
        if wish_item_qs.exists():
            wish_item = wish_item_qs.first()
            if wish_item.quantity > 1:
                wish_item.quantity -= 1
                wish_item.save()
            else:
                wish_item.delete()
        return redirect('wishes')  # Assuming 'wishes' is the name of your wishlist view


