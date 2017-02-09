try:
	from urllib import quote_plus #python 2
except:
	pass

try:
	from urllib.parse import quote_plus #python 3
except:
	pass

from django.core.mail import send_mail
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import panelForm, SignUpForm
from .models import panel

# Create your views here.
# Class based or function based views
def panel_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	if not request.user.is_authenticated():
		raise Http404
		
	form = panelForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# Adding message for success or error
		messages.success(request, "Successfully Created!")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "panel_form.html", context)

def panel_detail(request,slug=None):
	instance = get_object_or_404(panel, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.description)
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string
	}
	return render(request, "panel_detail.html", context)

def panel_list(request): # list items
	today = timezone.now().date()
	
	### This part is for signUpForm
	signUpForm = SignUpForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False) # This step allows criteria to be validated before saving
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "Anonymous"
		instance.full_name = full_name
		instance.save()
	### This part is for signUpForm
	
	queryset_list = panel.objects.active()
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = panel.objects.all()
	query = request.GET.get('q')
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(description__icontains=query)|
			Q(slug__icontains=query)|
			Q(markers__icontains=query)|
			Q(user__first_name__icontains=query)|
			Q(user__last_name__icontains=query)
		).distinct()
	paginator = Paginator(queryset_list, 25) # Show 25 queryset per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"title": "List",
		"page_request_var": page_request_var,
		"today": today,
		"signUpForm": signUpForm
	}
	return render(request, "panel_list.html", context)



def panel_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(panel, slug=slug)
	form = panelForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# Message success
		messages.success(request, "Successfully Updated!")
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags="html_safe")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "panel_form.html", context)

def panel_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(panel, slug=slug)
	instance.delete()
	messages.success(request, "Successfully Deleted!")
	return redirect("panel:list")

# def sign_up_home(request):
# 	title = "My title %s" %(request.user)
# 	form = SignUpForm()
# 	context = {
# 		"sign_up_form": form
# 	}
# 	return render(request, "panel_list.html", context)