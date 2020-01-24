from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'email',
        'slug',
        'number',
        'gender',
        'bio',
        'active',
        'updated', 
        'timestamp',
        'get_age'
    ]
    readonly_fields = ['updated', 'timestamp','get_age']
    def get_age(self,obj,*args,**kwargs):
        return str(obj.age())
    class Meta:
        model  = Person
        

admin.site.register(Person, PersonAdmin)
