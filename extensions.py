file_extension = input("Enter image extension: ")

if file_extension.endswith((".gif",
                            ".jpg",
                            ".jpeg",
                            ".png",
                            ".pdf",
                            ".txt",
                            ".zip")):

    split_file_extension = (file_extension.replace(".","/"))
    print(split_file_extension)

else:
    print("application/octet-stream")










