from PIL import Image, ImageDraw, ImageFont
import pandas as pd

df = pd.read_csv('list.csv') # opens the csv file

for index, j in df.iterrows():

    img = Image.open('certificate.png') # opens the template certificate image

    # THESE VALUES ARE SUBJECTED TO CHANGE ACCORDING TO THE POSITION OF THE TEXT ON THE CERTIFICATE
    start = 750
    if (len(j['Name']) < 10):
        start -= (len(j['Name']) - 10) * len(j['Name']) * 2
        end = 665
        font = ImageFont.truetype('arial.ttf', 120)
    elif (len(j['Name']) < 16):
        start -= (len(j['Name']) - 10) * len(j['Name'])
        end = 665
        font = ImageFont.truetype('arial.ttf', 120)
    else:
        start -= (len(j['Name']) - 10) * len(j['Name']) * 0.8
        end = 680
        font = ImageFont.truetype('arial.ttf', 90)
    

    draw = ImageDraw.Draw(img)
    draw.text(xy=(start, end),
              text='{}'.format(j['Name'].upper()),
              fill=(255, 255, 255),
              font=font)

    img.save('pictures/{}.png'.format(j['Name'].upper())) # pictures is the output folder
    print(j['Name'].upper())
    # break