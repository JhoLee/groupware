from django.contrib import admin


class MyAdminSite(admin.AdminSite):
    site_title = 'Groupware admin'
    site_header = 'Groupware administration'


admin_site = MyAdminSite(name='myadmin')