from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from FarmaSaludApp.models import Categoria,Producto
from django.contrib.auth.models import User
from FarmaSaludApp.serializers import CategoriaSerializer,ProductoSerializer,UserSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def categoriaApi(request,id=0):
    if request.method=='GET':
        categorias = Categoria.objects.all()
        categorias_serializer = CategoriaSerializer(categorias, many=True)
        return JsonResponse(categorias_serializer.data, safe=False)
    elif request.method=='POST':
        categoria_data = JSONParser().parse(request)
        categoria_serializer = CategoriaSerializer(data=categoria_data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return JsonResponse("Registro Exitoso!!", safe=False) 
        return JsonResponse("Error al Registrar.", safe=False)
    
    elif request.method=='PUT':
        categoria_data = JSONParser().parse(request)
        categoria = Categoria.objects.get(id_cat=categoria_data['id_cat'])
        categoria_serializer = CategoriaSerializer(categoria, data=categoria_data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return JsonResponse("Actualizacion Exitosa!!", safe=False)
        return JsonResponse("Error al Actualizar.", safe=False)
    elif request.method=='DELETE':
        categoria = Categoria.objects.get(id_cat=id)
        categoria.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

@csrf_exempt
def productoApi(request,id=0):
    if request.method=='GET':
        productos = Producto.objects.all()
        productos_serializer = ProductoSerializer(productos, many=True)
        return JsonResponse(productos_serializer.data, safe=False)
    elif request.method=='POST':
        producto_data = JSONParser().parse(request)
        producto_serializer = ProductoSerializer(data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return JsonResponse("Registro Exitoso!!", safe=False) 
        return JsonResponse("Error al Registrar.", safe=False)
    
    elif request.method=='PUT':
        producto_data = JSONParser().parse(request)
        producto = Producto.objects.get(id_pro=producto_data['id_pro'])
        producto_serializer = ProductoSerializer(producto, data=producto_data)
        if producto_serializer.is_valid():
            producto_serializer.save()
            return JsonResponse("Actualizacion Exitosa!!", safe=False)
        return JsonResponse("Error al Actualizar.", safe=False)
    elif request.method=='DELETE':
        producto = Producto.objects.get(id_pro=id)
        producto.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

@csrf_exempt
def guardarImagen(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name, safe=False)


@csrf_exempt
def userApi(request,id=0):
    if request.method=='GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method=='POST':  
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Registro Exitoso!!", safe=False) 
        return JsonResponse("Error al Registrar.", safe=False)
    
    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(id=user_data['id'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Actualizacion Exitosa!!", safe=False)
        return JsonResponse("Error al Actualizar.", safe=False)
    elif request.method=='DELETE':
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse("Registro Eliminado Exitosamente!!", safe=False)

    