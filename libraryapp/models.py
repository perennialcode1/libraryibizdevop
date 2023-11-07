# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Organization(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    orgid = models.IntegerField(db_column='OrgId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    createdon = models.DateTimeField(db_column='CreatedOn')  # Field name made lowercase.
    licensekey = models.CharField(db_column='LicenseKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organization'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Book(models.Model):
    bookid = models.AutoField(db_column='bookID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    bookcategoryid = models.IntegerField(db_column='bookcategoryID')  # Field name made lowercase.
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbnno = models.CharField(max_length=100)
    coverphoto = models.FileField(upload_to='Book Coverphoto')
    codeno = models.CharField(max_length=100)
    rackid = models.IntegerField(db_column='rackID', blank=True, null=True)  # Field name made lowercase.
    editionnumber = models.CharField(max_length=100)
    editiondate = models.DateTimeField(blank=True, null=True)
    publisher = models.CharField(max_length=100)
    publisheddate = models.DateTimeField(blank=True, null=True)
    notes = models.TextField()
    status = models.IntegerField()
    deleted_at = models.IntegerField()
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'book'


class Bookcategory(models.Model):
    bookcategoryid = models.AutoField(db_column='bookcategoryID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    description = models.TextField()
    coverphoto = models.FileField(upload_to='Bookcategory Coverphoto')
    status = models.IntegerField()
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bookcategory'


class Bookissue(models.Model):
    bookissueid = models.AutoField(db_column='bookissueID', primary_key=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleID')  # Field name made lowercase.
    memberid = models.ForeignKey('Member', models.DO_NOTHING, db_column='memberID', blank=True, null=True)  # Field name made lowercase.
    bookcategoryid = models.IntegerField(db_column='bookcategoryID')  # Field name made lowercase.
    bookid = models.PositiveIntegerField(blank=True, null=True)
    bookno = models.IntegerField()
    notes = models.CharField(max_length=255)
    issue_date = models.DateTimeField()
    expire_date = models.DateTimeField()
    renewed = models.IntegerField()
    max_renewed_limit = models.IntegerField()
    book_fine_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    fineamount = models.DecimalField(max_digits=10, decimal_places=2)
    paymentamount = models.DecimalField(max_digits=10, decimal_places=2)
    discountamount = models.DecimalField(max_digits=10, decimal_places=2)
    paidstatus = models.IntegerField()
    status = models.IntegerField()
    deleted_at = models.IntegerField()
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.
    member_foreign_id = models.IntegerField()
    mfk = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bookissue'


class Bookitem(models.Model):
    bookitemid = models.AutoField(db_column='bookitemID', primary_key=True)  # Field name made lowercase.
    bookid = models.IntegerField(db_column='bookID')  # Field name made lowercase.
    bookno = models.IntegerField()
    status = models.IntegerField()
    deleted_at = models.IntegerField()
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.
    label = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookitem'


class Bulkimport(models.Model):
    bulkimportid = models.AutoField(db_column='bulkimportID', primary_key=True)  # Field name made lowercase.
    file = models.CharField(max_length=200)
    file_name = models.CharField(max_length=255)
    module = models.IntegerField()
    status = models.IntegerField()
    create_date = models.DateField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bulkimport'


class Chat(models.Model):
    chatid = models.AutoField(db_column='chatID', primary_key=True)  # Field name made lowercase.
    message = models.TextField()
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chat'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ebook(models.Model):
    ebookid = models.AutoField(db_column='ebookID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    coverphoto = models.FileField(upload_to='Ebook Coverphoto')
    file = models.FileField(upload_to='Ebook File')
    file_original_name = models.CharField(max_length=200)
    notes = models.TextField()
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ebook'


class Emailsend(models.Model):
    emailsendid = models.AutoField(db_column='emailsendID', primary_key=True)  # Field name made lowercase.
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sender_name = models.TextField()
    email = models.CharField(max_length=255, blank=True, null=True)
    sender_memberid = models.IntegerField(db_column='sender_memberID')  # Field name made lowercase.
    sender_roleid = models.IntegerField(db_column='sender_roleID')  # Field name made lowercase.
    emailtemplateid = models.IntegerField(db_column='emailtemplateID')  # Field name made lowercase.
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    on_deleted = models.IntegerField()
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emailsend'


class Emailsetting(models.Model):
    optionkey = models.CharField(unique=True, max_length=100)
    optionvalue = models.TextField()
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emailsetting'


class Emailtemplate(models.Model):
    emailtemplateid = models.AutoField(db_column='emailtemplateID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=60)
    template = models.TextField()
    priority = models.IntegerField()
    status = models.IntegerField()
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'emailtemplate'


class Expense(models.Model):
    expenseid = models.AutoField(db_column='expenseID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.CharField(max_length=200, blank=True, null=True)
    fileoriginalname = models.CharField(max_length=200, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'expense'


class Finehistory(models.Model):
    finehistoryid = models.AutoField(db_column='finehistoryID', primary_key=True)  # Field name made lowercase.
    bookissueid = models.IntegerField(db_column='bookissueID')  # Field name made lowercase.
    bookstatusid = models.IntegerField(db_column='bookstatusID')  # Field name made lowercase.
    renewed = models.IntegerField()
    from_date = models.DateTimeField(blank=True, null=True)
    to_date = models.DateTimeField(blank=True, null=True)
    fineamount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'finehistory'


class Generalsetting(models.Model):
    optionkey = models.CharField(unique=True, max_length=100)
    optionvalue = models.CharField(max_length=250, blank=True, null=True)
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'generalsetting'


class Income(models.Model):
    incomeid = models.AutoField(db_column='incomeID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.CharField(max_length=200, blank=True, null=True)
    fileoriginalname = models.CharField(max_length=200, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'income'


class Libraryconfigure(models.Model):
    libraryconfigureid = models.AutoField(db_column='libraryconfigureID', primary_key=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleID')  # Field name made lowercase.
    max_issue_book = models.IntegerField()
    max_renewed_limit = models.IntegerField()
    per_renew_limit_day = models.IntegerField()
    book_fine_per_day = models.DecimalField(max_digits=11, decimal_places=0)
    issue_off_limit_amount = models.DecimalField(max_digits=11, decimal_places=0)
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'libraryconfigure'


class Member(models.Model):
    memberid = models.AutoField(db_column='memberID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=60)
    dateofbirth = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=15, blank=True, null=True)
    religion = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=15)
    bloodgroup = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    joinningdate = models.DateTimeField(blank=True, null=True)
    photo = models.FileField(upload_to='Member Photos')
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=128)
    roleid = models.IntegerField(db_column='roleID')  # Field name made lowercase.
    status = models.IntegerField()
    deleted_at = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.
    sample_pwd = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member'


class Menu(models.Model):
    menuid = models.AutoField(db_column='menuID', primary_key=True)  # Field name made lowercase.
    menuname = models.CharField(max_length=128)
    menulink = models.CharField(max_length=128)
    menuicon = models.CharField(max_length=128, blank=True, null=True)
    priority = models.IntegerField()
    parentmenuid = models.IntegerField(db_column='parentmenuID')  # Field name made lowercase.
    status = models.IntegerField()
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu'


class Newsletter(models.Model):
    newsletterid = models.AutoField(db_column='newsletterID', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=200)
    verify = models.IntegerField()
    created_at = models.DateTimeField()
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'newsletter'


class Orderitems(models.Model):
    orderitemid = models.BigAutoField(db_column='orderitemID', primary_key=True)  # Field name made lowercase.
    orderid = models.PositiveBigIntegerField(db_column='orderID')  # Field name made lowercase.
    storebookid = models.PositiveBigIntegerField(db_column='storebookID')  # Field name made lowercase.
    quantity = models.PositiveIntegerField()
    unit_price = models.FloatField()
    subtotal = models.FloatField()
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderitems'


class Orders(models.Model):
    orderid = models.BigAutoField(db_column='orderID', primary_key=True)  # Field name made lowercase.
    memberid = models.PositiveBigIntegerField(db_column='memberID')  # Field name made lowercase.
    name = models.CharField(max_length=191, db_collation='utf8mb4_unicode_ci')
    address = models.TextField(db_collation='utf8mb4_unicode_ci')
    mobile = models.CharField(max_length=191, db_collation='utf8mb4_unicode_ci')
    email = models.CharField(max_length=255, db_collation='utf8mb4_unicode_ci')
    delivery_charge = models.FloatField()
    subtotal = models.FloatField()
    total = models.FloatField()
    payment_status = models.PositiveIntegerField()
    payment_method = models.PositiveIntegerField()
    paid_amount = models.FloatField()
    discounted_price = models.FloatField()
    misc = models.TextField(db_collation='utf8mb4_unicode_ci', blank=True, null=True)
    status = models.PositiveIntegerField()
    notes = models.TextField(db_collation='utf8mb4_unicode_ci')
    create_date = models.DateTimeField(blank=True, null=True)
    modify_date = models.DateTimeField(blank=True, null=True)
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Paymentanddiscount(models.Model):
    paymentanddiscountid = models.AutoField(db_column='paymentanddiscountID', primary_key=True)  # Field name made lowercase.
    bookissueid = models.IntegerField(db_column='bookissueID')  # Field name made lowercase.
    paymentamount = models.DecimalField(max_digits=10, decimal_places=2)
    discountamount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=255)
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paymentanddiscount'


class Permissionlog(models.Model):
    permissionlogid = models.AutoField(db_column='permissionlogID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=60, db_collation='utf8mb3_unicode_ci')
    description = models.CharField(max_length=255, db_collation='utf8mb3_unicode_ci')
    active = models.CharField(max_length=3, db_collation='utf8mb3_unicode_ci')
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permissionlog'


class Permissions(models.Model):
    permissionlogid = models.IntegerField(db_column='permissionlogID')  # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permissions'


class Rack(models.Model):
    rackid = models.AutoField(db_column='rackID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    description = models.TextField()
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'rack'


class Requestbook(models.Model):
    requestbookid = models.AutoField(db_column='requestbookID', primary_key=True)  # Field name made lowercase.
    memberid = models.IntegerField(db_column='memberID')  # Field name made lowercase.
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    coverphoto = models.CharField(max_length=200)
    bookcategoryid = models.IntegerField(db_column='bookcategoryID')  # Field name made lowercase.
    isbnno = models.CharField(max_length=100, blank=True, null=True)
    editionnumber = models.CharField(max_length=50, blank=True, null=True)
    editiondate = models.DateField(blank=True, null=True)
    publisher = models.CharField(max_length=50, blank=True, null=True)
    publisheddate = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    deleted_at = models.IntegerField()
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'requestbook'


class Resetpassword(models.Model):
    resetpasswordid = models.AutoField(db_column='resetpasswordID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    code = models.CharField(max_length=11)
    memberid = models.IntegerField(db_column='memberID')  # Field name made lowercase.
    roleid = models.IntegerField(db_column='roleID')  # Field name made lowercase.
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField()
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resetpassword'


class Role(models.Model):
    roleid = models.AutoField(db_column='roleID', primary_key=True)  # Field name made lowercase.
    role = models.CharField(max_length=30)
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    modify_roleid = models.IntegerField(db_column='modify_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role'


class Storebook(models.Model):
    storebookid = models.AutoField(db_column='storebookID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    storebookcategoryid = models.IntegerField(db_column='storebookcategoryID')  # Field name made lowercase.
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbnno = models.CharField(max_length=100)
    coverphoto = models.CharField(max_length=200)
    codeno = models.CharField(max_length=100)
    editionnumber = models.CharField(max_length=100)
    editiondate = models.DateTimeField(blank=True, null=True)
    publisher = models.CharField(max_length=100)
    publisheddate = models.DateTimeField(blank=True, null=True)
    notes = models.TextField()
    description = models.TextField()
    status = models.IntegerField()
    deleted_at = models.IntegerField()
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'storebook'


class Storebookcategory(models.Model):
    storebookcategoryid = models.AutoField(db_column='storebookcategoryID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    description = models.TextField()
    coverphoto = models.CharField(max_length=255)
    status = models.IntegerField()
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    modify_date = models.DateTimeField()
    modify_memberid = models.IntegerField(db_column='modify_memberID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'storebookcategory'


class Storebookimage(models.Model):
    storebookimageid = models.AutoField(db_column='storebookimageID', primary_key=True)  # Field name made lowercase.
    storebookid = models.IntegerField(db_column='storebookID')  # Field name made lowercase.
    file_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)
    meta = models.TextField()
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'storebookimage'


class Updates(models.Model):
    updateid = models.AutoField(db_column='updateID', primary_key=True)  # Field name made lowercase.
    version = models.CharField(max_length=20)
    date = models.DateField()
    memberid = models.IntegerField(db_column='memberID')  # Field name made lowercase.
    status = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    orgid = models.IntegerField(db_column='orgID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'updates'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=60)
    phone = models.CharField(max_length=15, blank=True, null=True)
    joiningdate = models.DateTimeField()
    username = models.CharField(max_length=60, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)
    roleid = models.IntegerField(db_column='roleID')  # Field name made lowercase.
    create_date = models.DateTimeField()
    create_memberid = models.IntegerField(db_column='create_memberID')  # Field name made lowercase.
    create_roleid = models.IntegerField(db_column='create_roleID')  # Field name made lowercase.
    orgid = models.IntegerField(db_column='orgID')  # Field name made lowercase.
    isactive = models.TextField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'users'
