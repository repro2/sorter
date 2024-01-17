# File extensions categorized by type

# Image formats
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

# Video formats
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd", ".mkv"]

# Audio formats
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

# Document formats
document_extensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".txt", ".ods", ".eml"]

# Book formats
book_extensions = [".epub", ".mobi", ".fb2", ".fb3", "azw", ".prc", ".djvu"]

# Executable formats
exe_extensions = [".exe", ".zip", ".apk", ".torrent", ".rar", ".7z", ".m3u", ".Appx", ".html", ".ini", ".msi"]

# Mapping of categories to their respective extensions
file_extensions = {
    "image": image_extensions,
    "video": video_extensions,
    "audio": audio_extensions,
    "document": document_extensions,
    "books": book_extensions,
    "executables": exe_extensions
}
