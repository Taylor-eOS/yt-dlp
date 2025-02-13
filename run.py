import yt_dlp

options = {
    #'format': '134+bestaudio',
    'format': '140',
    #'postprocessors': [{
    #    'key': 'FFmpegVideoConvertor',
    #    'preferedformat': 'mp4',
    #}],
    'outtmpl': '%(title)s.%(ext)s',
}
with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=FJ3N_2r6R-o'])
