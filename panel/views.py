from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .forms import panelForm
from .models import panel

# Create your views here.
# Class based or function based views
def panel_create(request):
	form = panelForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# Adding message for success or error
		messages.success(request, "Successfully Created!")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Failed to Create, make sure you type in all the required field")
	context = {
		"form": form,
	}
	return render(request, "panel_form.html", context)

def panel_detail(request,id=None):
	instance = get_object_or_404(panel, id=id)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "panel_detail.html", context)

def panel_list(request): # list items
	queryset = panel.objects.all()
	context = {
		"object_list": queryset,
		"title": "List"
	}
	return render(request, "base.html", context)

def panel_update(request, id=None):
	instance = get_object_or_404(panel, id=id)
	form = panelForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()	
		# Message success
		messages.success(request, "Successfully Updated!")
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags="html_safe")
		messages.success(request, "Summer")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "panel_form.html", context)

def panel_delete(request, id=None):
	instance = get_object_or_404(panel, id=id)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("panel:list")