from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm, CommentForm
from django.contrib.auth.models import Group


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Add user to Participant group if it exists
            try:
                group = Group.objects.get(name="Participant")
                user.groups.add(group)
            except Group.DoesNotExist:
                pass

            login(request, user)  
            messages.success(request, f"Welcome, {user.username}! You have signed up successfully.")
            return redirect('ticket_list')
        else:
          
            for field in form.errors:
                for error in form.errors[field]:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def ticket_list(request):
    tickets = Ticket.objects.order_by('-created_at')
    return render(request, 'ticket_list.html', {'tickets': tickets})

def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    comment_form = CommentForm()
    
    if request.method == 'POST' and 'add_comment' in request.POST:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.ticket = ticket
            comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect('ticket_detail', pk=ticket.pk)
    
    return render(request, 'ticket_detail.html', {'ticket': ticket, 'comment_form': comment_form})

@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            messages.success(request, "Ticket created successfully.")
            return redirect('ticket_detail', pk=ticket.pk)
    else:
        form = TicketForm()
    
    return render(request, 'ticket_form.html', {'form': form})

@login_required
def ticket_resolve(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.status = 'resolved'
    ticket.save()
    messages.success(request, f"Ticket #{ticket.pk} has been resolved.")
    return redirect('ticket_detail', pk=pk)
