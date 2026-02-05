from PIL import Image

# 打开 JPG 文件
img = Image.open("input.jpg")

# 确保是 RGB 模式
if img.mode != 'RGB':
    img = img.convert('RGB')

# 保存为 BMP
img.save("output.bmp", 'BMP')
print("转换完成！")