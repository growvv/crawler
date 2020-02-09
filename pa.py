from requests_html import HTMLSession

base_url = 'https://www.cnblogs.com/lfri/default.html?page='
id = 1

def get_title(url):
    global id #在函数内部修改全局变量的值，要先用global声明全局变量。
    session = HTMLSession()
    r = session.get(url)
    r.html.render(scrolldown=3, sleep=0.01)  #下拉3次
    titles = r.html.find('a.postTitle2')
    print(len(titles))
    with open('titles.txt', 'a', encoding="utf-8") as f:  #使用utf-8编码
        for i, title in enumerate(titles):
            s = f'{id} [{title.text}]({title.attrs["href"]})'
            print(s)
            f.write(s + '\n')
            id = id + 1

if __name__ == '__main__':
    for x in range(1, 3):
        print('当前页面: '+ str(x))
        get_title(base_url+str(x))
