from uuid import uuid4


def greeting_image_path(instance, filename: str):
    _, extension = filename.rsplit(".", maxsplit=1)
    return f"greeting_images/{uuid4()}/picture.{extension}"
