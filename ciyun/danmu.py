import requests
import re
import tqdm
from collections import Counter
import pandas as pd
headers = {
    'Cookie':'buvid3=E4E1E1D7-A64C-7A43-9A9A-DE61F1AF44B916370infoc; b_nut=1694321616; CURRENT_FNVAL=4048; share_source_origin=COPY; bsource=share_source_copy_link; _uuid=3E6D6E78-CCC10-96105-A42E-D673D289F2CE16922infoc; buvid4=6042B332-DC3C-01B4-1951-F4AF405B5CB117125-023091012-%2FxwqHe8zHTXpnz9Y2USDLw%3D%3D; buvid_fp=7b4534f0b1972275112c323e4eb905db; rpdid=|(u))kkYuuuJ0J\'uYmRJkuYu); bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ1ODA4MjAsImlhdCI6MTY5NDMyMTYyMCwicGx0IjotMX0.kgGCqdQZvadUjM773n3lji9A_NtE2YBrdpjSWuR2x0I; bili_ticket_expires=1694580820; PVID=1; SESSDATA=5f63dce6%2C1709874063%2Cea219%2A91CjADAwKkKJokckJKer_rqNO67xnhCQG8GIo7rORSWaU5zSQA_2TzhDSm4DjjfRAizJISVlY4d3A0Vkxfd3ZpR25UemxaUmtyLVBSbmEzUlZPRUJVNEIwSzc1YlZjb3A0RDBxcmNhYW52VEZlVXUxX3dFYjdxM2N3ei12MjNPcXRheHZ0NUlVNE5nIIEC; bili_jct=1d3145b04ba2200537af1de0f51a2ce4; DedeUserID=107927451; DedeUserID__ckMd5=8d794fe3791038c4; sid=7kgtkecu; b_lsid=DE45528C_18A88EA5A8B',
    'Origin':'https://www.bilibili.com',
    'Referer':'https://www.bilibili.com/video/BV1yF411C7ZJ/?buvid=Y55AA5505B13D875552EBC388CAAAD3C0D61&is_story_h5=false&mid=4gsDUBgtXr2jR9%2BKhoxF8A%3D%3D&p=1&plat_id=114&share_from=ugc&share_medium=ipad&share_plat=ios&share_source=COPY&share_tag=s_i&timestamp=1694321510&unique_k=AHRIuaU&up_id=335850246',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
whole =[]
for i in tqdm.tqdm(range(1,18)):
    url = f'https://api.bilibili.com/x/web-interface/search/all/v2?page={i}&keyword=日本核污染水排海'
    response = requests.get(url=url, headers=headers)
    bvlist = re.findall(r'"bvid":"(.*?)"', response.text)
    for bv in tqdm.tqdm(bvlist):
        url1 = 'https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp'.format(bv)
        result = requests.get(url=url1, headers=headers)
        res_dict = result.json()
        cid = res_dict['data'][0]['cid']
        url2 = 'https://api.bilibili.com/x/v1/dm/list.so?oid={}'.format(cid)
        result = requests.get(url=url2,headers=headers)
        res_xml = result.content.decode('utf-8')
        pattern = re.compile('<d.*?>(.*?)</d>', re.S)
        danmu = re.findall(pattern, res_xml)
        whole = whole +danmu
        with open('danmu.txt', mode='a', encoding='utf-8') as f:
            for i in (range(len(danmu))):
                f.write(str(danmu[i]).strip() + '\n')
word_counts = Counter(whole)
df = pd.DataFrame(word_counts.items(), columns=["字符串", "频次"])
df.to_excel("out.xlsx", index=False)
top_20_words = word_counts.most_common(20)
for word, count in top_20_words:
    print(f"{word}: 出现 {count} 次")


