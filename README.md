# picol
picol (pronounced "pickle") is a Python script to fetch the ten most used colors in an image and present the hex colors.

&nbsp;

## Screens
![Screenshot1](https://user-images.githubusercontent.com/265139/42291684-9bb36758-7fcd-11e8-933d-733961d8950e.jpg)

![Screenshot2](https://user-images.githubusercontent.com/265139/42291685-9bd48762-7fcd-11e8-81c6-7ef6331cf218.jpg)

![Screenshot3](https://user-images.githubusercontent.com/265139/42291686-9bf4c428-7fcd-11e8-953b-a762da2b3f03.jpg)


&nbsp;

## Short description

This script uses the `colorgram` library to extract the ten most used colors in an image. It then makes an image like shown in the screens above, or it can output text with links to www.hex-color.com.

## How to use

Minimum to run the script is with path to an image as an argument: `./picol.py ~/Pictures/picture.jpg`


```
usage: picol.py [-h] [-s] [-d] [-st] image

positional arguments:
  image

optional arguments:
  -h, --help         show this help message and exit
  -s, --save-image   Save image to a given file
  -d, --do-not-show  Do not show the image that is made
  -st, --save-text   Save text to a given file
```




## Dependencies:
- colorgram
- Pillow