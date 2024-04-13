import json
import argparse
import os
import io
import shutil
import copy
import csv
from datetime import datetime
from pick import pick
from time import sleep
import pandas as pd


class NewsDataLoader:

    def __init__(self, path):
     
        self.path = path
        self.news = self.get_news_path()
        self.traffic = self.get_traffic_path()
        self.domain_location = self.get_domain_location_path()
    

    def get_news_path(self):
       
        news = os.path.join(self.path, 'rating.csv')
        
        return news
    
    def get_traffic_path(self):
       
        traffic = os.path.join(self.path, 'traffic.csv')
        
        return traffic
      
    def get_domain_location_path(self):
      
        domain_location = os.path.join(self.path, 'domains_location.csv')

        return domain_location


    def get_news_data(self):
       
        return pd.read_csv(self.get_news_path())
    
    def get_traffic_data(self):
      
        
        return pd.read_csv(self.get_traffic_path())
      
    def get_domain_location_data(self):
       

        return pd.read_csv(self.get_domain_location_path())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Export News history')

    
    parser.add_argument('--zip', help="Name of a zip file to import")
    args = parser.parse_args()