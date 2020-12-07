from gensim.models import word2vec
import logging

vector_size = 100
def distance(word1, word2):
    distance = 0
    for i in range(vector_size):
        distance = distance + (word1[i] - word2[i]) ** 2
    distance = distance ** 0.5
    return distance

def similarity(word1, word2):
    word1vec, word2vec = model.wv[word1], model.wv[word2]
    return ((10 * maxdis - mindis - 9 * distance(word1vec, word2vec)) / (maxdis - mindis))

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = word2vec.LineSentence('./Train_test_Set/train.txt')

model = word2vec.Word2Vec(sentences, size=100, window=5, sg=1, hs=0, negative=5, iter=10)

model.save('./my_model')
model = word2vec.Word2Vec.load('./my_model')
print(model)

f = open('./Train_Test_Set/pku_sim_test1.txt',encoding='utf-8')
worddic = model.wv.index2word
lines = f.readlines()
mindis = float('inf')
maxdis = float('-inf')

for line in lines:
    str = line.replace('\t',' ').replace('\n','')
    str1, str2 = str.split(" ")
    if str1 in worddic and str2 in worddic:
        maxdis = max(maxdis, distance(model.wv[str1], model.wv[str2]))
        mindis = min(mindis, distance(model.wv[str1], model.wv[str2]))
        print(str1, str2, model.wv.similarity(str1, str2), similarity(str1, str2))
    else:
        print(str1, str2, 1)



