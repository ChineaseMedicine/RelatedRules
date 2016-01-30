import apriori
import os

print os .getcwd()
# dataSet=[line.split() for line in open('recipe_num.txt').readlines()]
dataSet=[line.split() for line in open('F:\\medciinedata\\recipe_num.txt').readlines()]


L,suppData=apriori.apriori(dataSet,minSupport=0.2) #1/2124=0.00047

#file_object=open('F:\\test_result.txt', mode='w')

#strresult = str(suppData)
#file_object.write(strresult)
#file_object.close()
print "ok"
#print 'suppData=',suppData
#print 'L=',L

rules=apriori.generateRules(L,suppData,minConf=0.5)
print 'rules='
print rules

