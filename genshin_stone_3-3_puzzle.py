# coding: UTF-8
import itertools
import numpy as np
from numpy.core.fromnumeric import trace

'''
原神の珊瑚宮南西ワープすぐそばにあった３×３のパズルを解く奴
北は1、東は2、南は3、西は4
石なしの数値幅は 1-4
石つきの数値幅は 5-8

標準入力を受け付けず
コード内の数字を直接触って動かす程度には使いやすくしてない（早く完成させたかったため）
'''

def list_same_judge(tmp_list):
    same_flag = []
    for i in range(1, len(tmp_list)):
        if tmp_list[0] == tmp_list[i]:
            same_flag.append(True)
        else:
            same_flag.append(False)
    if False not in same_flag:
        return True
    else:
        return False

ans_num = [0, 0, 0, 0]
num = list(range(1, 5))
num_stone = list(range(5, 9))
# 総当たりの作成
num_pattern = list(itertools.product(num, num_stone, num, num_stone))
gyo_sum = []
retsu_sum = []

for num in num_pattern:
    ans_num = num
    question = [
        [ans_num[0], 7, ans_num[1]],
        [9, 5, 1],
        [ans_num[2], 3, ans_num[3]],
    ]

    tmp_list = question
    
    # 行合計
    gyo_sum = np.sum(tmp_list, axis = 1)
    
    # 列合計
    retsu_sum = np.sum(tmp_list, axis = 0)
    
    # ＼方向合計（対角和）
    trace_sum = np.trace(tmp_list)
    
    # ／方向合計
    # この方向に合計するメソッドはないので左右反転させて＼方向で合計する
    tmp_list_fliplr = np.fliplr(tmp_list)
    trace_sum_flip = np.trace(tmp_list_fliplr)

    if list_same_judge(gyo_sum) and list_same_judge(retsu_sum) and trace_sum == trace_sum_flip:
        print(tmp_list)
        print("行：" + str(gyo_sum))
        print("列：" + str(retsu_sum))
        print("＼：" + str(trace_sum))
        print("／：" + str(trace_sum_flip))
        print("★答えは" + str(ans_num) + "です")
