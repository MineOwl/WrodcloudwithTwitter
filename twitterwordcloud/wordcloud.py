import re
import webbrowser
import os
def cleanText(input_text,deleng=True):
    input_text = input_text.replace("\n", "")
    input_text = input_text.replace(r'\\', "")
    input_text = input_text.replace("\"", "")
    for punc in [',','.','!','"','$',';',':','[','/','{','}','(',')',"'",'-','=','_',' ','|',']','?','&','<','>']:
        input_text=input_text.replace(punc,'')

    html_mark=['<','>',"/"]
    for symbol in html_mark:
        input_text=input_text.replace(symbol,"")
            
    #ここからは英語の削除
    input_text=re.sub(r'([a-z]+)|([A-Z]+)|([0-9]+)','',input_text)
    return input_text

def twodata_into_wordcloud(words ,numbers ,minimamnum=0):
    code="["
    for word,num in zip(words,numbers):
        if num > minimamnum:
            word = cleanText(word)
            add='["'+word+'",'+str(num)+"],"+'\n'
            code+=add
    code = code[:-1]
    code+="]"

    htmlcode=u"""<!DOCTYPE html>
        <html>
        <head>
            <meta charset='utf-8'>
            <style>
                #cloud { border-radius:3px;border:1px solid #d0d0d0; }
                #cloud span { cursor: pointer; }
            </style>
        </head>
        <body>
            <div id='cloud' style="width:640px;height:450px;position:relative;"></div>
            <div id="details" style="width:640px;text-align:center;line-height:2em;margin-top:0.5em"></div>
            <script src='wordcloud2.js'></script>
            <script>"""
    htmlcode+=u"var tags ={};\n".format(code)
    htmlcode+=u"""WordCloud(document.getElementById('cloud'), {
                list : tags.map(function(word) { return [word[0], 10*Math.round(word[1])]; })
                });

                var clicked = function(ev) {
                if (ev.target.nodeName === "SPAN") {
                    var tag = ev.target.textContent;
                    var tagElem;
                    if (tags.some(function(el) { if (el[0] === tag) {tagElem = el; return true;} return false; })) {
                    location.href='https://twitter.com/search?q='+tag
                    document.getElementById("details").innerText = "There were " + tagElem[1] + 
                        " Stack Overflow questions tagged \\"\" + tag + "\\"\";
                    }
                } else {
                    document.getElementById("details").innerText = "";
                }
                }
                document.getElementById("cloud").addEventListener("click", clicked)
            </script>
        </body>
        </html>"""
    #print(htmlcode)


    file_path = './CloudHtmls/cloud.html'
    with open(file_path,"w+") as f:
        f.write(htmlcode)
    
    file_path='file://{}/CloudHtmls/cloud.html'.format(os.getcwd())
    webbrowser.open_new_tab(file_path)
