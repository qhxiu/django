from django.shortcuts import render
import MySQLdb

# Create your views here.

def getform(request):
    return render(request, 'message_form.html')

def book_list(request):
    db = MySQLdb.connect(user='root', db='testdjango', password='ha', host='locahost')
    cursor = db.cursor()
    cursor.execute('')