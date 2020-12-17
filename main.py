from snownlp import SnowNLP
#for file Dataset
Dataset = open(r"Reviews-Dataset.csv", mode='a', encoding='utf-8')

ReviewsDataset = open(r"Reviews-Dataset.csv", 'r', encoding='utf-8')
# here for read line in dataset file
line = ReviewsDataset.readline()
#num nlp
sum=0
count=0
# run code

while line:
    print('\033[1m'+line, '\n')
    s = SnowNLP(line)
    print('{}'.format(s.sentiments))

    sum+=s.sentiments
    count+=1
    line = ReviewsDataset.readline()

score=sum/count
#print dataset + finalscore
print('finalscore={}'.format(score))
