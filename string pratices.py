# a = "w3resource.com"
# print(len(a))

# a = "w3resource"
# print(a[0:2] + a[-2:])
def change_char(str1):
    char  = str1[0]
    str1 = str1.replace(char,'$')
    str1 = char +str1[1:]
    return str1
print(change_char('restart'))
