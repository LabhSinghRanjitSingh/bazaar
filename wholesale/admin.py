from django.contrib import admin
from django.utils.safestring import mark_safe

from wholesale.models import Book, Brand, ClothType, Piece, PieceImage, Tag, ContactInfo, Order


class PieceImageInline(admin.TabularInline):
    model = PieceImage


class PieceInline(admin.TabularInline):
    model = Piece
    inlines = [PieceImageInline]


class AdminBook(admin.ModelAdmin):
    list_display = ['name', 'image_tag']
    inlines = [PieceInline]


class AdminBrand(admin.ModelAdmin):
    list_display = ['name']


class AdminTag(admin.ModelAdmin):
    list_display = ['name']


class AdminPiece(admin.ModelAdmin):
    list_display = ['name']
    inlines = [PieceImageInline]


class AdminClothType(admin.ModelAdmin):
    list_display = ['name']


class AdminContactInfo(admin.ModelAdmin):
    list_display = ['name', 'businessName', 'city', 'state', 'country', 'phoneNumber', 'email', 'notes']


class AdminOrder(admin.ModelAdmin):
    list_display = ['pk', 'contactInfo', '_books']

    def _books(self, object):
        _html = "<ul>"
        _html += " ".join(["<li><a href='/admin/wholesale/book/%d/change/'>%s</a></li>" % (book.id, book.name) for book in
                         object.cartBooks.all()])
        _html += "</ul>"
        return mark_safe(_html)



# class AdminPieceImage(admin.ModelAdmin):
#     list_display =['piece','image_tag']


admin.site.register(Book, AdminBook)
admin.site.register(Brand, AdminBrand)
admin.site.register(Tag, AdminTag)
admin.site.register(Piece, AdminPiece)
admin.site.register(ClothType, AdminClothType)
admin.site.register(ContactInfo, AdminContactInfo)
admin.site.register(Order, AdminOrder)
# admin.site.register(PieceImage,AdminPieceImage)
