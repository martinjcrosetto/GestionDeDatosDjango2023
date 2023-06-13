from django.contrib import admin
from appfarmacia.models import *

# Register your models here.


@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = (
        'iddetalleventa',
        'cantidad',
        'preciounitario',
    )
    ordering = ['iddetalleventa']  # -nombre escendente, nombre ascendente
    search_fields = ['iddetalleventa']
    list_filter = (
        'iddetalleventa',
    )
@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = (
        'iddireccion',
        'calle',
        'altura',
    )
    ordering = ['iddireccion']  # -nombre escendente, nombre ascendente
    search_fields = ['calle']
    list_filter = (
        'iddireccion',
    )
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'idempleado',
        'nombre',
        'telefono',
    )
    ordering = ['idempleado']  # -nombre escendente, nombre ascendente
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

@admin.register(Localidad)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = (
        'idlocalidad',
        'nombre',
    )
    ordering = ['idlocalidad']  # -nombre escendente, nombre ascendente
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'idproducto',
        'nombre',
        'dosis',
    )
    ordering = ['idproducto']  # -nombre escendente, nombre ascendente
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )


@admin.register(ProductoProveedor)
class ProductoProveedorAdmin(admin.ModelAdmin):
    list_display = (
        'idproductoproveedor',
        'precio',
        'cantidad',
    )
    ordering = ['idproductoproveedor']  # -nombre escendente, nombre ascendente
    search_fields = ['idproductoproveedor']
    list_filter = (
        'idproductoproveedor',
    )

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = (
        'idproveedor',
        'nombre',
        'telefono',
    )
    ordering = ['idproveedor']  # -nombre escendente, nombre ascendente
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = (
        'idtipodocumento',
        'nombre',
    )
    ordering = ['idtipodocumento']  # -nombre escendente, nombre ascendente
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

@admin.register(TipoProducto)
class TipoProductoAdmin(admin.ModelAdmin):
    list_display = (
        'idtipoproducto',
        'nombre',
    )
    ordering = ['idtipoproducto']  # -nombre escendente, nombre ascendente
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

@admin.register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = (
        'idunidadmedida',
        'nombre',
        'descripcion',
    )
    ordering = ['idunidadmedida']  # -nombre escendente, nombre ascendente
    search_fields = ['nombre']
    list_filter = (
        'nombre',
    )

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = (
        'idventa',
        'fecha',
        'hora',
    )
    ordering = ['idventa']  # -nombre escendente, nombre ascendente
    search_fields = ['idventa']
    list_filter = (
        'idventa',
    )