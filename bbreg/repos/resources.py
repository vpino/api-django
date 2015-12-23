from tastypie.authorization import Authorization
#from tastypie.authentication import Authentication
from tastypie.resources import ModelResource
from models import Repositorio, PackageGeneric, PackageGenericEdu, PackageCinnamon, PackageCinnamonEdu, PackageMate, PackageMateEdu

API_LIMIT_PER_PAGE = 0

class RepositoryResource(ModelResource):
    class Meta:
        queryset = Repositorio.objects.all()
        resource_name = 'repositorios'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()

class PackageGenericResource(ModelResource):
    class Meta:
        queryset = PackageGeneric.objects.all()
        resource_name = 'paquetes-generic'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()

class PackageGenericEduResource(ModelResource):
    class Meta:
        queryset = PackageGenericEdu.objects.all()
        resource_name = 'paquetes-generic-edu'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()

class PackageCinnamonResource(ModelResource):
    class Meta:
        queryset = PackageCinnamon.objects.all()
        resource_name = 'paquetes-cinnamon'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True

class PackageCinnamonEduResource(ModelResource):
    class Meta:
        queryset = PackageCinnamonEdu.objects.all()
        resource_name = 'paquetes-cinnamon-edu'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()

class PackageMateResource(ModelResource):
    class Meta:
        queryset = PackageMate.objects.all()
        resource_name = 'paquetes-mate'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()

class PackageMateEduResource(ModelResource):
    class Meta:
        queryset = PackageMateEdu.objects.all()
        resource_name = 'paquetes-mate-edu'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        authorization = Authorization()