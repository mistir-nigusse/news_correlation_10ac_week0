import json
import argparse
import os
import io
import shutil
import copy
import csv
from datetime import datetime
from time import sleep



class NewsDataLoader:

    def __init__(self, path):
       
        self.path = path
        self.news = self.get_news()
        self.traffic = self.get_traffic()
        self.domain_location = self.get_domain_location()
    

    def get_news(self):
      
        news = os.path.join(self.path, 'rating.csv')
        
        return news
    
    def get_traffic(self):
     
        traffic = os.path.join(self.path, 'traffic.csv')

        return traffic  
      
    def get_domain_location(self):
 
        domain_location = os.path.join(self.path, 'domains_location.csv')

        return domain_location



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Export News history')

    
    parser.add_argument('--zip', help="Name of a zip file to import")
    args = parser.parse_args()