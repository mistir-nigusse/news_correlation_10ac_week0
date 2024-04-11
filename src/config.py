from __future__ import print_function
import argparse
import os

default_path = os.path.join("data")
default_news_path = os.path.join(default_path, 'rating.csv')

parser = argparse.ArgumentParser(description='cmdArgs')
parser.add_argument('--output', type=str, default='news_output.csv',
                help='filename to write analysis output in CSV format')
parser.add_argument('--path', required=False, type=str, default=default_path, help='directory where news data reside')
parser.add_argument('--news', type=str, default='rating.csv', help='which news we are parsing')
parser.add_argument('--traffic', type=str, default='trafiic.csv', help='which traffic we are parsing')
parser.add_argument('--domain', type=str, default='domains_location.csv', help='a data conataining domain locations')

cfg, unknown_args = parser.parse_known_args()
print(cfg)

# Print the values of the arguments
print(f'Output File: {cfg.output}')
print(f'Path: {cfg.path}')
print(f'News Data: {cfg.news}')
print(f'Traffic Data: {cfg.traffic}')
print(f'Domain Location Data: {cfg.domain}')