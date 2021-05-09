import spritemaker


def main():

    """
    A simple console application to test the spritemaker module
    """

    imagepaths = ("icons/facebook.png", "icons/github.png", "icons/linkedin.png", "icons/pinterest.png", "icons/twitter.png", "icons/youtube.png")

    try:

        spritemaker.create_sprites(imagepaths, "sprites.png", "spritestyles.css")

    except IOError as e:

        print(e)

main()
