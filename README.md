# 🖼️ 图片格式转换工具集

一个简单的 Python 工具集合，支持多种图片格式互转。

## ✨ 功能

| 工具 | 功能 | 状态 |
|:---|:---|:---|
| `converter.py` | PNG/JPG → BMP | ✅ 已完成 |
| `webp_to_png.py` | WebP → PNG | 🚧 计划中 |
| `batch_convert.py` | 批量转换文件夹 | 🚧 计划中 |

## 🚀 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
使用示例
单文件转换：
bash
复制
python converter.py 图片.jpg
python converter.py 图片.png
输出为同名 .bmp 文件。
📋 支持的格式
输入：PNG、JPG、JPEG、BMP、GIF、WebP 等
输出：BMP（24位 RGB）
📁 项目结构
复制
image-tools/
├── converter.py      # 主程序
├── requirements.txt  # 依赖
├── README.md         # 说明文档
└── .gitignore        # 忽略规则
🤝 贡献
欢迎提交 Issue 和 PR！
📄 许可
MIT License