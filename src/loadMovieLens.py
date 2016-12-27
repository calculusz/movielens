
import sys
import os

##==================================
#         加载指定的训练集文件
#  参数fileName 代表某个训练集文件
##==================================
def loadMovieLensTrain(fileName='ua.base'):
    str1 = './movielens/'                         # 目录的相对地址

    prefer = {}
    for line in open(str1+fileName,'r'):       # 打开指定文件
        (userid, movieid, rating,ts) = line.split('\t')     # 数据集中每行有4项
        prefer.setdefault(userid, {})      # 设置字典的默认格式,元素是user:{}字典
        prefer[userid][movieid] = float(rating)

    return prefer      # 格式如{'user1':{itemid:rating, itemid2:rating, ,,}, {,,,}}


##==================================
#        加载对应的测试集文件
#  参数fileName 代表某个测试集文件,如u1.test
##==================================
def loadMovieLensTest(fileName='ua.test'):
    str1 = './movielens/'
    prefer = {}
    for line in open(str1+fileName,'r'):
        (userid, movieid, rating,ts) = line.split('\t')   #数据集中每行有4项
        prefer.setdefault(userid, {})
        prefer[userid][movieid] = float(rating)
    return prefer

def loadResult(fileName="result.txt"):
    result={}
    for line in open(fileName,'r'):
        (userid,movieid,rating)=line.split('\\')
        result.setdefault(userid,{})
        result[userid][movieid]=float(rating)
    return result

def loadAllData(fileName="u.data"):
    str1="./movielens/"
    dataset={}
    for line in open(str1+fileName,'r'):
        (userid,movieid,rating,timestamp)=line.split('\t')
        dataset.setdefault(userid,{})
        dataset[userid][movieid]=rating
    return dataset

def loadAllMovie(fileName="u.item"):
    str1="./movielens/"
    datamovie={}
    for line in open(str1+fileName,'r'):
        (movieid,movietitle,releasedate,videorelease,imdb,unknown,action,adventure,animation,child,comedy,crime,documentary,drama,fantasy,file_oir,horror,musical,mystery,romance,sci_fi,thriller,war,western)=line.split('|')
        datamovie.setdefault(movieid)
        datamovie[movieid]=movietitle
    return datamovie

def loadAllUser(fileName="u.user"):
    str1="./movielens/"
    datauser=[]
    for line in open(str1+fileName):
        (userid,age,gender,occupation,zip)=line.split('|')
        datauser.append(userid)
    return datauser



if __name__ == "__main__":
    print ("""这个部分可以进行上面2个函数测试 """)

    trainDict = loadMovieLensTrain()
    testDict = loadMovieLensTest()

    print (len(trainDict))
    print (len(testDict))
    print (""" 测试通过 """)


















