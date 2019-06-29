from flask import Flask,render_template,request,redirect
from bs4 import BeautifulSoup
import requests,random

app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('base.html')


@app.route('/quotes',methods=['GET','POST'])
def quotes():
    url = 'https://writingcooperative.com/18-motivational-quotes-to-bring-out-the-writer-in-you-ea3e61c93734'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html5lib')
    m=soup.find_all('blockquote')
    l=[]
    for i in m:
        j=i.get_text()
        l.append(j)
    impo=random.choice(l)
    index=l.index(impo)
    if "—" in impo:
        imp=l[index+1]
        writer=l[index+2]
    else:
        imp=impo
        writer=l[index+1]
    print(impo)
    print(imp)
    print(writer)
    return render_template('quotes.html',imp=imp,writer=writer)


if __name__ == '__main__':
    app.run(debug=True)
