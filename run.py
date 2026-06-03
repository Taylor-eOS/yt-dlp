import yt_dlp

options = {
    #'format': '134+bestaudio',
    #'format': '140',
    'format': 'bestaudio',
    #'postprocessors': [{'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4',}],
    'outtmpl': '%(title)s.%(ext)s',
}
with yt_dlp.YoutubeDL(options) as ydl:
    input_file = input("Input url: ")
    ydl.download([input_file])
