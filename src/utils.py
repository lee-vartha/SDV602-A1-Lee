import os

def load_image(image_name):
    """
    Load an image file from the images directory

    Args:
        image_name: the name of the image file to load

    Returns:
        the image data
    """
    return os.path.join('images', image_name)

