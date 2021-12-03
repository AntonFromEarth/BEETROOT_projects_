#run `pip install pillow` before
#make sure you have `requests` lib installed
#use https://pillow.readthedocs.io/en/stable/handbook/tutorial.html for reference

from PIL import Image
import requests


URL = 'https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg'


def Load_Image(filename="example.jpg", url):
    image = Image.open(requests.get(url,stream=True).raw)
    image.save(os.path.join(os.getcwd(), filename))

def printImageData(file):
    image = Image.open(file)
    print(img.size, img.mode)

def is_square_image(file):
    image = Image.open(file)
    return not image.size[0] != image.size[1]

def create_thumbnail(file):
    #TODO: handle all errors on thumbnail creation
    thumbnail_size = (200, 200)
    image = Image.open('file')
    image.thumbnail(thumbnail_size)
    image.save('thumbnail.jpg', "JPEG")

def is_thumbnail(file):
    thumbnail_size = [200, 200]
    image = Image.open(file)
    return image.size() == thumbnail_size

def rotate_image(degrees):
    image = Image.open(file)
    rotated = image.rotate(degrees)
    image.save('rotated.jpg')

def flip_image(file, direction):
    directions = {'LR': Image.FLIP_LEFT_RIGHT, 'TB':Image.FLIP_TOP_BOTTOM}
    image = Image(file)
    out = image.transpose(directions[direction])
    out.save('flipped.jpg')

def copy_images_to_dir(dirname):
    '''Copies all images from current folder into subfolder'''

    for file in os.listdir():
        try:
            image = Image.open(file)
            image.save(os.path.join(os.getcwd(), dirname, image.filename))
        except:
            break

def delete_images(self):
    for file in os.listdir:
        if file.endswith(".jpg"):
            os.remove(file)

#TODO: create a function that will save rectangle area from given image to the separate file
#with name 'rectangle.jpg'. Coordinates of rectangle have to be passed as tuple of 4 integers


if __name__ == __main__:
    Load_Image(URL)
    printImageData()
    is_square_image('example.jpg')
    create_thumbnail('example.jpg')
    is_thumbnail('thumbnail.jpg')
    rotate_image('example.jpg', 45)
    flip_image('example.jpg', 'LT')
    copy_images_to_dir('images')
print('Done!')
