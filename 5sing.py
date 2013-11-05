# encoding=utf-8
import urllib
import urllib2
import re

fl = 'musiclist.txt'

def fk5sing():
	links = get_link()
	for link in links:
		source = get_source(link)
		pat = re.compile(r'file: "(.*?)"')
		pat2 = re.compile(r'var SongName   = "(.*?)";')
		mlink = pat.findall(source)[0]
		mname = pat2.findall(source)[0]
		download(mlink, mname)
		update_fl(links[1:])

def get_source(link):	
	source = urllib2.urlopen(link).read()
	return source

def download(link, name):
	urllib.urlretrieve(link, 'music/'+name+'.mp3')

def get_link():
	f = open(fl, 'r')
	links = f.readlines()
	f.close()
	return links

def update_fl(links):
	f = open(fl, 'w')
	for link in links:
		f.write(link)
	f.close()

fk5sing()

