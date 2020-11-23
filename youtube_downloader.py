import pafy

link_input = input('Enter your link here : ')
url = pafy.new(link_input)

audio = url.audiostreams
dl = url.getbest()

type = input("Enter want you want to download [video/audio] :")
if type == 'video':
    dl.download()
elif type == 'audio':
    audio[0].download()
else:
    print("Sorry we have no idea about what you want")










