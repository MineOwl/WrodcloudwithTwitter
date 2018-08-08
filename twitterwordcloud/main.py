from collections import Counter

from TwitterSearch import TwitterSearch
from japanese_into_english import ja_en_ja
from wordcloud import twodata_into_wordcloud
def main(word):
    searchObj = TwitterSearch(word)
    result = searchObj.search_start(amount = 10)
    del searchObj
    
    resultlist=[]
    print('単語リスト作成中')
    for tweet in result[:20]:
        resultlist.extend(ja_en_ja(tweet))

    counterObj = Counter(resultlist)
    print('htmlファイル作成')
    twodata_into_wordcloud( list(counterObj.keys()),list(counterObj.values()) , minimamnum=0)
        
if __name__=="__main__":
    main('イニエスタ')