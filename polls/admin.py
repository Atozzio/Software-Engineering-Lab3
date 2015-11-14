fBook


#class ChoiceInline(admin.TabularInline):
   #  ;
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['Name']
    list_display = ('Name', 'Age', 'Country')
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    search_fields = ['Title']
    list_display = ('Title' ,'Publisher', 'PublishDate', 'Price')
admin.site.register(Book, BookAdmin)