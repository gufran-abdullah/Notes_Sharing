from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
from .models import *


def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

def user_login(request):
	error = ""
	if request.method == 'POST':
		email = request.POST['email']
		pwd = request.POST['password']

		user = authenticate(request,username=email,password=pwd)

		try:
			if user:
				login(request,user)
				error = "no"
			else:
				error = "yes"
		except:
			error="yes"
	context = {
		"error":error
	}
	return render(request,'userlogin.html',context)

def admin_login(request):
	error = ""
	if request.method == 'POST':
		uname = request.POST['uname']
		pwd = request.POST['password']

		user = authenticate(request,username=uname,password=pwd)

		try:
			if user.is_staff:
				login(request,user)
				error = "no"
			else:
				error = "yes"
		except:
			error="yes"
	context = {
		"error":error
	}
	return render(request,'admin_login.html',context)

def user_signup(request):
	error = ""
	if request.method == "POST":
		fname = request.POST['fname']
		lname = request.POST['lname']
		uname = request.POST['email']
		pwd = request.POST['password']
		mbl = request.POST['contact']
		branch = request.POST['branch']
		role = request.POST['role']

		try:
			user = User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=pwd)
			UserSignup.objects.create(user = user,mobile=mbl,branch=branch,role=role)
			error="no"
		except:
			error="yes"
	context = {
		"error":error
	}
	return render(request,'user_signup.html',context)

def admin_home(request):
	if not request.user.is_staff:
		return redirect('admin_login')
	pending_notes = Notes.objects.filter(status = "Pending").count()
	accepted_notes = Notes.objects.filter(status = "Accepted").count()
	rejected_notes = Notes.objects.filter(status = "Rejected").count()
	all_notes = Notes.objects.all().count()
	context = {
		"pending_notes":pending_notes,
		"accepted_notes":accepted_notes,
		"rejected_notes":rejected_notes,
		"all_notes":all_notes
	}
	return render(request,'admin_home.html',context)

def persons_logout(request):
	logout(request)
	return redirect('/')	

def user_profile(request):
	if not request.user.is_authenticated:
		return redirect('user_login')

	user = User.objects.get(id=request.user.id)
	data = UserSignup.objects.get(user = user)

	context = {
		"user":user,
		"data":data
	}
	return render(request,'user_profile.html',context)

def user_changepassword(request):
	if not request.user.is_authenticated:
		return redirect('user_login')
	error=""
	if request.method == 'POST':
		crpwd = request.POST['crpassword']
		newpwd = request.POST['newpassword']
		cnpwd = request.POST['cnpassword']

		if newpwd == cnpwd:
			u = User.objects.get(username__exact=request.user.username)
			u.set_password(newpwd)
			u.save()
			error="no"
		else:
			error="yes"
	context = {
		"error":error
	}
	return render(request,'user_changepassword.html',context)

def user_editprofile(request):
	if not request.user.is_authenticated:
		return redirect('user_login')

	user = User.objects.get(id=request.user.id)
	data = UserSignup.objects.get(user = user)

	error = False
	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		contact = request.POST['contact']
		branch = request.POST['branch']

		user.first_name = fname
		user.last_name = lname
		data.mobile = contact
		data.branch = branch

		user.save()
		data.save()
		error = True

	context = {
		"user":user,
		"data":data,
		"error":error
	}
	return render(request,'user_editprofile.html',context)

def upload_notes(request):
	if not request.user.is_authenticated:
		return redirect('user_login')
	error = ""
	if request.method == "POST":
		branch = request.POST['branch']
		subject = request.POST['subject']
		notesfile = request.FILES['notesfile']
		filetype = request.POST['filetype']
		description = request.POST['description']

		user = User.objects.filter(username=request.user.username).first()
		try:
			Notes.objects.create(user=user,upload_date=date.today(),
				branch=branch,subject=subject,notesfile=notesfile,filetype=filetype,
				description=description,status='Pending')
			error="no"
		except:
			error="yes"
	context = {
		"error":error
	}
	return render(request,'upload_notes.html',context)

def user_viewnotes(request):
	if not request.user.is_authenticated:
		return redirect('user_login')

	user = User.objects.get(id=request.user.id)
	data = Notes.objects.filter(user = user)
	context = {
		"data":data
	}
	return render(request,'user_viewnotes.html',context)

def delete_notes(request,id):
	if not request.user.is_authenticated:
		return redirect('user_login')

	notes = Notes.objects.get(id=id)
	notes.delete()
	return redirect('user_viewnotes')

def view_allusers(request):
	if not request.user.is_staff:
		return redirect('admin_login')
	users = UserSignup.objects.all()
	context = {
		"users":users
	}
	return render(request,'view_allusers.html',context)

def delete_users(request,id):
	if not request.user.is_staff:
		return redirect('admin_login')

	users = UserSignup.objects.get(id=id)
	users.delete()
	return redirect('view_allusers')

def pending_notes(request):
	if not request.user.is_staff:
		return redirect('admin_login')
	user = User.objects.get(id=request.user.id)
	data = Notes.objects.filter(status = "Pending")
	context = {
		"data":data
	}
	return render(request,'pending_notes.html',context)

def change_notesstatus(request,id):
	if not request.user.is_staff:
		return redirect('admin_login')
	notes = Notes.objects.get(id=id)
	error = ""
	if request.method == 'POST':
		status = request.POST['changestatus']
		try:
			notes.status = status
			notes.save()
			error = "no"
		except:
			error = "yes"
		
	context = {
		"error":error,
		"notes":notes
	}
	return render(request,'change_notesstatus.html',context)

def accepted_notes(request):
	if not request.user.is_staff:
		return redirect('admin_login')
	user = User.objects.get(id=request.user.id)
	data = Notes.objects.filter(status = "Accepted")
	context = {
		"data":data
	}
	return render(request,'accepted_notes.html',context)

def rejected_notes(request):
	if not request.user.is_staff:
		return redirect('admin_login')
	user = User.objects.get(id=request.user.id)
	data = Notes.objects.filter(status = "Rejected")
	context = {
		"data":data
	}
	return render(request,'rejected_notes.html',context)

def all_notes(request):
	if not request.user.is_staff:
		return redirect('admin_login')
	data = Notes.objects.all()
	context = {
		"data":data
	}
	return render(request,'all_notes.html',context)

def delete_notesbyadmin(request,id):
	if not request.user.is_staff:
		return redirect('admin_login')

	notes = Notes.objects.get(id=id)
	notes.delete()
	return redirect('all_notes')

def user_viewallnotes(request):
	if not request.user.is_authenticated:
		return redirect('user_login')
	data = Notes.objects.filter(status = "Accepted")
	context = {
		"data":data
	}
	return render(request,'user_viewallnotes.html',context)