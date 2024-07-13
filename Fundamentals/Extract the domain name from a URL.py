'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.
'''


import re


def domain_name1(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


def domain_name(url):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]


a = "http://github.com/carbonfive/raygun"
a.split('.')
print(a.split('//')[-1].split('www.')[-1].split('.')[0])