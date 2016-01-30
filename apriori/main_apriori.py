import apriori
import os
import codecs

print os .getcwd()
# dataSet=[line.split() for line in open('recipe_num.txt').readlines()]
# dataSet=[line.split() for line in open('F:\\medciinedata\\recipe_num.txt').readlines()]

#f=codecs.open('C:\\Users\\GYN\\Desktop\\lxx\yibin_data\\drug_allClass1.txt','r','utf-8')
#f=codecs.open('C:\\Users\\GYN\\Desktop\\lxx\yibin_data\\SourceDrugResult20160124.txt','r','utf-8')

#dataSet=[line.split() for line in f.readlines()]
#f.close()

dataSet=[line.split() for line in open('C:\\Users\\GYN\\Desktop\\lxx\yibin_data\\SourceDrugNum20160125_asc.txt').readlines()]

# code by Adu
#dataSet = reduce(lambda x,y:x|y,[set(i.strip().split(',')) for i in open('C:\\Users\\GYN\\Desktop\\lxx\yibin_data\\drug_allClass.txt')])

print dataSet

#//  test print utf-8 data into chinese character
#f2 = codecs.open('C:\\Users\\GYN\\Desktop\\lxx\yibin_data\\apriori_result\\testwrite.txt','a','utf-8')
#for line in dataSet:
    #f2.writelines(str(line).encode('gbk')+'\n')

L,suppData=apriori.apriori(dataSet,minSupport=0.0005) #1/2124=0.00047

#file_object=open('F:\\test_result.txt', mode='w')

#strresult = str(suppData)
#file_object.write(strresult)
#file_object.close()
print "ok"
#print 'suppData=',suppData
#print 'L=',L

rules = apriori.generateRules(L,suppData,minConf=0.0005)

#decodedRules = rules.decode("unicode-escape")   
        
print 'rules='
print rules
#print decodedRules

