from rest_framework import serializers
from FarmaSaludApp.models import Categoria,Producto
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
        )


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id_cat','nombre_cat')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id_pro','nombre_pro','cantidad_pro','precio_pro','imagen_pro','fk_id_cat')

