import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
def download_images(url, save_folder):
    # 发送GET请求获取网页内容
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.example.com',
        'Accept-Language': 'en-US,en;q=0.9',
        # 添加其他可能需要的头信息
    }
    response = requests.get(url, headers=headers)

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到所有图片标签
    img_tags = soup.find_all('img')
    for img_tag in img_tags:
        # 获取图片的URL
        img_url = img_tag.get('src')

        # 将相对路径转换为绝对路径
        img_url = urljoin(url, img_url)

        # 发送GET请求获取图片内容
        img_response = requests.get(img_url)

        # 保存图片到本地
        with open(f'{save_folder}/image{img_tags.index(img_tag) + 1}.jpg', 'wb') as img_file:
            img_file.write(img_response.content)


# 示例用法
website_url = 'https://unsplash.com/s/photos/apple'
save_folder_path = '/Users/sakana/Downloads/pic'
download_images(website_url, save_folder_path)
