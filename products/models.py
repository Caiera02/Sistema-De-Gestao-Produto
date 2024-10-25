from django.db import models

class Cooperado(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    mat= models.IntegerField( verbose_name= 'Matricula')
    cpf = models.IntegerField( verbose_name= 'CPF')
    rg = models.IntegerField(  verbose_name='RG')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_inactive = models.BooleanField(verbose_name='Inativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Cooperado'

    def __str__(self):
        return self.name

#Marca
class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Marca'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Departamento'

    def __str__(self):
        return self.name
    
    
# Maquina, Celulares etc....    
class Product(models.Model):
    #name= models.ForeignKey(Cooperado, on_delete= models.PROTECT,related_name='products', verbose_name='Nome')
    title = models.CharField(max_length=100, verbose_name='Título')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
                              related_name='products', verbose_name='Marca')
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='products', verbose_name='Departamento')
    
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['title']
        verbose_name = 'Produto'

    def __str__(self):
        return self.title
   
class Branch(models.Model):
    name = models.TextField(null=True, blank=True, verbose_name='Nome')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
#Controle do notebooks
class Controle(models.Model):
    name= models.ForeignKey(Cooperado, on_delete= models.PROTECT,
                            related_name='controls', verbose_name='Nome')
    branch = models.ForeignKey(Branch, on_delete= models.PROTECT,
                            related_name='controls', verbose_name='Filial')
    
    laptop = models.ForeignKey(Product, on_delete=models.PROTECT, 
                               related_name='controls',verbose_name='Notebook')
    
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
                              related_name='controls', verbose_name='Marca')
    
    delivery = models.DateTimeField(auto_now_add=True, verbose_name='Entregue em')
    
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='controls', verbose_name='Departamento')
    
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_inactive = models.BooleanField(verbose_name='Inativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Controle'

    def __str__(self):
        return str(self.name)


