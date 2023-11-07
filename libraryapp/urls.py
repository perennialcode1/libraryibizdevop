"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', index, name = 'home'),
    path('', sign_in, name = 'sign_in'),
    path('add-book-issue', add_book_issue, name='add_book_issue'),
    path('book-issues-list', bookissues_list, name='bookissues_list'),
    path('book-issue-view/<int:id>', bookissue_view, name='bookissue_view'),
    path('add-member', add_member, name='add_member'),
    path('logout', logout_view, name='logout'),
    path('members-list', members_list, name='members_list'),
    path('member-view/<int:id>', member_view, name='member_view'),
    path('member-edit/<int:id>', member_edit, name='member_edit'),
    path('member-delete/<int:id>', member_delete, name='member_delete'),
    path('add-ebook', add_ebook, name='add_ebook'),
    path('books-list', books_list, name='books_list'),
    path('books-add', add_book, name='add_book'),
    path('book-view/<int:id>', book_view, name='book_view'),
    path('book-edit/<int:id>', book_edit, name='book_edit'),
    path('book-delete/<int:id>', book_delete, name='book_delete'),
    path('racks-list', racks_list, name='racks_list'),
    path('racks-add', rack_add, name='rack_add'),
    path('rack-edit', rack_edit, name='rack_edit'),
    path('rack-delete/<int:id>', rack_delete, name='rack_delete'),
    path('book-category-list', book_category_list, name='book_category_list'),
    path('book-category-add', book_category_add, name='book_category_add'),
    path('book-category-delete/<int:id>', book_category_delete, name='book_category_delete'),
    path('book-category-edit/<int:id>', book_category_edit, name='book_category_edit'),
    path('book-barcode', book_barcode, name='book_barcode'),
    path('book-names', book_name_form, name='book_name_form'),
    path('book-bulk-upload', book_bulk_upload, name='book_bulk_upload'),
    path('member-bulk-upload', member_bulk_upload, name='member_bulk_upload'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
