from django.shortcuts import render, redirect
from django.http import HttpResponse
from ticketlist.models import Ticket,Status,Damage,Devicemodel,Device,Devicedamage
from ticketlist.forms import AddDevice, AddTicket, AddDamage, DeleteDamage

# Create your views here.

def ticketindex(request):
    username = str(request.user)
    if username == 'admin':
        tickets_list = Ticket.objects.order_by('-data_utworzenia')
    else:
        usergroup = str(request.user.groups.all()[0])
        tickets_list = Ticket.objects.order_by('-data_utworzenia').filter(firma=usergroup)
        
    date_dickt = {'tickets':tickets_list}

    form = AddTicket()
    date_dickt['form']=form
    #print("tak")

    if request.method == 'POST':
        form = AddTicket(request.POST)
        #print("tak2")

        if form.is_valid():
            #obj.YOUR_FILE_FIELD = obj.get_upload_file_name(request.user, filename)
            obj = form.save(commit=False)
            obj.uzytkownik = str(request.user)
            #print(obj.uzytkownik,str(request.user),str(request.user.groups.all()[0].name))
            #print("tak3")
            obj.firma = str(request.user.groups.all()[0].name)
            obj = form.save()
            return redirect('/tickets/'+str(obj.id))

    return render(request,'ticketlist/list.html',context=date_dickt)

def ticketdetails(request, ticket_id):
    #print(ticket_id)
    ticket_dtls = Ticket.objects.filter(id=ticket_id)
    one_ticket_dict = {'ticket':ticket_dtls}
    devices_to_tckt = Device.objects.filter(ticket=ticket_id).order_by('serialnumber')
    one_ticket_dict['device'] = devices_to_tckt
    damage_to_ticket = Devicedamage.objects.prefetch_related('damagedpart', 'device').order_by('damagedpart__damagetype')
    #print(one_device_id)
    one_ticket_dict['damage'] = damage_to_ticket

    form = AddDevice()
    one_ticket_dict['deviceform'] = form

    damageform = AddDamage()
    one_ticket_dict['damageform'] = damageform
    
    if request.method == 'POST':
        form = AddDevice(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.ticket_id = ticket_id
            obj = form.save()
            return redirect('/tickets/'+str(ticket_id))
        else:
            form = AddDamage(request.POST)

            if form.is_valid():
                one_device_id = Device.objects.filter(ticket=ticket_id).values_list('id', flat=True)[0]
                obj = form.save(commit=False)
                obj.ticket_id = ticket_id
                obj.device_id = one_device_id
                obj = form.save()
                return redirect('/tickets/'+str(ticket_id))

    
    return render(request,'ticketlist/detail.html',context=one_ticket_dict)

def deletedamage(request):
    if request.method == 'POST':
        #form = AddDamage()
        #damages = Devicedamage.objects.all()
        damageid = int(request.POST.get('damage_id'))
        ticketid = Devicedamage.objects.filter(id=damageid).values_list('ticket_id', flat=True)[0]
        #print(str(ticketid))
        damage = Devicedamage.objects.get(id=damageid)
        damage.delete()
        return redirect('/tickets/'+str(ticketid))