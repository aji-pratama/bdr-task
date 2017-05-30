from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import Ticket
from app.opreport.forms import TicketForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

def index_ticket(request):
    try:
        form = TicketForm()
        ticket_list = Ticket.objects.all()
        paginator = Paginator(ticket_list, 5)

        page = request.GET.get('page')
        try:
            tickets = paginator.page(page)
        except PageNotAnInteger:
            tickets = paginator.page(1)
        except EmptyPage:
            tickets = paginator.page(paginator.num_pages)

    except Ticket.DoesNotExist:
        raise Http404("Ticket Does Not Exist")
    return render(request, 'opreport/ticket/index_ticket.html', {'tickets': tickets, 'form': form})

def input_ticket(request):
    if request.POST:
        date_flight = request.POST.get('date_flight')
        om = request.POST.get('om')
        name = request.POST.get('name')
        customer = request.POST.get('customer')
        id_jobno = request.POST.get('id_jobno')
        purpose = request.POST.get('purpose')
        cost = request.POST.get('cost')
        payment = request.POST.get('payment')
        insert_data = Ticket(date_flight=date_flight, om=om, name=name,
                    customer=customer, id_jobno=id_jobno,
                    purpose=purpose, cost=cost, payment=payment)
        insert_data.save()
        messages.add_message(request, messages.INFO, 'Ticket %s telah ditambahkan' % name)
        return HttpResponseRedirect('/operation-report/input-ticket')
    form = TicketForm()
    return render(request, 'opreport/ticket/new_ticket.html', {'form':form})


def edit_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    form = TicketForm()
    if request.POST:
        date_flight = request.POST.get('date_flight')
        om = request.POST.get('om')
        name = request.POST.get('name')
        customer = request.POST.get('customer')
        id_jobno = request.POST.get('id_jobno')
        purpose = request.POST.get('purpose')
        cost = request.POST.get('cost')
        payment = request.POST.get('payment')
        ticket.date_flight = date_flight
        ticket.om = om
        ticket.name = name
        ticket.customer = customer
        ticket.id_jobno = id_jobno
        ticket.purpose = purpose
        ticket.cost = cost
        ticket.payment = payment
        ticket.save()
        messages.add_message(request, messages.INFO, 'Ticket %s telah diupdate' % name)
        return HttpResponseRedirect('/operation-report/edit-ticket-%s' % ticket.id)

    return render(request, 'opreport/ticket/edit_ticket.html', {'form':form, 'ticket':ticket})


def delete_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.delete()

    return HttpResponseRedirect('/operation-report/ticket/')












#
