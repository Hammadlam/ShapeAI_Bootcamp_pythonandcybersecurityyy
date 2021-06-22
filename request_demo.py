import requests
r= requests.get('https://imgs.xkcd.com/comics/python.png')


with open('comic.png', 'wb')as f:
    f.write(r.content)
lines = ['Weather', 'Thiis will show the weather of Karachi']
with open('readme.txt', 'w') as f:
    f.write('\n'.join(lines))