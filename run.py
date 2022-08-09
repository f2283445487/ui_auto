import json
import keymap
from common import com


def runner(case):
    msg = {'code': 200 , 'm':'执行成功'}
    comm = com()
    if isinstance(case,list):
        for i in case:
            if isinstance(i, str) and i in keymap.func:
                index = case.index(i)
                ele = case[index + 1]
                func = getattr(comm, keymap.func[i])
                if isinstance(ele, list):
                    if len(ele) < 2:
                        func(ele[0])
                    else:
                        func(ele[0], [1])
                else:
                    return json.dumps(msg, ensure_ascii=False)
            else:
                pass

        return json.dumps(msg, ensure_ascii=False)
    # if isinstance(res,dict):
    #     for key in res:
    #         if key[0:2] in keymap.func:
    #             func = getattr(comm,keymap.func[key[0:2]])
    #             if isinstance(res[key], dict):
    #                 key_value = res[key]
    #                 if len(key_value) < 2:
    #                     lis = list(key_value.values())
    #                     func(lis[0])
    #                 else:
    #                     lis = list(key_value.values())
    #                     func(lis[0],lis[1])
    #             else:
    #                 return json.dumps(msg,ensure_ascii=False)
    #         else:
    #             msg['code'] = 500
    #             msg['m']= '方法不存在'
    #             return json.dumps(msg,ensure_ascii=False)
    #     return json.dumps(msg,ensure_ascii=False)
    # if not isinstance(res,dict):
    #     msg['code'] = 400
    #     msg['m']='用例格式错误'
    #     return json.dumps(msg,ensure_ascii=False)

if __name__ == '__main__':
    lit = [
        '打开', ['http://www.baidu.com'],
        '点击', ['//*[@id="hotsearch-refresh-btn"]/span'],
        '等待',[3],
        '点击', ['//*[@id="hotsearch-refresh-btn"]/span'],
        '等待', [3],
    ]
    runner(lit)