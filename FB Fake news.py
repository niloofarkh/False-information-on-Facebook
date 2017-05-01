
get_ipython().magic(u'matplotlib inline')


data = []
first_line = True
typeCount = {'video':{'true':0,'false':0,'mix':0},'photo':{'true':0,'false':0,'mix':0},'link':{'true':0,'false':0,'mix':0},'text':{'true':0,'false':0,'mix':0}}
falseReactions = {'share':0,'like':0,'comment':0}
trueReactions = {'share':0,'like':0,'comment':0}
mixReactions = {'share':0,'like':0,'comment':0}
shareCountsOfFalseNews={'video':0,'photo':0,'link':0,'text':0}
shareCountsOfTrueNews={'video':0,'photo':0,'link':0,'text':0}
shareCountsOfMixNews={'video':0,'photo':0,'link':0,'text':0}
firstLine = True
falseCount = 0
trueCount = 0
mixCount = 0
with open('/home/nell/facebook-fact-check.csv','r') as f:
	for line in f:
		#if firstLine:
		#	firstLine = False
		#	break

		tmp = line.split('\n')[0]
		elements = tmp.split(',')
		data.append([elements[6],elements[7],elements[9],elements[10],elements[11]])
		#print elements
		
		postType = elements[6]
		commentCount = (elements[11])
		reactionCount = (elements[10])
		shareCount = (elements[9])
		

		if 'mostly true' in elements:
			typeCount[postType]['true'] = typeCount[postType]['true']+1 
			
			if shareCount is not '': 
				trueReactions['share'] = trueReactions['share']+int(shareCount)
				shareCountsOfTrueNews[postType] = shareCountsOfTrueNews[postType]+int(shareCount)
			if reactionCount is not '':
				trueReactions['like'] = trueReactions['like']+int(reactionCount)
			if commentCount is not '':
				trueReactions['comment'] = trueReactions['comment']+int(commentCount)
			
			trueCount=trueCount+1

		elif 'no factual content' in elements:
			typeCount[postType]['false'] = typeCount[postType]['false']+1
			
			if shareCount is not '': 
				falseReactions['share'] = falseReactions['share']+int(shareCount)
				shareCountsOfFalseNews[postType] = shareCountsOfFalseNews[postType]+int(shareCount)
			if reactionCount is not '':
				falseReactions['like'] = falseReactions['like']+int(reactionCount)
			if commentCount is not '':
				falseReactions['comment'] = falseReactions['comment']+int(commentCount)
			
			falseCount = falseCount+1

		elif 'mixture of true and false' in elements:
			typeCount[postType]['mix'] = typeCount[postType]['mix']+1
			
			if shareCount is not '': 
				mixReactions['share'] = mixReactions['share']+int(shareCount)
				shareCountsOfMixNews[postType] = shareCountsOfMixNews[postType]+int(shareCount)
			if reactionCount is not '':
				mixReactions['like'] = mixReactions['like']+int(reactionCount)
			if commentCount is not '':
				mixReactions['comment'] = mixReactions['comment']+int(commentCount)
			
			mixCount = mixCount+1

f.close()
print '**********************type counts*************************************'
print '***********************False*****************************************'
print shareCountsOfFalseNews
print '***********************True*****************************************'
print shareCountsOfTrueNews
print '***********************Mix*****************************************'
print shareCountsOfMixNews
print '***********************PHOTOS*****************************************'
print typeCount['photo']
print '***********************VIDEO******************************************'
print typeCount['video']
print '***********************LINK*******************************************'
print typeCount['link']
print '***********************TEXT*******************************************'
print typeCount['text']
print '*****************FALSE REACTIONS**************************************'
print falseReactions
print '*****************True REACTIONS***************************************'
print trueReactions
print '*****************MIX REACTIONS****************************************'
print mixReactions
print '************************COUNTS****************************************'

falseCnt = 0
for key in typeCount.keys():
	falseCnt = falseCnt + typeCount[key]['false']

print 'num of true news:'+str(trueCount)
print 'num of false news:'+str(falseCount)
print falseCnt
print 'num of mix news:'+str(mixCount)


#print data
videoFalseFrac=float(typeCount['video']['false'])/(typeCount['video']['false']+typeCount['video']['true']+typeCount['video']['mix'])
linkFalseFrac=float(typeCount['link']['false'])/(typeCount['link']['false']+typeCount['link']['true']+typeCount['link']['mix'])
textFalseFrac=float(typeCount['text']['false'])/(typeCount['text']['false']+typeCount['text']['true']+typeCount['text']['mix'])
photoFalseFrac=float(typeCount['photo']['false'])/(typeCount['photo']['false']+typeCount['photo']['true']+typeCount['photo']['mix'])
percentage=[photoFalseFrac, videoFalseFrac, linkFalseFrac, textFalseFrac]
print percentage
import matplotlib.pyplot as plt
xticks=['photo','video','link','text']
x=[1,2,3,4]
plt.bar(x,percentage,align='center')
plt.xticks(x,xticks)
plt.legend()
plt.title('Fraction of Fake news in different categories')
plt.show()
y=[falseReactions['share'],falseReactions['comment'],falseReactions['like']]
print y
xticks=['share','comment','reaction']
x=[1,2,3]
plt.bar(x,y,align='center')
plt.xticks(x,xticks)
plt.legend()
plt.title('number of shares, comments, and likes of fake news')
plt.show()





