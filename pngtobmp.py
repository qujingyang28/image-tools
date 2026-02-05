from PIL import Image

# 打开 PNG 文件
img = Image.open("input.png")

# 如果有透明背景，转为白色背景
if img.mode == 'RGBA':
    background = Image.new('RGB', img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[-1])
    img = background
elif img.mode != 'RGB':
    img = img.convert('RGB')

# 保存为 BMP
img.save("output.bmp", 'BMP')
print("转换完成！")