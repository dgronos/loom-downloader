import argparse
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
import shutil

def fetch_video_details(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('meta', property='og:title')['content'] if soup.find('meta', property='og:title') else 'Untitled'
    video_id = urlparse(url).path.split('/')[-1]
    download_url = fetch_loom_download_url(video_id)
    return title, download_url

def fetch_loom_download_url(video_id):
    response = requests.post(f'https://www.loom.com/api/campaigns/sessions/{video_id}/transcoded-url')
    response.raise_for_status()
    return response.json()['url']

def download_video(download_url, output_path):
    with requests.get(download_url, stream=True) as response:
        response.raise_for_status()
        with open(output_path, 'wb') as f:
            shutil.copyfileobj(response.raw, f)

def valid_filename(title):
    # Allow letters, numbers, spaces, dots, underscores, and hyphens
    return ''.join(char for char in title if char.isalnum() or char in " .-_").rstrip()

def download_task(url):
    title, download_url = fetch_video_details(url)
    sanitized_filename = valid_filename(title)  # Use the valid_filename function
    output_path = f"{sanitized_filename}.mp4"
    print(f"Downloading video '{title}' to '{output_path}'")
    download_video(download_url, output_path)

def main():
    parser = argparse.ArgumentParser(description="Download videos from Loom.")
    parser.add_argument('-u', '--url', type=str, help='URL of the video in the format https://www.loom.com/share/[ID]')
    parser.add_argument('-l', '--list', type=str, help='Filename of the text file containing the list of URLs')
    args = parser.parse_args()

    if not args.url and not args.list:
        parser.error('Please provide either --url or --list')

    if args.url and args.list:
        parser.error('Please provide either --url or --list, not both')

    if args.list:
        with open(args.list, 'r') as file:
            urls = [line.strip() for line in file.readlines() if line.strip()]
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(download_task, urls)
    elif args.url:
        download_task(args.url)

if __name__ == "__main__":
    main()
