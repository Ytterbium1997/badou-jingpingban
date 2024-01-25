#week3作业

#词典；每个词后方存储的是其词频，词频仅为示例，不会用到，也可自行修改
Dict = {"经常":0.1,
        "经":0.05,
        "有":0.1,
        "常":0.001,
        "有意见":0.1,
        "歧":0.001,
        "意见":0.2,
        "分歧":0.2,
        "见":0.05,
        "意":0.05,
        "见分歧":0.05,
        "分":0.1}

#待切分文本
sentence = "经常有意见分歧"
#目标输出;顺序不重要
target = [
    ['经常', '有意见', '分歧'],
    ['经常', '有意见', '分', '歧'],
    ['经常', '有', '意见', '分歧'],
    ['经常', '有', '意见', '分', '歧'],
    ['经常', '有', '意', '见分歧'],
    ['经常', '有', '意', '见', '分歧'],
    ['经常', '有', '意', '见', '分', '歧'],
    ['经', '常', '有意见', '分歧'],
    ['经', '常', '有意见', '分', '歧'],
    ['经', '常', '有', '意见', '分歧'],
    ['经', '常', '有', '意见', '分', '歧'],
    ['经', '常', '有', '意', '见分歧'],
    ['经', '常', '有', '意', '见', '分歧'],
    ['经', '常', '有', '意', '见', '分', '歧']
]


#实现全切分函数，输出根据字典能够切分出的所有的切分方式
def all_cut(sentence, Dict, start=0, segmented=[]):
    # 如果起始位置已经到达句子末尾，返回当前分词结果
    if start == len(sentence):
        return [segmented]


    segments = []
    # 遍历从当前位置到句尾的所有子字符串
    for end in range(start + 1, len(sentence) + 1):
        # 检查当前子字符串是否在词典中
        print(end)
        word = sentence[start:end]
        if word in Dict:
            # 如果在词典中，递归调用full_segmentation处理剩余的字符串
            new_segments = all_cut(sentence, Dict, end, segmented + [word])
            segments.extend(new_segments)

    return segments

# 进行全切分
all_segmentations = all_cut(sentence, Dict)


# 输出所有可能的分词结果
for segmentation in all_segmentations:
    print(' '.join(segmentation))