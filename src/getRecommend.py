from src.getRating import *
from src.loadMovieLens import *
import time
import pickle

def getUserRecommend(userid):
    recommenlist=[]
    data=loadAllData()
    moviedata=loadAllMovie()
    prefer1=loadMovieLensTrain()
    for items in moviedata:
        if(getRating(prefer1,userid,items,20,similarity=sim_pearson)>3):
            recommenlist.append(items)
    return recommenlist

def getAllUserRecommend():
    allrecommendlist={}
    userdata=loadAllUser()
    for user in userdata:
        allrecommendlist.setdefault(user,[])
        allrecommendlist[user]=getUserRecommend(user)

    return allrecommendlist

def calprecision():
    data=loadAllData()
    f=open("recommend.dat",'rb')
    recommenddata=pickle.load(f)
    correct=0
    lens=0
    f.close()
    for user in recommenddata:
        for item in recommenddata[user]:
            lens+=1

            if (item in data[user] and int(data[user][item])>=3):
                correct+=1
    return float(correct/lens)

def calrecall():
    data=loadAllData()
    f=open("recommend.dat",'rb')
    recommenddata=pickle.load(f)
    f.close()
    lens=0
    correct=0
    for user in data:
        for item in data[user]:
            if(int(data[user][item])>=3):
                lens+=1
                if (item in recommenddata[user] ):
                    correct+=1
    return float(correct/lens)

if __name__ == "__main__":
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    data={}
    # all=getAllUserRecommend()
    f=open("recommend.dat",'rb')
    # pickle.dump(all,f)
    data=pickle.load(f)
    f.close()
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    print(calprecision())
    print(calrecall())





