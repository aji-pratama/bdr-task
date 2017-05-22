from __future__ import unicode_literals

from django.shortcuts import render
from app.opreport.models import Ticket
from app.opreport.forms import TicketForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index_ticket(request):
    try:
        form = TicketForm()
        ticket_list = Ticket.objects.all()
        # if request.POST:
        #     q = request.POST.get('q')
        #     ticket_list = Ticket.objects.filter(ticket_name__contains=q)

        paginator = Paginator(ticket_list, 5) # Show 25 contacts per page

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
        return HttpResponse('')

def delete_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.delete()

    return HttpResponseRedirect('/operation-report/ticket/')












#
