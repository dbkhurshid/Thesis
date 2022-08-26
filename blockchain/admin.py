from django.contrib import admin
from .models import Blockchain

# class Blockchain(admin.ModelAdmin):
#     list_display= ('user_id', 'nonce', 'data', 'prev_hash', 'time_stamp')

admin.site.register(Blockchain)
# Register your models here.
