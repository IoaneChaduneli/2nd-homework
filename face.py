import emoji

hello = input("Please say hello: ").replace(":)", emoji.emojize(":slightly_smiling_face:")).replace(":(", emoji.emojize(":slightly_frowning_face:"))


print(hello)