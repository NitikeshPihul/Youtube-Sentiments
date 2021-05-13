import pickle
from flask import Flask,render_template,request
from CommentSentiment import comment_extract as CE
from CommentSentiment import sentimentYouTube as SYT

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=["POST"])
def predict():
    text=request.form['text']
    start = text.index("=")
    text=text[(start+1):]
    no_comment=request.form['No_comment']
    comments = CE.commentExtract(text, no_comment)
    ans = SYT.sentiment(comments)
    lis=list(ans)
    dic={'sentiment':'weight' , 'positive':lis[0],'negative':lis[1]}
    lis.append(dic)
    return render_template("analysed.html",lis=lis)
    
     
@app.route('/about')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)