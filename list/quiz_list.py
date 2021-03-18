def merge(*strings):
    result=''
    for v in result[:-1]:
        result+=v
        result+=', '
    result+='and '+strings[-1]
    return result
final=merge('abc','cde')
print(merge)