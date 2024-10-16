#!/usr/bin/python3
"""ye"""


import requests
import csv


def fetch_and_print_posts():
    """ye"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        print("\nTitles of all posts:\n")
        for post in posts:
            print(post['title'])
    else:
        print("Failed to retrieve posts.")


def fetch_and_save_posts():
    """ye"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        structured_data = []
        for post in posts:
            structured_data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
        csv_columns = ['id', 'title', 'body']
        try:
            with open('posts.csv', mode='w', newline='',
                      encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=csv_columns)
                writer.writeheader()
                writer.writerows(structured_data)
            print("Data has been successfully written to posts.csv.")
        except Exception as e:
            print(f"Error writing to CSV file: {e}")
    else:
        print("Failed to retrieve posts.")
