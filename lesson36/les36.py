from PIL import Image
import requests
import os


def benchmark(func):
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper

@benchmark
def my_func(name):
    #import requests
    #webpage = requests.get(url)
    return "hello {}". format(name)

#some_func = my_func('Vasya')
#print(some_func)


URL = "https://lp-cms-production.imgix.net/2019-06/4871827ef10d74079fb636806d371ccc-brighton-hove.jpg"
@benchmark
def load_image(url):
    image = Image.open(requests.get(url, stream=True).raw)
    image.save(os.path.join(os.getcwd(), "img1.jpg"))

#load_image(URL)

@benchmark
def rotate_image(file, degrees):
    image = Image.open(file)
    rotated = image.rotate(degrees, expand=True)
    rotated.save("rotated.jpg")

rotate_image("img1.jpg", 45)