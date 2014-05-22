#!/usr/bin/env python

from twython import Twython
import xlrd
from time import sleep

#insert here api keys
CONSUMER_KEY = 'YOUR CONSUMER KEY'
CONSUMER_SECRET = 'YOUR CONSUMER SECRET'
ACCESS_KEY = 'YOU ACCESS KEY'
ACCESS_SECRET = 'YOUR ACCESS SECRET'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

sleeptime = raw_input('Insert the number of seconds you want to wait between each tweet: ')

#excel file
workbook = xlrd.open_workbook('tweet.xls')
worksheet = workbook.sheet_by_name('Sheet1')

#variables
num_rows = worksheet.nrows - 1
curr_row = -1

#tweeting all the first column rows
while curr_row < num_rows:
	curr_row += 1
	row = worksheet.row(curr_row)
	tweet = (worksheet.cell_value(curr_row, 0))
	print tweet
	api.update_status(status = tweet)
	sleep(int(sleeptime))
