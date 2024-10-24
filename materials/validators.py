from rest_framework.serializers import ValidationError

available_url = "https://www.youtube.com/watch?v"
def validate_video_url(value):
    if available_url not in value:
        raise ValidationError("Запрещенная ссылка, разрешены только ссылки на youtube")