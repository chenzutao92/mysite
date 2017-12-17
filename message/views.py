from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from message.models import Message


@login_required
def message(request):
    user = request.user
    unread_messages = Message.objects.filter(owner=user,status=1)
    return render(request, "message/message.html",{"unread_messages":unread_messages})


def read(request, msg_id):
    msg_id = int(msg_id)
    user = request.user
    link = Message.objects.filter(owner=user,id=msg_id).values("link")
    links = link[0]['link']
    m = Message.objects.get(owner=user,id=msg_id)
    m.status = 0
    m.save()
    return redirect(links)