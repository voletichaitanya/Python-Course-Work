import re
res = re.match(r'[a-z]','hello world')
print(res.group() if res else "No Pattern")

res1 = re.match(r'[A-Z]+','Hello World')
print(res1.group() if res1 else "No Pattern")

res2 = re.match(r'\d+','188hello world')
print(res2.group() if res2 else "No Pattern")

res3 = re.match(r'\d{2}','188hello world')
print(res3.group() if res3 else "No Pattern")

res4 = re.match(r'[0-9]{2}','ds-da-15-14')
print(res4.group() if res4 else "No Pattern")


find = re.findall(r'[0-9]{2}','PFS-30 & PFS-31 & ds-da-15-14')
print(find)

print()
finditer = re.finditer(r'[0-9]{2,}','46 16 74PFS- 14 30 & PFS-31 & ds-da-15-14')

for i in finditer:
    print(i.group(),i.start())

print()
fullmatchs = re.fullmatch(r'(aeiou)+','aeiou')
print(fullmatchs.group())
print()

phone = re.fullmatch(r'^[6-9]\d{9}','9876543210')
print(phone.group() if phone else "No Pattern")
print()

python = re.findall(r'p..h.n','python ptyhjn perhkn pytxon')
print(python)


space = re.findall(r'\s\s\w','  hello  hii  how  are  you df')
print(space)
print()

split = re.split(r'[,;"-]','python,pythonx;pythonvk"psxhin-python pthon')
print(split)
print()

sub = re.sub(r'[aeiouAEIOU]',' *0* ','python programming chaitanya')
print(sub)

subs = re.sub(r'[A-Z]','*','PyJthon pNrJDrammSing chaEiGtSGaHnya')
print(subs)

pattern = re.search(r'[a-z]*[0-9]$','hello world7')
print(pattern.group() if pattern else "No Pattern")
print()

boundary = re.findall(r'\b\d{2}\b','34 23 52 7  89 76 67 344 23 879 456 987 234')
print(boundary)


# fullname = r'^[A-Za-z]{2,25} ( [A-Za-z]{2,25})+$'    chaitanya voleti
# email_pattern = r'^[a-zA-Z0-9._]+@[0-9a-zA-Z]+\.[a-zA-Z]{2,3}$'  chaitu@gmail.com
# phone_number = r'^(?:\+91|0)?[6-9]\d(9)$'
# password = r'^(?=.*[A-Z]) (?=.*[a-z]) (?=.*\d) (?=.*[@$!%*?&]) [A-Za-z\d@$!%*?&] {8,}$'
