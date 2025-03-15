from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import *


def sotuv_ochirish(request, id):
    if request.user.is_authenticated:
        sotuv = get_object_or_404(Sotiv, id=id, bolim=request.user.sotuvchi.bolim)
        sotuv.delete()
        messages.success(request, "Sotuv muvaffaqiyatli o‘chirildi!")
        return redirect('sotuvlar')
    return redirect('login')


class SotuvlarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            sotuvlar = Sotiv.objects.filter(bolim=request.user.sotuvchi.bolim)
            mijozlar = Mijoz.objects.filter(bolim=request.user.sotuvchi.bolim)
            mahsulotlar = Maxsulot.objects.filter(bolim=request.user.sotuvchi.bolim)
            context = {
                'sotuvlar': sotuvlar,
                'mijozlar': mijozlar,
                "mahsulotlar": mahsulotlar,

            }
            return render(request, 'sotuvlar.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            mijoz = get_object_or_404(Mijoz, id=request.POST.get('mijoz_id'))
            mahsulot = get_object_or_404(Maxsulot, id=request.POST.get('mahsulot_id'))
            if request.POST.get("tolandi"):
                tolandi = float(request.POST.get("tolandi"))
            else:
                tolandi = None
            if request.POST.get("miqdor"):
                miqdor = float(request.POST.get("miqdor"))
            else:
                miqdor = None
            if request.POST.get("qarz"):
                qarz = float(request.POST.get("qarz"))
            else:
                qarz = None
            if request.POST.get("jami_summa"):
                jami_summa = float(request.POST.get("jami_summa"))
            else:
                jami_summa = None

            if mahsulot.miqdor < miqdor:
                context = {
                    "message": f"omborda mahsulot yetarli emas! Mavjud: {mahsulot.miqdor} {mahsulot.olchov}"
                }
                return render(request, 'error.html', context)

            if not qarz and not tolandi and not jami_summa:
                jami_summa = miqdor * mahsulot.narx2
                qarz = 0
                tolandi = jami_summa

            if not qarz and not tolandi:
                tolandi = jami_summa
                qarz = 0

            if not jami_summa and not tolandi:
                jami_summa = miqdor * mahsulot.narx2
                tolandi = jami_summa - qarz

            if not jami_summa and not qarz:
                jami_summa = miqdor * mahsulot.narx2
                qarz = jami_summa - tolandi

            if not jami_summa:
                jami_summa = miqdor * mahsulot.narx2
            else:
                jami_summa = float(jami_summa)

            if not tolandi:
                tolandi = jami_summa - qarz
            else:
                tolandi = float(tolandi)

            if not qarz:
                qarz = jami_summa - tolandi
            else:
                qarz = float(qarz)

            if jami_summa and tolandi and qarz and jami_summa != tolandi + qarz:
                context = {
                    "message": "kiritilgan qiymatlar bir biriga togri kelmaydi!"
                }
                return render(request, 'error.html', context)

            Sotiv.objects.create(
                mahsulot=mahsulot,
                mijoz=mijoz,
                miqdor=miqdor,
                jami_summa=jami_summa,
                tolandi=tolandi,
                qarz=qarz,
                bolim=request.user.sotuvchi.bolim
            )

            mijoz.qarz += qarz
            mijoz.save()

            mahsulot.miqdor -= miqdor
            mahsulot.save()
            return redirect('sotuvlar')

        return redirect('login')


class SotuvTahrorlashView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            mijozlar = Mijoz.objects.filter(bolim=request.user.sotuvchi.bolim)
            mahsulotlar = Maxsulot.objects.filter(bolim=request.user.sotuvchi.bolim)
            sotuv = get_object_or_404(Sotiv, pk=pk, bolim=request.user.sotuvchi.bolim)
            context = {
                'sotuv': sotuv,
                'mijozlar': mijozlar,
                'mahsulotlar': mahsulotlar,
            }
            return render(request, 'sotuv-tahrirlash.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:

            sotuv = get_object_or_404(Sotiv, id=pk, bolim=request.user.sotuvchi.bolim)
            mijoz = sotuv.mijoz
            yangi_qarz = float(request.POST.get("qarz", 0))
            eski_qarz = sotuv.qarz

            if yangi_qarz > eski_qarz:
                context = {"message": "Yangi qarz eski qarzdan ko'p bo'lishi mumkin emas!"}
                return render(request, 'error.html', context)


            mijoz.qarz -= (eski_qarz - yangi_qarz)


            sotuv.qarz = yangi_qarz
            sotuv.save()
            mijoz.save()

            return redirect('sotuvlar')
        return redirect('login')
