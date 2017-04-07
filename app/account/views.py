from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

from app.karyawan.models import Akun, Karyawan


def index(request):
    return render(request, 'index.html')

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    return render(request, 'account/dashboard.html')

def login(request):
	# if request.POST:
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # username = request.POST.get('username')
        # password = request.POST.get('password')
		# user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
				try:
					# akun = Akun.objects.get(akun=user.id)
					login(request, user)
#BUG: didieu
					request.session['karyawan_id'] = akun.karyawan.id
					request.session['jenis_akun'] = akun.jenis_akun
					request.session['username'] = request.POST['username']
				except:
					messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data karyawan, silahkan hubungi administrator')
				return redirect('/dashboard')
            else:
				messages.add_message(request, messages.INFO, 'User belum terverifikasi')
        else:
			messages.add_message(request, messages.INFO, 'Username atau password Anda salah')

    return render(request, 'account/login.html')

def logout(request):
	logout(request)
	return redirect('/')

#DOING: Login
# def login(request):
#     if request.POST:
#         return HttpResponse("yesss this is login")
#     return render(request, 'account/login.html')
