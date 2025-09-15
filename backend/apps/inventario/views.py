from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.inventario.dao.producto_dao import ProductoDAO
from apps.inventario.dto.producto_dto import ProductoDTO

class ProductoViewSet(viewsets.ViewSet):
    """
    CRUD básico para productos usando DAO y DTO.
    """

    def list(self, request):
        productos = ProductoDAO.listar_productos()
        serializer = ProductoDTO(productos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        producto = ProductoDAO.obtener_producto_por_id(pk)
        if producto:
            serializer = ProductoDTO(producto)
            return Response(serializer.data)
        return Response({"error": "Producto no encontrado"}, status=404)

    def create(self, request):
        serializer = ProductoDTO(data=request.data)
        if serializer.is_valid():
            producto = ProductoDAO.crear_producto(**serializer.validated_data)
            return Response(ProductoDTO(producto).data, status=201)
        return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        producto = ProductoDAO.obtener_producto_por_id(pk)
        if not producto:
            return Response({"error": "Producto no encontrado"}, status=404)
        serializer = ProductoDTO(data=request.data)
        if serializer.is_valid():
            updated = ProductoDAO.actualizar_producto(pk, **serializer.validated_data)
            return Response(ProductoDTO(updated).data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        producto = ProductoDAO.obtener_producto_por_id(pk)
        if not producto:
            return Response({"error": "Producto no encontrado"}, status=404)
        ProductoDAO.eliminar_producto(pk)
        return Response({"mensaje": "Producto eliminado"})
