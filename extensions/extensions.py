filename = input("File name: ").strip()
idx = filename.rfind(".")
# print(idx)
ext = filename[idx:].lower()

if ext == ".gif":
    print("image/gif")
elif ext == ".jpg":
    print("image/jpeg")
elif ext == ".jpeg":
    print("image/jpeg")
elif ext == ".png":
    print("image/png")
elif ext == ".pdf":
    print("application/pdf")
elif ext == '.zip':
    print("application/zip")
elif ext == '.txt':
    print("text/plain")
else:
    print("application/octet-stream")
