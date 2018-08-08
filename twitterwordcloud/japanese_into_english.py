from googletrans import Translator

def ja_en_ja(text):
    japanese=text
    translator = Translator()
    result=translator.translate(japanese,dest='en')

    #print(result.text)
    engwords=(result.text).split(' ')
    return_list=[]

    smallwords=['the', 'be', 'and', 'of', 'a', 'in', 'to', 'have', 'it',"It", 'i', 'that', 'for', 'you', 'he', 'with', 'on', 'do', 'say', 'this', 'they', 'is', 'an', 'at', 'but', 'we', 'his', 'from', 'that', 'not', 'by', 'she', 'or', 'as', 'what', 'go', 'their', 'can', 'who', 'get', 'if', 'would', 'her', 'all', 'my', 'make', 'about', 'know', 'will', 'as', 'up', 'one', 'time', 'has', 'been', 'there', 'year', 'so', 'think', 'when', 'which', 'them', 'some', 'me', 'people', 'take', 'out', 'into', 'just', 'see', 'him', 'your', 'come', 'could', 'now', 'than', 'like', 'other', 'how', 'then', 'its', 'our', 'two', 'more', 'these', 'want', 'way', 'look', 'first', 'also', 'new', 'because', 'day', 'more', 'use', 'no', 'man', 'find', 'here', 'thing', 'give', 'many', 'well']
    for engword in engwords:
        if engword in smallwords:
            continue
        #print(engword)
        jaword = translator.translate(engword,dest='ja')
        return_list.append(jaword.text)
        
    return return_list