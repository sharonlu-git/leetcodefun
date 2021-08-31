
def reverseList(str):
	strSplit = str.split(" ")
	return strSplit[::-1]

str = "hello world today"
newStr = ' '.join(reverseList(str))
print(newStr)
