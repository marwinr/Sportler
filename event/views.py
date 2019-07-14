from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Event
from .forms import EventForm
from . import forms

# Create your views here.

def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'event/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'event/event_detail.html', {'event': event})

def event_new(request):
    if request.method == 'POST':
        form = forms.EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()            
            return redirect('event_detail', pk=event.pk)
    else:
        form = forms.EventForm()
    return render(request, 'event/event_new.html', {'form':form})

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.date = timezone.now()
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'event/event_new.html', {'form': form})