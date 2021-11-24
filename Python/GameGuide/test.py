fullstring="This is jayed. You are jayed"
remov="jayed"



result = "".join(fullstring.rsplit(remov, 1))
print(result)