# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DetalleVenta(models.Model):
    iddetalleventa = models.AutoField(primary_key=True)
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='idventa', blank=True, null=True)
    idproducto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    preciounitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class Direccion(models.Model):
    iddireccion = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=255, blank=True, null=True)
    altura = models.IntegerField(blank=True, null=True)
    idlocalidad = models.ForeignKey('Localidad', models.DO_NOTHING, db_column='idlocalidad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    idempleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)
    iddireccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='iddireccion', blank=True, null=True)
    idtipodocumento = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='idtipodocumento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class Localidad(models.Model):
    idlocalidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'localidad'


class Producto(models.Model):
    idproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    idtipoproducto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='idtipoproducto', blank=True, null=True)
    idunidadmedida = models.ForeignKey('UnidadMedida', models.DO_NOTHING, db_column='idunidadmedida', blank=True, null=True)
    dosis = models.IntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoProveedor(models.Model):
    idproductoproveedor = models.AutoField(primary_key=True)
    idproducto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='idproducto', blank=True, null=True)
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor', blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto_proveedor'


class Proveedor(models.Model):
    idproveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)
    iddireccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='iddireccion', blank=True, null=True)
    idtipodocumento = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='idtipodocumento', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class TipoDocumento(models.Model):
    idtipodocumento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoProducto(models.Model):
    idtipoproducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class UnidadMedida(models.Model):
    idunidadmedida = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidad_medida'


class Venta(models.Model):
    idventa = models.AutoField(primary_key=True)
    idempleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='idempleado', blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'
