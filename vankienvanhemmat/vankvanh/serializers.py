from rest_framework import serializers
from .models import Update, Backgrounds

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = ('id', 'header', 'created_at', 'link', 'message')
		
		
class BackgroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backgrounds
        fields = ('id', 'header', 'created_at', 'link', 'message')
		
