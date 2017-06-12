from django.shortcuts import render

# Create your views here.
from ..forms import ClienteForm
from ..models.Cliente import Cliente

def inicio(request):
    form = ClienteForm(request.POST or None)  # campos obligatorios
    # print (dir(form)) para saber comandos en cmd
    if form.is_valid():
        form_data = form.cleaned_data
        aba = form_data.get("nombre_cliente")
        abb = form_data.get("apellidos_cliente")
        abc = form_data.get("direccion_cliente")
        abd = form_data.get("telefono_cliente")
        abe = form_data.get("tipodoc_cliente")
        abf = form_data.get("numdoc_cliente")
        abg = form_data.get("email_cliente")
        abh = form_data.get("genero_cliente")
        abi = form_data.get("fechasuscripcion_cliente")
        obj = Cliente.objects.create(nombre_cliente=aba, apellidos_cliente=abb, direccion_cliente=abc, telefono_cliente=abd,
                                     tipodoc_cliente=abe, numdoc_cliente=abf, email_cliente=abg, genero_cliente=abh, fechasuscripcion_cliente=abi)
    context = {
        "var_form": form,
    }
    return render(request, "inicio.html", context)