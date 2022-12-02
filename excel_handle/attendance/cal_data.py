data = """11-0108:34
打卡打卡打卡
11-0210:12
打卡啦
在做核酸
11-0308:35
打卡打卡
要出门了
11-0408:35
打卡
11-0808:38
鉴于昨天加班，今天特放你不用
打卡
11-0809:46
11-0909:47
打卡打卡了
11-1009:51
退到打卡
28 无照片
11-1108:50
退到打卡
无照片
踩点踩点
没有退到
照片！
嗯？
哦哦
退到了
搞错了
那以后
哈哈哈
都改成9：00
退到好了
YFAN10-3119:25
退出的规则：存的钱大吃一顿，不够各
自补贴。…
没退到
踩点了
喉？
好呢
我一直以为35退到
再去做核酸的路上
11-1108:56
上周退到了两次
这周也退到了两次哟
不过这周可以通过周末补卡
好呢
11-1201:22
28
我累计退到一次
一凡累计退到四次
熬夜各自扣一块钱
11-1408:51
打卡打卡
哎呀
好难过
51
差了几秒
没事，放过你
我打开QQ的时候还是50呢
放你一马
照片呢
交出来
没有照片
我还在衰室呢
你这属于无效打卡
我下了床
洗激好了
算了，今天放过你
没出衰室
11-1508:51
打卡
又和昨天一样
呐，给你
11-1708:50
打卡打卡
照片呦
8
还没出室
刚洗激好
昨天的
今天的
你以为我不知道么
我不管
快上班吧
爱你
3
11-1808:47
打卡打卡
照片呢
一会发
交出来
一会交，快去微信
11-1809:06
不发了吧，我拍了半天
都好丑
11-1908:45
打卡了
11-1909:08
11-2008:49
打卡，无照片
11-21 08:50
打卡了打卡了
QQ美颜过度回
嘻嘻嘻
还没出门
居家记得吃早餐
知道啦
112200:39
晚睡罚款
钱比我重要，我算是看清了
11-2208:58
退到打卡
哈哈哈
11-2311:16
出门打卡
X3
星期四08：50
打卡
星期四08:56
还没出门
刚收拾好
嘴巴上一个小包"""

list_data = data.replace('：', ':').split('\n')
# print(list_data)
lst = list()
lst_repeat = list()
for i, data in enumerate(list_data):
    data = data.replace(' ', '')
    if '-' in data and ':' in data \
            and len(data) <= 12 \
            and data[:5] not in lst_repeat:
        # print(data)
        lst.append(data)
        lst_repeat.append(data[:5])
    elif ':' in data \
            and '星期' in data \
            and data[:3] not in lst_repeat:
        # print(data)
        lst.append(data)
        lst_repeat.append(data[:3])
print(len(lst))
for i, data in enumerate(lst):
    print(data)
# print(lst_repeat)
