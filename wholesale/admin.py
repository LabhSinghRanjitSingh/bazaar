from django.contrib import admin

from wholesale.models import Book,Brand,ClothType,Piece,PieceImage


class PieceImageInline(admin.TabularInline):
    model = PieceImage



class PieceInline(admin.TabularInline):
    model = Piece
    inlines =[PieceImageInline]



class AdminBook(admin.ModelAdmin):
    list_display =['name','image_tag']
    inlines = [PieceInline]


class AdminBrand(admin.ModelAdmin):
    list_display =['name']




class AdminPiece(admin.ModelAdmin):
    list_display =['name']
    inlines = [PieceImageInline]


class AdminClothType(admin.ModelAdmin):
    list_display =['name']


# class AdminPieceImage(admin.ModelAdmin):
#     list_display =['piece','image_tag']


admin.site.register(Book,AdminBook)
admin.site.register(Brand,AdminBrand)
admin.site.register(Piece,AdminPiece)
admin.site.register(ClothType,AdminClothType)
# admin.site.register(PieceImage,AdminPieceImage)
