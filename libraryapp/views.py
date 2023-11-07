from django.shortcuts import redirect, render
from .decorators import session_required
from django.contrib.auth import logout
from django.utils import timezone
from datetime import timedelta
from .models import *
import barcode
from barcode.writer import ImageWriter
import os
import pandas as pd
from django.contrib import messages

# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        entered_password = request.POST.get('password')
        try:
            user_obj = Users.objects.get(username = uname)
            if entered_password == user_obj.password:
                request.session['email'] = user_obj.email
                return redirect('home')
            else:
                return redirect('sign_in')
        except:
            print('except')
            return redirect('sign_in')
            
    return render(request, 'sign-in.html')

@session_required
def index(request):
    m_count = Member.objects.all().count()
    u_count = Users.objects.all().count()
    bi_count = Bookissue.objects.all().count()
    b_count = Book.objects.all().count()
    context={
        'm_count':m_count,
        'u_count':u_count,
        'bi_count':bi_count,
        'b_count':b_count,
    }
    return render(request, 'home.html', context)

@session_required
def add_book_issue(request):
    email = request.session.get('email')
    user_obj = Users.objects.get(email = email)
    template_name = 'add-book-issue.html'
    members_obj = Member.objects.all()
    book_obj = Book.objects.all()
    bookno_obj = Bookissue.objects.all()
    book_config = Libraryconfigure.objects.get(roleid = user_obj.roleid)
    context = {
        'member': members_obj,
        'book': book_obj,
        'bookno': bookno_obj
    }
    if request.method == 'POST':
        current_time = timezone.now()
        print(current_time)
        member = request.POST.get('member')
        book = request.POST.get('book')
        bookno = request.POST.get('bookno')
        issuedate = request.POST.get('issuedate')
        notes = request.POST.get('notes')
        bookid = Book.objects.get(bookid = book)
        expirydate  = current_time + timedelta(days = book_config.per_renew_limit_day)
        Bookissue.objects.create(
            roleid = user_obj.roleid,
            memberid = Member.objects.get(memberid=member),
            bookcategoryid = bookid.bookcategoryid,
            bookid = book,
            bookno = bookno,
            notes = notes,
            issue_date = issuedate,
            create_date = current_time,
            create_memberid = 1,
            create_roleid = user_obj.roleid,
            book_fine_per_day = book_config.book_fine_per_day,
            fineamount = 0,
            paymentamount = 0,
            discountamount = 0,
            paidstatus = 0,
            status = 0,
            deleted_at = 0,
            modify_date = current_time,
            modify_memberid = 1,
            modify_roleid = user_obj.roleid,
            max_renewed_limit = book_config.max_renewed_limit,
            expire_date = expirydate,
            renewed = book_config.max_renewed_limit,
            orgid = user_obj.orgid,
            member_foreign_id = 0,
            mfk = 0
        )
    return render(request, template_name, context)

@session_required
def bookissues_list(request):
    template_name = 'bookissues-list.html'
    data = Bookissue.objects.all()
    
    context = {
        'data': data
    }
    return render(request, template_name, context)

@session_required
def bookissue_view(request, id):
    template_name = 'view-bookissue.html'
    bookissue_obj = Bookissue.objects.get(bookissueid = id)
    # member_obj = Member.objects.get(memberid = bookissue_obj.memberid)
    book_obj = Book.objects.get(bookid = bookissue_obj.bookid)
    book_renew_obj = Bookissue.objects.filter(memberid = bookissue_obj.memberid)
    context = {
        'data': bookissue_obj,
        # 'member': member_obj,
        'book': book_obj,
        'book_renew': book_renew_obj,
    }
    print(context)
    return render(request, template_name, context)

@session_required
def add_member(request):
    email = request.session.get('email')
    user_obj = Users.objects.get(email = email)
    print('fun call')
    if request.method == 'POST':
        current_time = timezone.now()
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        membertype = request.POST.get('membertype')
        status = request.POST.get('status')
        joindate = request.POST.get('joindate')
        photo = request.FILES['photo']
        address = request.POST.get('address')
        a = Member.objects.create(
            create_memberid = 1,
            photo = photo,
            create_roleid = user_obj.roleid,
            modify_date = current_time,
            modify_roleid = user_obj.roleid,
            create_date = current_time,
            roleid = 3, 
            name = name,
            status = status,
            address = address,
            dateofbirth = dob,
            gender = gender,
            email = email,
            phone = phone,
            modify_memberid = membertype,
            sample_pwd = '1234',
            joinningdate = joindate,
            orgid = user_obj.orgid,
            membertype=membertype
        )
        # Member_Images.objects.create(memberid = a, image = photo)
    return render(request, 'add-member.html')
 
@session_required
def members_list(request):
    template_name = 'members-list.html'
    data = Member.objects.all()
    context = {
        'data': data
    }
    return render(request, template_name, context)

@session_required
def member_view(request, id):
    template_name = 'view-member.html'
    member_obj = Member.objects.get(memberid = id)
    # member_img_obj = Member.objects.get(bimgid = member_obj.memberid)
    book_issue_obj = Bookissue.objects.filter(memberid = id)
    context = {
        'user_data': member_obj,
        'book_data': book_issue_obj,
        # 'member_img': member_img_obj
    }
    return render(request, template_name, context)

@session_required
def member_edit(request, id):
    user_obj = Member.objects.get(memberid = id)
    template_name = 'edit-member.html'
    context = {
        'user_data': user_obj,
    }
    if request.method == 'POST':
        current_time = timezone.now()
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        membertype = request.POST.get('membertype')
        status = request.POST.get('status')
        joindate = request.POST.get('joindate')
        photo = request.FILES['photo']
        address = request.POST.get('address')

        # Updating edited values
        if photo is not None:
            user_obj.photo = photo

        user_obj.modify_date = current_time
        user_obj.name = name
        user_obj.dateofbirth = dob
        user_obj.gender = gender
        user_obj.email = email
        user_obj.phone = phone
        user_obj.memberid = membertype
        user_obj.status = status
        user_obj.joinningdate = joindate
        user_obj.address = address
        user_obj.photo = user_obj.photo
        user_obj.save()
    return render(request, template_name, context)

@session_required
def member_delete(request, id):
    mem_obj = Member.objects.get(memberid=id)
    mem_obj.status = 1
    mem_obj.save()
    return redirect('members_list')

@session_required
def add_ebook(request):
    template_name = 'add-ebook.html'
    email = request.session.get('email')
    user_obj = Users.objects.get(email = email)
    if request.method == 'POST':
        current_time = timezone.now()
        name = request.POST.get('bname')
        author = request.POST.get('author')
        cover_photo = request.FILES['cphoto']
        file = request.FILES['ffile']
        notes = request.POST.get('notes')
        Ebook.objects.create(name = name,
            author= author,
            coverphoto = cover_photo,
            notes = notes,
            file = file,
            create_date = current_time,
            create_memberid = 1,
            create_roleid = user_obj.roleid,
            modify_date = current_time,
            modify_memberid = 1,
            modify_roleid = user_obj.roleid,
            orgid = user_obj.orgid
        )
    return render(request, template_name)

@session_required
def books_list(request):
    template_name = 'books-list.html'
    data = Book.objects.filter(status = 0)
    context = {
        'data': data
    }
    return render(request, template_name, context)

@session_required
def add_book(request):
    template_name = 'add-book.html'
    email = request.session.get('email')
    user_obj = Users.objects.get(email = email)
    if request.method == 'POST':
        current_time = timezone.now()
        bname = request.POST.get('bname')
        author = request.POST.get('author')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        codeno = request.POST.get('codeno')
        bookcategory = request.POST.get('bookcategory')
        isbn = request.POST.get('isbn')
        rack = request.POST.get('rack')
        photo = request.FILES['photo']
        editionnumber = request.POST.get('editionnumber')
        editiondate = request.POST.get('editiondate')
        publisheddate = request.POST.get('publisheddate')
        publisher = request.POST.get('publisher')
        notes = request.POST.get('notes')
        Book.objects.create(
            name = bname,
            author = author,
            bookcategoryid = bookcategory,
            quantity = quantity,
            price = price,
            isbnno = isbn,
            coverphoto = photo,
            codeno = codeno,
            rackid = rack,
            editionnumber = editionnumber,
            editiondate = editiondate,
            publisher = publisher,
            publisheddate = publisheddate,
            notes = notes,
            status = 0,
            deleted_at = 0,
            create_date = current_time,
            create_memberid = 1,
            create_roleid = user_obj.roleid,
            modify_date = current_time,
            modify_memberid = 1,
            modify_roleid = user_obj.roleid,
            orgid = user_obj.orgid
        )
    return render(request, template_name)

@session_required
def book_view(request, id):
    template_name = 'view-book.html'
    book_obj = Book.objects.get(bookid = id)
    context = {
        'book': book_obj
    }
    return render(request, template_name, context)

@session_required
def book_edit(request, id):
    template_name = 'edit-book.html'
    book_obj = Book.objects.get(bookid = id)
    context = {
        'book': book_obj
    }
    if request.method == 'POST':
        current_time = timezone.now()
        bname = request.POST.get('bname')
        author = request.POST.get('author')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        codeno = request.POST.get('codeno')
        bookcategory = request.POST.get('bookcategory')
        isbn = request.POST.get('isbn')
        rack = request.POST.get('rack')
        photo = request.FILES['photo']
        editionnumber = request.POST.get('editionnumber')
        editiondate = request.POST.get('editiondate')
        publisheddate = request.POST.get('publisheddate')
        publisher = request.POST.get('publisher')
        notes = request.POST.get('notes')

        book_obj.name = bname
        book_obj.author = author
        book_obj.quantity = quantity
        book_obj.price = price
        book_obj.codeno = codeno
        book_obj.bookcategoryid = bookcategory
        book_obj.isbnno = isbn
        book_obj.rackid = rack
        if photo:
            book_obj.coverphoto = photo
        book_obj.editionnumber = editionnumber
        book_obj.editiondate = editiondate
        book_obj.publisheddate = publisheddate
        book_obj.publisher = publisher
        book_obj.notes = notes
        book_obj.save()
        book_obj = Book.objects.get(bookid = id)
        context = {
        'book': book_obj
        }
    return render(request, template_name, context)

@session_required
def book_delete(request, id):
    book_obj = Book.objects.get(bookid = id)
    book_obj.status = 1
    book_obj.save()
    return redirect('books_list')

@session_required
def racks_list(request):
    template_name = 'racks-list.html'
    data = Rack.objects.all()
    context = {
        'data': data
    }
    return render(request, template_name, context)

@session_required
def rack_add(request):
    email = request.session.get('email')
    user_obj = Users.objects.get(email = email)
    if request.method == 'POST':
        current_time = timezone.now()
        name = request.POST.get('rackNmae')
        desc = request.POST.get('rackDesc')
        Rack.objects.create(
            name = name,
            description = desc,
            create_date = current_time,
            create_memberid = 1,
            modify_roleid = user_obj.roleid,
            modify_memberid = 1,
            modify_date = current_time,
            create_roleid = user_obj.roleid,
            orgid = user_obj.orgid
        )
    return redirect('racks_list')

@session_required
def rack_edit(request):
    email = request.session.get('email')
    user_obj = Users.objects.get(email = email)
    if request.method == 'POST':
        id = request.POST.get('rackId')
        print(id)
        rack_obj = Rack.objects.get(rackid = id)
        current_time = timezone.now()
        name = request.POST.get('rackName')
        desc = request.POST.get('rackDesc')
        # Updating rack_object
        rack_obj.name = name
        rack_obj.description = desc
        rack_obj.create_date = current_time
        rack_obj.create_memberid = user_obj.memberid
        rack_obj.modify_date = current_time
        rack_obj.create_roleid = user_obj.roleid
        rack_obj.modify_memberid = user_obj.memberid
        rack_obj.modify_roleid = user_obj.roleid
        rack_obj.save()

    return redirect('racks_list')

@session_required
def rack_delete(request, id):
    rack_obj = Rack.objects.get(rackid = id)
    rack_obj.isactive = 0
    rack_obj.save()
    return redirect('racks_list')

@session_required
def book_category_list(request):
    template_name = 'book-category-list.html'
    data = Bookcategory.objects.all()
    context = {
        'data': data
    }
    return render(request, template_name, context)

@session_required
def book_category_add(request):
    email = request.session.get('email')
    user_obj = Users.objects.get(email = email)
    if request.method == 'POST':
        current_time = timezone.now()
        name = request.POST.get('bookNmae')
        photo = request.FILES['photo']
        desc = request.POST.get('bookDesc')
        status = request.POST.get('status')
        Bookcategory.objects.create(
        name = name,
        description = desc,
        coverphoto = photo,
        status=status,
        create_date = current_time,
        create_memberid = 1,
        modify_roleid = user_obj.roleid,
        modify_memberid = 1, 
        modify_date = current_time, 
        create_roleid = user_obj.roleid,
        orgid = user_obj.orgid
        )
    return redirect('book_category_list')

@session_required
def book_category_delete(request, id):
    bcat_obj = Bookcategory.objects.get(bookcategoryid = id)
    bcat_obj.status = 0
    return redirect('book_category_list')

@session_required
def book_category_edit(request, id):
    template_name = 'edit-book-category.html'
    book_cat_obj = Bookcategory.objects.get(bookcategoryid = id)
    context = {
        'bco': book_cat_obj
    }
    if request.method == 'POST':
        bcname = request.POST.get('bcname')
        description = request.POST.get('description')
        status = request.POST.get('status')
        photo = request.FILES.get('photo')
        if photo is not None:
            book_cat_obj.coverphoto = photo
        book_cat_obj.name = bcname
        book_cat_obj.description = description
        book_cat_obj.status = status
        book_cat_obj.save()
        book_cat_obj = Bookcategory.objects.get(bookcategoryid = id)
        context = {
            'bco': book_cat_obj
        }
    return render(request, template_name, context)

@session_required
def book_barcode(request):
    template_name = 'book-barcode.html'
    email = request.session.get('email')
    user_obj = Users.objects.get(email = email)
    book_cat_obj = Bookcategory.objects.all()
    context = {
        'bcategory': book_cat_obj,
    }
    if request.method == 'POST':
        bname = request.POST.get('bname')
        text = request.POST.get('prefix')
        book_item_obj = Book.objects.get(bookid=bname)
        barcodes = []
        books_count = Bookitem.objects.filter(bookid = bname).count()
        no_of_generate_barcodes = book_item_obj.quantity - books_count
        print(no_of_generate_barcodes, 'no_of_generate_barcodes')
        label_text_obj = Bookitem.objects.filter(bookid=bname)
        print(label_text_obj, 'label_text_obj')

        for j in range(books_count):
            if no_of_generate_barcodes == 0:
                if not os.path.exists('barcodes'):
                    os.makedirs('barcodes')
                if label_text_obj is not None:
                    barcodes = []
                    count = 0
                    for i in label_text_obj:
                        count += 1
                        if i is not None:
                            if i.label is None:
                                # Generate the barcode using python-barcode
                                code = barcode.get_barcode_class('code128')
                                ean = code(text+str(count), writer=ImageWriter())
                                barcode_file = ean.save(f'media/barcodes/barcode{i}')
                                barcodes.append(barcode_file)
                                i.label = text+str(count)
                                i.save()
                            else:
                                # Generate the barcode using python-barcode
                                code = barcode.get_barcode_class('code128')
                                ean = code(i.label, writer=ImageWriter())
                                barcode_file = ean.save(f'media/barcodes/barcode{i}')
                                barcodes.append(barcode_file)
            else:
                print('else')
                barcodes = []
                for i in range(1, no_of_generate_barcodes + 1):
                    if not os.path.exists('barcodes'):
                        os.makedirs('barcodes')
                    # for i in range(1, num_barcodes + 1):
                    barcode_text = text
                    barcode_text += str(i)
                    Bookitem.objects.create(
                        bookid = bname,
                        bookno  =  0,
                        status = 0,
                        deleted_at = 1,
                        label = barcode_text,
                        orgid = user_obj.orgid
                    )
                    label_text_obj = Bookitem.objects.filter(bookid = bname)
                    for i in label_text_obj:
                    # Generate the barcode using python-barcode
                        code = barcode.get_barcode_class('code128')
                        ean = code(i.label, writer=ImageWriter())
                        barcode_file = ean.save(f'media/barcodes/barcode{i}')
                        barcodes.append(barcode_file)
        context={
            'barcodes': barcodes,
            'bcategory': book_cat_obj,
        }
    return render(request, template_name, context)

@session_required
def book_name_form(request):
    template_name = 'book-barcode.html'
    book_cat_obj = Bookcategory.objects.all()
    context = {
        'bcategory': book_cat_obj,
    }
    # if request.method == 'POST':
    bcategory = request.POST.get("bcategory")
    book_name_obj = Book.objects.filter(bookcategoryid = bcategory)
    context={
        'bnames':book_name_obj,
        'bcategory': book_cat_obj,
    }
    return render(request, template_name, context)

@session_required
def book_bulk_upload(request):
    template_name = 'book-bulk-uploades.html'
    current_time = timezone.now()
    email = request.session.get('email')
    user_obj = Users.objects.get(email=email)
    book_category_data = Bookcategory.objects.all()
    context = {
        'bcat': book_category_data
    }
    if request.method == 'POST':
        bcat = request.POST.get('bcat')
        book_file = request.FILES['bookfile']
        if book_file.name.endswith(('.xlsx', '.xls', '.csv')):
            try:
                df = pd.read_excel(book_file, engine='openpyxl')
                for index, row in df.iterrows():
                    data = {
                        'name': row['Book Name'],
                        'author': row['Author'],
                        'quantity': row['Quantity'],
                        'price': row['Price'] if not pd.isna(row['Price']) else 0.0,  # Handle missing values
                        'isbnno': row['ISBN Number'],
                        'codeno': row['Code Number'],
                        'editionnumber': row['Edition Number'],
                        'editiondate': row['Edition Date'],
                        'publisher': row['Publisher Name'],
                        'publisheddate': row['Published Date'],
                        'notes': row['Notes'],
                        'status': 1,
                        'bookcategoryid': bcat,
                        'deleted_at': 0,
                        'create_date': current_time,
                        'create_memberid': 0,
                        'create_roleid': user_obj.roleid,
                        'modify_date': current_time,
                        'modify_memberid': 0,
                        'modify_roleid': user_obj.roleid,
                        'orgid': user_obj.orgid
                    }
                    try:
                        rack = Rack.objects.get(name=row['Rack Name'])
                        data['rackid'] = rack.rackid
                    except Rack.DoesNotExist:
                        print(f"Rack with name {row['Rack Name']} not found.")
                    Book.objects.create(**data)
                print("Data inserted successfully.")
            except Exception as e:
                print(f"Error: {str(e)}")
        else:
            print("Invalid file format. Please upload an .xlsx, .xls, or .csv file.")

    return render(request, template_name, context)

@session_required
def member_bulk_upload(request):
    template_name = 'member-bulk-uploades.html'
    current_time = timezone.now()
    email = request.session.get('email')
    user_obj = Users.objects.get(email=email)
    if request.method == 'POST':
        book_file = request.FILES['memberfile']
        if book_file.name.endswith(('.xlsx', '.xls', '.csv')):
            try:
                df = pd.read_excel(book_file, engine='openpyxl')
                for index, row in df.iterrows():
                    data = {
                        'name': row['Member Name'],
                        'dateofbirth': row['Date of Birth'],
                        'gender': row['Gender'],
                        'email': row['Email'],  # Handle missing values
                        'phone': row['Phone'],
                        'address': row['Address'],
                        'joinningdate': row['Joining Date'],
                        'roleid':0,
                        'status':1,
                        'create_date':current_time,
                        'create_memberid':0,
                        'create_roleid':user_obj.roleid,
                        'modify_date':current_time,
                        'modify_memberid':0,
                        'modify_roleid':user_obj.roleid,
                        'orgid': user_obj.orgid
                    }
                    print(data['dateofbirth'])
                    try:
                        member_type = Membertype.objects.get(role = row['Member Type'])
                        data['membertype'] = member_type.membertypeid
                    except Membertype.DoesNotExist:
                        print(f"Member Type with name {row['Member Type']} not found.")
                    print(data)
                    Member.objects.create(**data)
                    print("Data inserted successfully.")
            except Exception as e:
                print(f"Error: {str(e)}")
        else:
            print("Invalid file format. Please upload an .xlsx, .xls, or .csv file.")

    return render(request, template_name)

@session_required
def logout_view(request):
    logout(request)
    return redirect('sign_in')