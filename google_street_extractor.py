import google_streetview.api
from  matplotlib import pyplot as plt
import requests
from PIL import Image
from io import BytesIO
import numpy as np

   
    
class ImageExtractor():
    
    def __init__(self,zip,city,street,number,key):
        self.zip = zip
        self.city = city
        self.street = street
        self.number = number
        self.address = f"{street} {number} ,{zip} {city}"
        self.key = key

    # Download meta data information from Google Street API
    def get_metadata(self):
        '''
        Download meta data information from Google Street API
        '''
        # Define parameters for street view api
        params = [{
            'size': '640x640', # max 640x640 pixels
            'location': self.address,
            'pitch': '20',
            'key': self.key}]

        # Create a results object
        results = google_streetview.api.results(params)

        self.links = results.links
        self.location = results.metadata
        self.params = results.params
    
    # Download core image informations in RGB format
    def get_image(self):
        '''
        Download core image informations in RGB format
        '''
        response = requests.get(*self.links)
        self.image_pillow = Image.open(BytesIO(response.content))
        self.image = np.asarray(self.image_pillow)

    
