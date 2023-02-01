from django.core.exceptions import ValidationError


def image_size_validator(image):
    image_max_size_bytes = 10 * 1000 * 1000
    image_max_size_px = 10000
    image_max_proportion_ratio = 20

    width, height = image.width, image.height
    min_side, max_side = min(width, height), max(width, height)
    if image.size > image_max_size_bytes:
        raise ValidationError("Image size is too large. Max size is 10mb.")
    if height + width > image_max_size_px:
        raise ValidationError(f"Image is too big. Max width + height: {image_max_size_px}")
    if max_side / min_side > image_max_proportion_ratio:
        raise ValidationError("Bad image proportions.")
