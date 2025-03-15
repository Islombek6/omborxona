from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.utils import timezone
from .models import *
from .templatetags.custom_filters import register


def bolimlar_view(request):
    if request.user.is_authenticated:
        return render(request, "bo'limlar.html")
    return redirect('login')


def mahsulot_ochirish(request, id):
    if request.user.is_authenticated:
        mahsulot = get_object_or_404(Maxsulot, id=id, bolim=request.user.sotuvchi.bolim)
        mahsulot.delete()
        messages.success(request, "Mahsulot muvaffaqiyatli o‘chirildi!")
        return redirect('mahsulotlar')
    return redirect('login')


def mijoz_ochirish(request, id):
    if request.user.is_authenticated:
        mijoz = get_object_or_404(Mijoz, id=id, bolim=request.user.sotuvchi.bolim)
        mijoz.delete()
        messages.success(request, "Mijoz muvaffaqiyatli o‘chirildi!")
        return redirect('mijozlar')
    return redirect('login')


class MaxsulotlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mahsulotlar = Maxsulot.objects.filter(bolim=request.user.sotuvchi.bolim)
            context = {
                "mahsulotlar": mahsulotlar
            }
            return render(request, 'mahsulotlar.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Maxsulot.objects.create(
                nom=request.POST.get('nom'),
                brend=request.POST.get('brend'),
                narx1=request.POST.get('narx1'),
                narx2=None if request.POST.get('narx2') == "" else request.POST.get('narx2'),
                miqdor=request.POST.get('miqdor'),
                olchov=request.POST.get('olchov'),
                sana=request.POST.get('sana'),
                bolim=request.user.sotuvchi.bolim,
            )
            return redirect('mahsulotlar')
        return redirect('login')


class MijozlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            mijozlar = Mijoz.objects.filter(bolim=request.user.sotuvchi.bolim)
            context = {
                'mijozlar': mijozlar
            }
            return render(request, 'mijozlar.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Mijoz.objects.create(
                ism=request.POST.get('ism'),
                dokon=request.POST.get('dokon'),
                telefon=request.POST.get('telefon'),
                manzil=request.POST.get('manzil'),
                qarz=request.POST.get('qarz'),
                bolim=request.user.sotuvchi.bolim
            )
            return redirect('mijozlar')
        return redirect('login')


class MijozTahrirlashView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mijoz = get_object_or_404(Mijoz, pk=pk, bolim=request.user.sotuvchi.bolim)
            context = {
                'mijoz': mijoz
            }
            return render(request, 'mijoz-tahrirlash.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            Mijoz.objects.filter(id=pk, bolim=request.user.sotuvchi.bolim).update(
                ism=request.POST.get('ism'),
                dokon=request.POST.get('dokon'),
                manzil=request.POST.get('manzil'),
                telefon=request.POST.get('telefon'),
                qarz=request.POST.get('qarz'),
                bolim=request.user.sotuvchi.bolim
            )
            return redirect('mijozlar')
        return redirect('login')


class MaxsulotlarTaxrirlashView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            maxsulot = get_object_or_404(Maxsulot, pk=pk, bolim=request.user.sotuvchi.bolim)
            if maxsulot.sana:
                maxsulot.sana = timezone.localtime(maxsulot.sana)
            context = {
                'maxsulot': maxsulot
            }
            return render(request, 'mahsulot-tahrirlash.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            Maxsulot.objects.filter(id=pk, bolim=request.user.sotuvchi.bolim).update(
                nom=request.POST.get('nom'),
                brend=request.POST.get('brend'),
                narx1=request.POST.get('narx1'),
                narx2=None if request.POST.get('narx2') == "" else request.POST.get('narx2'),
                miqdor=request.POST.get('miqdor'),
                olchov=request.POST.get('olchov'),
                sana=request.POST.get('sana'),
                bolim=request.user.sotuvchi.bolim
            )
            return redirect('mahsulotlar')
        return redirect('login')


def error_view(request):
    if register.user.is_authenticated:
        return render(request, 'error.html')
    return redirect('login')
