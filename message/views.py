from django.shortcuts import render
import MySQLdb
from .models import UserMessage

# Create your views here.

def getform(request):
    message = None
    all_message = UserMessage.objects.filter(name='kaka')
    if all_message:
        message = all_message[0]

    # for message in all_message:
    #     message.delete()
    #     print(message.name)


    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     print(name)
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "hello3"
    #     user_message.save()
    return render(request, 'message_form.html', {
        "my_message": message
    })

def book_list(request):
    db = MySQLdb.connect(user='root', db='testdjango', password='ha', host='locahost')
    cursor = db.cursor()
    cursor.execute('')