import json
import keymap
from requests import request
from common import com
from flask import Flask,request


app = Flask(__name__)

@app.route('/ui',methods=['POST'])
def run(driver=None):
    msg = {'code': 200 , 'm':'执行成功'}
    comm = com(driver)
    r = request.get_data()
    res = json.loads(r)
    if isinstance(res,dict):
        for key in res:
            if key[0:2] in keymap.func:
                func = getattr(comm,keymap.func[key[0:2]])
                if isinstance(res[key], dict):
                    key_value = res[key]
                    if len(key_value) < 2:
                        lis = list(key_value.values())
                        func(lis[0])
                    else:
                        lis = list(key_value.values())
                        func(lis[0],lis[1])
                else:
                    return json.dumps(msg,ensure_ascii=False)
            else:
                msg['code'] = 500
                msg['m']= '方法不存在'
                return json.dumps(msg,ensure_ascii=False)
        return json.dumps(msg,ensure_ascii=False)
    if not isinstance(res,dict):
        msg['code'] = 400
        msg['m']='用例格式错误'
        return json.dumps(msg,ensure_ascii=False)

app.run(debug=True,port=8888)

# if __name__ == '__main__':
#     case = {
#         '打开': {'url':'http://www.baidu.com'},
#         '点击1': {'元素':'//*[@id="hotsearch-refresh-btn"]'},
#         '等待': {'时间': 3},
#         '点击2': {'元素':'//*[@id="hotsearch-refresh-btn"]'},
#     }
#
#     run(**case)
