from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile


def validate_photo_size(value: UploadedFile) -> None:
    MAX_SIZE = 5242880
    if value.size > MAX_SIZE:
        bytes_size = MAX_SIZE / (1024 * 1024)
        file_size = value.size / (1024 * 1024)
        raise ValidationError(f"The maximum file size is {bytes_size}MB and the uploaded file is {file_size}MB.")
