---
# Loom Video Downloader

Python Loom Video Downloader

Python Loom Video Downloader is a command-line tool written in Python to download videos from loom.com. It retrieves the video download link based on the video ID extracted from the provided URL and saves the video with the original video title as the filename, or using a specified filename prefix for multiple files.

## Getting Started

To run this tool, you need to have Python and pip installed on your machine.

### Installation

    Clone the repo: 'git clone https://github.com/YourUsername/python-loom-downloader.git'

### Install required Python packages:

    pip install requests beautifulsoup4

### Dependencies

This tool uses the following Python packages:

    requests - A simple, yet elegant HTTP library.
    beautifulsoup4 - A library for pulling data out of HTML and XML files.
    concurrent.futures - A high-level interface for asynchronously executing callables.

## Usage

Download a Single Video

To download a single video from loom.com, run the following command, replacing [VideoId] with the actual video ID from the URL:

```
python loom_video_downloader.py --url https://www.loom.com/share/[VideoId]
```

This will download the video and save it using the video title as the filename. If the title cannot be retrieved, it defaults to Untitled.mp4.

You can specify a different output filename with the --out or -o option:

```
python loom_video_downloader.py --url https://www.loom.com/share/[VideoId] --out [FileName].mp4
```

This will download the video and save it as [FileName].mp4.
Download Multiple Videos

To download multiple videos listed in a text file, use the --list option. Create a text file with one video URL per line and pass the file path to the script:

```
python loom_video_downloader.py --list path/to/urls.txt
```
By default, each video will be saved using the video title as the filename.

You can specify a filename prefix with the --prefix option. The script will append an auto-incrementing number to each downloaded video:

```
python loom_video_downloader.py --list path/to/urls.txt --prefix download --out path/to/output
```
This will save the videos with the specified prefix "download" and an incremented number in the given output directory.

    download-1.mp4
    download-2.mp4

If no output path is specified, it will default to the current directory.
Avoid Rate Limiting

To prevent getting rate-limited, a timeout can be set between downloads using the --timeout option:

```
python loom_video_downloader.py --list path/to/urls.txt --prefix download --out path/to/output --timeout 5
```
This will add a 5-second wait time between each download. Adjust as needed.
Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contributors

- [dgronos](https://github.com/dgronos)
## License

This project is open source and available under the [MIT License](https://choosealicense.com/licenses/mit/).

---
