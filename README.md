# crawler ![CI](https://github.com/growvv/crawler/workflows/CI/badge.svg)
使用GitHub Action运行爬虫，并将结果保存到七牛云对象存储。

[查看效果](https://rogn.top/crawler/)

## 一、爬虫部分

### 1. 安装python环境及依赖

必须要先装python再pip

```yml
    - name: Setup Python environment
      uses: actions/setup-python@v1.1.1
    
    - name: Install Dependence
      run: pip install requests-html
```

### 2.运行爬虫

```yml
    - name: Run pa.py
      run: python pa.py
```

## 二、Markdown转HTML
### 1. 安装nodejs及依赖
需要 <code>fs</code> 和 <code>marked</code>，这一次没有直接安装，而是使用了 <code>package-lock.json</code>。
```yml
    - name: Setup Node.js for use with actions
      uses: actions/setup-node@v1.1.0
    
    - name: Install Dependence
      run: npm install
```

### 2. 转换格式
可以利用marked库将titles.md转成index.html，开启Github Pages就能在浏览器查看结果。

```js
fs.readFile('./titles.md', 'utf-8', (err, data)=>{
    if(err){
        throw err
    }else{
        // 3.使用marked方法，将md格式的文件转化为html格式
        let htmlStr = marked(data.toString());
        // 4.将转化的html格式的字符串，写入到新的文件中
        fs.writeFile('./index.html', htmlStr, err=>{
            if(err){
                throw err
            }else{
                console.log("success")
                console.log(htmlStr)
            }
        })
    }
})
```

## 三、 上传部分

### 1. 安装qrsctl

由于我使用的七牛云对象存储，我觉得好用一点的工具qrsctl。

需要先下载，并赋予可执行权限。具体语法见[官方文档](https://developer.qiniu.com/kodo/tools/1300/qrsctl)。

```yml
    - name: Install qrsctl
      run: |
        wget http://devtools.qiniu.com/linux/amd64/qrsctl
        chmod +x qrsctl
        sudo cp qrsctl /usr/local/bin/ && echo ok  
```

### 2. 上传之七牛云
```yml
    - name: Upload to Qiniu
      run: | 
        qrsctl login 2092876368@qq.com lfr139931
        qrsctl info
        qrsctl put 111imgbed titles.txt titles.txt
```

### 3. 上传到repo

妈耶，发现能直接上传到本仓库，之前的好多努力都是瞎搞。直接上传到github它不香吗？

```yml
    - name: Upload this repo
      run: |
        git config --global user.name "growvv"
        git config --global user.email "2092876368@qq.com"
        git add titles.md 
        git commit -m 'upload pa result'
        git push -u origin master && echo ok
```

完整的工作流真好看，忍不住截幅图：

![](https://cdn.jsdelivr.net/gh/growvv/img/images/20200209122022.png)



## 四、有待改进
1. 如果能直接上传到本仓库该多好啊【已解决】
2. 爬虫有时会因为超时失败，可以换个爬虫框架试试【已解决】

把下拉3次去掉了，在本程序中没有起到实际作用
