import yt_dlp

# تأكد من استبدال `video_url` برابط الفيديو الذي تريد تنزيله.
video_url = 'https://youtube.com/watch?v=your_video_id'

ydl_opts = {
    'cookiefile': 'cookies.txt',  # تأكد من أن اسم الملف يتطابق مع اسم الملف الذي قمت بتحميله
    # يمكنك إضافة خيارات أخرى هنا إذا لزم الأمر
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([https://youtube.com/watch?v=your_video_id])
