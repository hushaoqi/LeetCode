#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        a = line.split()
        print(int(a[0]) + int(a[1]))