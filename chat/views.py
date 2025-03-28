from django.shortcuts import render


def start_chating(request):
    return render(request,'chat/chat_page.html')


