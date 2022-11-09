tamaalHostelClient={'name':'Gyavira','roomNo':420,'rentPaid':'Yes'}
tamaalHostelClient['phone']= '+254700300152'
#print(tamaalHostelClient['name'])
#print(tamaalHostelClient.get('phone'))
tamaalHostelClient.update({'name':'Musya','roomNo':504,'phone':+254757405701,'rentPaid':'No'})
del tamaalHostelClient['rentPaid']
print(tamaalHostelClient.items())
for key,value in tamaalHostelClient.items():
    print(key,value)