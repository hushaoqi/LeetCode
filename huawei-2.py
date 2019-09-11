input_str = input().strip()
for i in range(len(input_str)-1):
    if input_str[i:i+2] == '--':  # 找出--分隔符，根据要求3 ，间隔符用两个空格代替
        input_str = input_str[:i] + '  ' + input_str[i+2:]
    if input_str[i] == '-':  # 找出连接符
        if input_str[i-1] == ' ' or input_str[i+1] == ' ':  # 判断是否为合法的连接符
            input_str = input_str[:i] + ' ' + input_str[i+1:]
    if input_str[i] != '-' and (input_str[i] > '9' or input_str[i] < '0'):
        if input_str[i] > 'z' or input_str[i] < 'A':  # 非法字符， 作为间隔处理
            input_str = input_str[:i] + ' ' + input_str[i+1:]
array = input_str.split()
array.reverse()  # 倒序
print(" ".join(array))  # 连接字符
