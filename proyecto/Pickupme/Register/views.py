from django.shortcuts import render, redirect

listaur = ['kike', '']
listapr = ['00', '']

def register(request):
    if request.method == 'POST':
        us = request.POST['us']
        co = request.POST['co']
        if not us in listaur:
            indexu = listaur.index(us)
            indexu = listapr.index(co)
    return render(request, 'maidxx.html')
