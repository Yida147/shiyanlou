import json
from flask import Flask, render_template, abort

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    # 显示文章名称的列表
    # 也就是 /home/shiyanlou/files/ 目录下所有 json 文件中的 `title` 信息列表
    with open("../files/helloshiyanlou.json") as f:
        data1 = json.load(f)
    with open("../files/helloworld.json") as f:
        data2 = json.load(f)
    return render_template("index.html",titles={"title1":data1["title"],"title2":data2["title"]})



@app.route('/files/<filename>')
def file(filename):
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
    # 如果 filename 不存在，则显示包含字符串 `shiyanlou 404` 404 错误页面

    if filename not in ["helloshiyanlou","helloworld"]:
        abort(404)
    else:
        with open("../files/{}.json".format(filename)) as f:
            data = json.load(f)
            file_contents = data["content"]
            if "\\\\n" in file_contents:
                new_file_contents = file_contents.split("\\\\n")
            else:
                new_file_contents = file_contents.split("\\n")
        return render_template("file.html",file_contents=new_file_contents)

@app.errorhandler(404)
def not_fond(error):
    return  render_template('404.html') , 404
