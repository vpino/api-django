from django.db import models


class Repositorio(models.Model):
    Nombre = models.CharField('nombre proyecto', max_length=50)
    Url = models.CharField('url repositorio del proyecto', max_length=100)

    def __unicode__(self):
        return self.Nombre

class PackageGeneric(models.Model):
    Nombre = models.CharField('nombre paquete', max_length=50)

    def __unicode__(self):
        return self.Nombre

class PackageGenericEdu(models.Model):
    Nombre = models.CharField('nombre paquete', max_length=50)

    def __unicode__(self):
        return self.Nombre

class PackageCinnamon(models.Model):
    Nombre = models.CharField('nombre paquete', max_length=50)

    def __unicode__(self):
        return self.Nombre

class PackageCinnamonEdu(models.Model):
    Nombre = models.CharField('nombre paquete', max_length=50)

    def __unicode__(self):
        return self.Nombre

class PackageMate(models.Model):
    Nombre = models.CharField('nombre paquete', max_length=50)

    def __unicode__(self):
        return self.Nombre

class PackageMateEdu(models.Model):
    Nombre = models.CharField('nombre paquete', max_length=50)

    def __unicode__(self):
        return self.Nombre
