#Meme Module
This module has all the models and functions required for generating memes.

--Dependencies
pillow package is used to draw text over images.

--Usage
Import and use `MemeEngine` class to provide the image path, meme
body and author.
`generate_meme` method to generate random memes.


--Models

---MemeEngine
This class takes an output directory path as an argument. Each instance keeps
count of the image generated. The `make_meme` method creates the meme image and
saves it in the provided output directory and returns a path to the created
meme. It uses the `pillow` library to resize image and draw text on it.
