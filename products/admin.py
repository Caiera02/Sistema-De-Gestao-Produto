import csv
from django.http import HttpResponse
from django.contrib import admin
from openpyxl import Workbook
from .models import Cooperado,Brand, Category, Product, Branch, Controle,Phone

@admin.register(Cooperado)
class CooperadoAdmin(admin.ModelAdmin):
    list_display = ('name','mat','cpf','rg','is_active','is_inactive',)
    search_fields = ('name' ,)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="brands.csv"'
        writer = csv.writer(response)
        writer.writerow(['nome', 'ativo', 'descrição', 'cirado em', 'atualizado em'])
        for brand in queryset:
            writer.writerow([brand.name, brand.is_active, brand.description,
                             brand.created_at, brand.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]

@admin.register(Category)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'description', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('is_active',)

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="categories.csv"'
        writer = csv.writer(response)
        writer.writerow(['nome', 'ativo', 'descrição', 'cirado em', 'atualizado em'])
        for category in queryset:
            writer.writerow([category.name, category.is_active, category.description,
                             category.created_at, category.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]

#Maquina, Celular etc
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category','processor','memory_ram','storage','description',
                    'is_active', 'created_at')
    search_fields = ('title', 'brand__name', 'category__name',)
    list_filter = ('is_active', 'brand', 'category')

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        writer = csv.writer(response)
        writer.writerow(['título', 'marca', 'categoria', 'preço',
                         'ativo', 'descrição', 'criado em', 'atualizado em'])
        for product in queryset:
            writer.writerow([product.title, product.brand.name, product.category.name,
                             product.price, product.is_active, product.description,
                             product.created_at, product.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]
    
@admin.register(Branch)# Filiais
class BranchAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at',)
    search_fields = ('name',)

@admin.register(Controle)#Controles de de notebooks e celular
class ControleAdmin(admin.ModelAdmin):
    list_display = ('name','laptop','phones','branch','delivery','description','created_at',)
    #search_fields = ('controls__name')
    search_fields= ('description',)
    list_filter = ('name','phones', 'category',)

    #importando para excel
    def export_controles_to_excel(request,self,queryset):
    # Cria o workbook e a planilha
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "Controle"

        # Adiciona o cabeçalho
        headers = ['id','Nome', 'Computador', 'Telefone', 'Filial', 'Data da Entrega', 'Descrição', 'Data de Criação']
        worksheet.append(headers)

        # Recupera os dados do modelo e preenche a planilha
        controles = Controle.objects.all() #Busca em Controle todos o objetos
        for controle in controles: #Percorre os objetos
            worksheet.append([
                controle.id,
                str (controle.name),
                str (controle.laptop),
                str (controle.phones),
                str (controle.branch),
              controle.delivery.strftime("%Y-%m-%d %H:%M:%S"),
                # str (controle.description),
                # controle.created_at,
            ])

        # Configura a resposta HTTP para o download
        response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        response["Content-Disposition"] = "attachment; filename=controles.xlsx"
        workbook.save(response)
        return response
    
    export_controles_to_excel.short_description = 'Exportar para excel'
    actions = [export_controles_to_excel]

@admin.register(Phone)#Celulares
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('title','category','brand','imei',)
    search_fields = ('title',)
    list_filter = ('is_active', 'brand', 'category')

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'

        writer = csv.writer(response)
        writer.writerow(['nome', 'marca', 'categoria', 'preço',
                         'ativo', 'descrição', 'criado em', 'atualizado em'])
        for product in queryset:
            writer.writerow([product.title, product.brand.name, product.imei.name,
                             product.price, product.is_active, product.description,
                             product.created_at, product.updated_at])
        return response

    export_to_csv.short_description = 'Exportar para CSV'
    actions = [export_to_csv]