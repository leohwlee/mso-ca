"""Contact sheets of final browser screenshots for visual QA."""
from pathlib import Path
from PIL import Image,ImageDraw
p=Path(__file__).resolve().parent/'previews'
for n in range(1,8):
    canvas=Image.new('RGB',(1500,1740),'#eaf0f4')
    draw=ImageDraw.Draw(canvas)
    for col,lang in enumerate(('tc','en','both')):
        for row,device in enumerate(('desktop','mobile')):
            im=Image.open(p/f'part-{n}-{lang}-{device}.png')
            im.thumbnail((480,800))
            x=col*500+(500-im.width)//2;y=row*870+42
            draw.text((col*500+15,row*870+15),f'Part {n} | {lang.upper()} | {device}',fill='#173c59')
            canvas.paste(im,(x,y))
    canvas.save(p/f'part-{n}-all-modes.png')
