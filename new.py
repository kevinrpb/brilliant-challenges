#!/usr/bin/env python3

import sys
import os
import subprocess
import argparse
from datetime import datetime
from shutil import copyfile

# Check if file exists
def new(title):
	# Get Date and Title
	DATE = datetime.today().strftime('%Y-%m-%d')
	TITLE = title

	# Template and post filenames
	TEMP = 'template'
	FILE = '_posts/{}-{}.md'.format(DATE, TITLE.replace(' ', '-'))

	print('[INFO] Creating file `{}`'.format(FILE))
	if not os.path.isfile(FILE):
		copyfile(TEMP, FILE)

		if os.path.isfile(FILE):
			print('[INFO] FILE `{}` successfully created'.format(FILE))

			subprocess.run(['sed', '-i', '-e', 's/YYYY-MM-DD/{}/g'.format(DATE), FILE])
			subprocess.run(['sed', '-i', '-e', 's/TITLE/{}/g'.format(TITLE), FILE])
			os.remove('{}-e'.format(FILE))
		else:
			print('[ERROR] File `{}` could not be created'.format(FILE))
	else:
		print('[ERROR] File `{}` already exists'.format(FILE))

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def gen():
	print('[INFO] Generating index file')

	posts = {}

	for filename in sorted(os.listdir('_posts/')):
		parts = filename.replace('.md', '').split('-')
		year = parts[0]
		month = parts[1]
		day = parts[2]
		title = '-'.join(parts[3:])

		if year not in posts:
			posts[year] = {}

		if month not in posts[year]:
			posts[year][month] = {}

		if day not in posts[year][month]:
			posts[year][month][day] = []

		posts[year][month][day].append(title)

	with open('index.md', 'w') as file:
		file.write(
"""---
title: Brilliant Challenges
description: Collection of Daily Challenges from Brilliant.org
---""")
		for year in posts.keys():
			file.write('\n\n# {}\n\n'.format(year))

			for month in posts[year].keys():
				file.write('## {}\n\n'.format(MONTHS[int(month) - 1]))

				for day in posts[year][month].keys():
					for title in posts[year][month][day]:
						path = '{}-{}-{}-{}'.format(year, month, day, title)
						href = "{{ site.baseurl }}{% post_url " + path + " %}"

						file.write('* [{}-{}-{} - {}]({})\n'.format(year, month, day, title, href))
	print('[INFO] Successfully generated index file')

parser = argparse.ArgumentParser()
parser.add_argument('--title', '-t', dest='title', type=str, nargs="+")
parser.add_argument('--generate', '-g', dest='generate', action='store_true')

args = parser.parse_args()

if args.title is not None:
	new(' '.join(args.title))

if args.generate:
	gen()
