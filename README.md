# crawler
使用GitHub Action运行爬虫，并将结果保存到七牛云对象存储。

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

## 二、 上传部分

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

## 三、有待改进
1. 如果能直接上传到本仓库该多好啊
