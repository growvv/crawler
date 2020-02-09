const fs = require('fs')
const marked = require('marked')


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

fs.readFile('./record.md', 'utf-8', (err, data)=>{
    if(err){
        throw err
    }else{
        // 3.使用marked方法，将md格式的文件转化为html格式
        let htmlStr = marked(data.toString());
        // 4.将转化的html格式的字符串，写入到新的文件中
        fs.writeFile('./record.html', htmlStr, err=>{
            if(err){
                throw err
            }else{
                console.log("success")
                console.log(htmlStr)
            }
        })
    }
})
