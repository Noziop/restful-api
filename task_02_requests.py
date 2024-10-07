#!/usr/bin/python3
''' Module that fetches data from an API '''


import requests as req
import csv as csv


def fetch_and_print_posts():
    ''' Fetches data from an API '''
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = req.get(url)
    posts = response.json()
    for post in posts:
        print(post.get('title'))


def fetch_and_save_posts():
    ''' Fetches data from an API and saves it to a file '''
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = req.get(url)
    posts = response.json()
    with open('posts.csv', 'w') as file:
        for post in posts:
            file.write('"{}", "{}", "{}", "{}"\n'.format(
                post.get('userId'),
                post.get('id'),
                post.get('title'),
                post.get('body')
            ))
    print('Data saved to posts.csv')
    .*


if __name__ == '__main__':
    fetch_and_print_posts()
    fetch_and_save_posts()
