#import flask
import os

base_path = '/home/onaquest/server-output'
image_sources = [f'{base_path}/images0', f'{base_path}/images1']

@whatever('/list') # return current list of all images
def get_list():
    list = [(file, os.path.getsize(f'{output_path}{id}/{file}')) for file in os.listdir(f'{output_path}{id}')]
    #return in some way 

# client will compare its list of images to what it needs and begin making requests 
@whatever('/images<int:id>/<string:date_str>.png') # request specific image
def get_image(date_str, id):
    
