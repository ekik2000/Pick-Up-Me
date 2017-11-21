from django.shortcuts import render

def login(request):
    listau = ['kike', 'labeibe']
    listap = ['123456', '654321']
    argumento = {'notificacion': '¿Aún no estás dentro?'}
    if request.method == 'POST':
        usuario = request.POST['u']
        password = request.POST['p']
        if usuario in listau:
            indexu = listau.index(usuario)
            if password in listap and password == listap[indexu]:
                argumento = {'notificacion': '¡Bienvenido!'}
    return render(request, 'mainly.html', argumento)
