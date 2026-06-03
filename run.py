import yt_dlp

default = 'bestaudio'

def get_url():
    return input("Input url: ").strip()

def list_formats(url):
    with yt_dlp.YoutubeDL({'listformats': True}) as ydl:
        ydl.extract_info(url, download=False)

def get_format():
    print("Combinations like 137+140 are possible.")
    format = input(f"Enter format (" + default + "): ").strip() or default
    return format

def download(url, fmt):
    with yt_dlp.YoutubeDL({'format': fmt, 'outtmpl': '%(title)s.%(ext)s'}) as ydl:
        ydl.download([url])

def main():
    url = get_url()
    list_formats(url)
    fmt = get_format()
    download(url, fmt)

if __name__ == '__main__':
    main()
