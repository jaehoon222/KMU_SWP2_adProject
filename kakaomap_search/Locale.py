import json

class Locale:
    @staticmethod
    def MakeLocale(post):
        try:
            place_name = post['place_name']
            x = post['x']
            y = post['y']
            address_name = post['address_name']
            place_url = post['place_url']
            return Locale(place_name,x,y,address_name,place_url)
        except:
            return None
    def __init__(self,place_name,x,y,address_name, place_url):
        self.place_name = place_name
        self.x = x
        self.y = y
        self.address_name = address_name
        self.place_url = place_url