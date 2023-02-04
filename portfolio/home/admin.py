from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import UsedTechnology


class UsedTechnologyAdmin(ModelAdmin):
    model = UsedTechnology
    menu_label = "Technologies"
    menu_icon = "code"
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "color",)
    search_fields = ("name", "color",)


modeladmin_register(UsedTechnologyAdmin)
