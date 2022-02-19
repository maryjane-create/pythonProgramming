import imaplib
import  pprint


name= 'rofiat'

#print(name[0:4], 'roy' in  name)

for i in name:print('***', i, '***')


animal=['goat', 'cow', 'dog', 'elephant']
animal.sort()
for i in animal:
    print(animal)
    break
print(animal.sort(reverse=True))

print('four score and seven'+  ' years ago')























































































# import  smtplib
#
# smtObj=smtplib.SMTP('smtp.example.com', 587)
# smtObj.ehlo()
# smtObj.starttls()
#
# smtObj.login('bob@example.com', 'MY_SECRET_PASSWORD')
# smtObj.sendmail('bob@example.com', 'alice@example.com', 'Subject:so long ')
# smtObj.quit()



































































#
# while True:
#     print('enter name of cats')
#     name=input()
#     if name=='':
#         print('nope')
#         break
#     cat=cat+[name]
# print('cat names are:')
# for cats in cat:
#     print(''+name)