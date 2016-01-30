'''
Created on Mar 24, 2011
Ch 11 code
@author: Peter
'''
from numpy import *

def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

#----------------------------------------------------------------------
def sortedDictValues(adict):
    keys=adict.keys()
    keys.sort()
    return map(adict.get,keys)
    

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
                
    C1.sort()
  #  print 'C1=',C1
    return map(frozenset, C1)#use frozen set so we
                            #can use it as a key in a dict    

count=1
strIndex="Property1"
def scanD(D, Ck, minSupport):
    global count
    global strIndex
    # print to a file
    for i in range(count-1):
        strIndex=strIndex+"\tProperty"+str(i+1)
        print i
        print strIndex
     
    #file_object=open('F:\\test_result.txt', mode='a')
    
   # # strtitle ="\n\n---------------------------------------------------------------"+"\n"+"No.\t"+strIndex+"\t SupportNum\t SupportRate\n"
    #strtitle=strIndex+"\t SupportNum\t SupportRate\n"
    #print strtitle
    #file_object.write(strtitle)
    #file_object.close()    
 #   global index=1
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not ssCnt.has_key(can): ssCnt[can]=1
                else: ssCnt[can] += 1
    numItems = float(len(D))
    retList = []
    supportData = {}
       
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support # type a 'Tab',just save keys whose supportData>=support
   #     print key,"-->",ssCnt[key],"-->",support
   # data2=sortedDictValues(supportData)
    #print data2
    
    #print numItems #2124
    print "------------------"
    datalist_sn=sorted(ssCnt.items(), lambda x, y: -cmp(x[1], y[1]))         # sort by support num,reverse sort
    datalist_sr=sorted(supportData.items(), lambda x, y: -cmp(x[1], y[1]))       # sort by support rate,reverse sort
    
    #strProperty='Property',index
   # strProperty=index # ??????????????????????????????????
    #print strProperty
    #index+=1
    # ---------------print frequent item into text---------------
    print 'datalist_sn=',len(datalist_sn)
    print 'datalist_sr=',len(datalist_sr)
    for i in range(0,len(datalist_sn)):
        # filename="F:\\test_result" +str(count)+".txt"  
        filename="C:\\Users\\GYN\\Desktop\\lxx\\yibin_data\\apriori_result\\xitem" +str(count)+".txt" 
        #file_object=open(filename,mode='a+')        
        strresult1 = str(datalist_sn[i][0])
        
        slashUStr = strresult1;
        decodedUniChars = slashUStr.decode("unicode-escape")     
        
        strresult2=str(datalist_sn[i][1])
        #strresult4=str(datalist_sr[i][0])
        #slashUStr4 = strresult4;
        #decodedUniChars4 = slashUStr4.decode("unicode-escape")         
        
        strresult3=str(datalist_sr[i][1])
        strresult=str(i+1)+"\t"+strresult1+'\t'+strresult2+'\t'+strresult3
    #    strresult=str(i+1) + "\t" + decodedUniChars + '\t' + strresult2 + '\t' + strresult3

        print strresult
        #file_object.write(strresult)
        #file_object.write('\n')
        #file_object.close()  
        
    print "111111111111111111111"
    print supportData
    print "next"
  #  print index,"-->",supportData
  #  print "aaa",supportData
  #  index+=1
  
    count+=1
    print count
    return retList, supportData

def aprioriGen(Lk, k): #creates Ck
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk): 
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            L1.sort(); L2.sort()
            if L1==L2: #if first k-2 elements are equal
                retList.append(Lk[i] | Lk[j]) #set union
    return retList

def apriori(dataSet, minSupport):
     #-----------add a index to count for properties----in function ScanD------
    global index
    index=1    
    C1 = createC1(dataSet)
    D = map(set, dataSet)
        
    L1, supportData = scanD(D, C1, minSupport)
        
   # print supportData
    
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)#scan DB to get Lk
   #     print supK
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData

def generateRules(L, supportData, minConf):  #supportData is a dict coming from scanD
    bigRuleList = []
    for i in range(1, len(L)):#only get the sets with two or more items
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, minConf)
            else:
                calcConf(freqSet, H1, supportData, bigRuleList, minConf)
    return bigRuleList         

def calcConf(freqSet, H, supportData, brl, minConf):
    prunedH = [] #create new list to return
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq] #calc confidence
        if conf >= minConf: 
            print freqSet-conseq,'-->',conseq,'conf:',conf
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, supportData, brl, minConf):
    m = len(H[0])
    if (len(freqSet) > (m + 1)): #try further merging
        Hmp1 = aprioriGen(H, m+1)#create Hm+1 new candidates
        Hmp1 = calcConf(freqSet, Hmp1, supportData, brl, minConf)
        if (len(Hmp1) > 1):    #need at least two sets to merge
            rulesFromConseq(freqSet, Hmp1, supportData, brl, minConf)
            
def pntRules(ruleList, itemMeaning):
    for ruleTup in ruleList:
        for item in ruleTup[0]:
            print itemMeaning[item]
        print "           -------->"
        for item in ruleTup[1]:
            print itemMeaning[item]
        print "confidence: %f" % ruleTup[2]
        print       #print a blank line
        
            
'''from time import sleep
from votesmart import votesmart
votesmart.apikey = 'a7fa40adec6f4a77178799fae4441030'
#votesmart.apikey = 'get your api key first'
def getActionIds():
    actionIdList = []; billTitleList = []
    fr = open('recent20bills.txt') 
    for line in fr.readlines():
        billNum = int(line.split('\t')[0])
        try:
            billDetail = votesmart.votes.getBill(billNum) #api call
            for action in billDetail.actions:
                if action.level == 'House' and \
                (action.stage == 'Passage' or action.stage == 'Amendment Vote'):
                    actionId = int(action.actionId)
                    print 'bill: %d has actionId: %d' % (billNum, actionId)
                    actionIdList.append(actionId)
                    billTitleList.append(line.strip().split('\t')[1])
        except:
            print "problem getting bill %d" % billNum
        sleep(1)                                      #delay to be polite
    return actionIdList, billTitleList
    '''
        
def getTransList(actionIdList, billTitleList): #this will return a list of lists containing ints
    itemMeaning = ['Republican', 'Democratic']#list of what each item stands for
    for billTitle in billTitleList:#fill up itemMeaning list
        itemMeaning.append('%s -- Nay' % billTitle)
        itemMeaning.append('%s -- Yea' % billTitle)
    transDict = {}#list of items in each transaction (politician) 
    voteCount = 2
    for actionId in actionIdList:
        sleep(3)
        print 'getting votes for actionId: %d' % actionId
        try:
            voteList = votesmart.votes.getBillActionVotes(actionId)
            for vote in voteList:
                if not transDict.has_key(vote.candidateName): 
                    transDict[vote.candidateName] = []
                    if vote.officeParties == 'Democratic':
                        transDict[vote.candidateName].append(1)
                    elif vote.officeParties == 'Republican':
                        transDict[vote.candidateName].append(0)
                if vote.action == 'Nay':
                    transDict[vote.candidateName].append(voteCount)
                elif vote.action == 'Yea':
                    transDict[vote.candidateName].append(voteCount + 1)
        except: 
            print "problem getting actionId: %d" % actionId
        voteCount += 2
    return transDict, itemMeaning
