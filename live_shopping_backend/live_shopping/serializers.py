from rest_framework import serializers
from live_shopping.models import LiveVideoRequest

class ProductSerializer(serializers.Serializer):
    """Serializer for Product Model"""
    id = serializers.IntegerField()
    title = serializers.CharField()
    image = serializers.URLField()

class LiveVideoRequestSerializer(serializers.ModelSerializer):
    """Serializer for LiveVideoRequest Model"""
    feedback = serializers.CharField(required=False)
    product = ProductSerializer()
	
    class Meta:
        model = LiveVideoRequest
        fields = "__all__"
        read_only_fields = [
			"id", "status", "dyte_meeting_id", "support_user",
            "user_dyte_participant_id", "support_user_dyte_participant_id"
		]