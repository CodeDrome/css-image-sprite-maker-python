import os
from pathlib import Path

import PIL
from PIL import Image


def create_sprites(imagepaths, spritefilepath, cssfilepath):

    """
    Creates a sprite image by combining the images in the imagepaths tuple into one image.
    This is saved to spritefilepath.
    Also creates a file of CSS classes saved to cssfilepath.
    The class names are the original image filenames without the filename extension.
    IOErrors are raised.
    """

    size = _calculate_size(imagepaths)

    _create_sprite_image(imagepaths, size, "sprites.png")

    _create_styles(imagepaths, "spritestyles.css", "sprites.png")


def _calculate_size(imagepaths):

    """
    Creates a width/height tuple specifying the size of the image
    needed for the combined images.
    """

    totalwidth = 0
    maxheight = 0

    try:

        for imagepath in imagepaths:

            image = Image.open(imagepath)

            totalwidth += image.width
            maxheight = max(image.height, maxheight)

    except IOError as e:

        raise

    return (totalwidth, maxheight)


def _create_sprite_image(imagepaths, size, spritefilepath):

    """
    Creates a new image and pastes the original images into it,
    then saves it to spritefilepath.
    """

    sprites = PIL.Image.new("RGBA", size, (255,0,0,0))

    x = 0

    try:

        for imagepath in imagepaths:

            image = Image.open(imagepath)

            sprites.paste(image, (x, 0))

            x += image.width

        sprites.save(spritefilepath, compress_level = 9)

    except IOError as e:

        raise


def _create_styles(imagepaths, cssfilepath, spritefilepath):

    """
    Creates a set of CSS classes for the sprite images
    and saves it to spritefilepath.
    """

    styles = []

    x = 0

    try:

        for imagepath in imagepaths:

            image = Image.open(imagepath)

            classname = Path(imagepath).stem

            style = ["."]
            style.append(f"{classname}\n")
            style.append("{\n")

            style.append(f"    background: url('{spritefilepath}') no-repeat;\n")
            style.append(f"    width: {image.width}px;\n")
            style.append(f"    height: {image.height}px;\n")
            style.append("    display: inline-block;\n")
            style.append(f"    background-position: -{x}px 0px;\n")

            style.append("}\n\n")

            x += image.width

            style = "".join(style)

            styles.append(style)

        styles = "".join(styles)

        f = open(cssfilepath, "w+")
        f.write(styles)
        f.close()

    except IOError as e:

        raise
