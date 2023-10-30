from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'description', 'created_at',]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['name'].disabled = True
            form.base_fields['name'].widget.attrs['style'] = 'background-color :skyblue'
        else:
            form.base_fields['name'].widget.attrs['style'] = 'background-color :transparent'

        return form


admin.site.register(Product, ProductAdmin)
