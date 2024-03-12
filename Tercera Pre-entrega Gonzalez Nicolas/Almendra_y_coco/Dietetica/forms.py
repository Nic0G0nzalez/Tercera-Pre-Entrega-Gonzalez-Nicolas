from django import forms

class ClientesForm(forms.Form):
    nombre= forms.CharField(max_length=40, required= True)
    apellido= forms.CharField(max_length=40, required= True)
    email= forms.EmailField(required= True)
    DNI= forms.IntegerField(required= True)


class VendedoresForm(forms.Form):
    nombre= forms.CharField(max_length=40, required= True)
    apellido= forms.CharField(max_length=40, required= True)
    email= forms.EmailField(required= True)
    DNI= forms.IntegerField(required= True)

class ProductosForm(forms.Form):
    nombre= forms.CharField(max_length=40, required= True)
    gramos= forms.IntegerField(required= True)
    pesos= forms.IntegerField(required= True)

class Productos_pormayorForm(forms.Form):
    nombre= forms.CharField(max_length=40, required= True)
    kilos= forms.IntegerField(required= True)
    pesos= forms.IntegerField(required= True)




