from flask import Flask,render_template,request
import predictions1,predictions2,predictions3

app=Flask(__name__)

diseaseid=0


@app.route('/' ,methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route('/about' ,methods=["GET","POST"])
def about():
    return render_template("about.html")

@app.route('/team' ,methods=["GET","POST"])
def team():
    return render_template("team.html")

@app.route('/input' ,methods=["GET","POST"])
def input():
    return render_template("input.html")
@app.route('/inp1' ,methods=["GET","POST"])
def inp1():
    if request.method=='POST':
        val=request.form.get("my_value")
        diseaseid=val
    return render_template("inp1.html")
@app.route('/inp2' ,methods=["GET","POST"])
def inp2():
    if request.method=='POST':
        val=request.form.get("my_value")
        diseaseid=val
    return render_template("inp2.html")

@app.route('/sel1' ,methods=["GET","POST"])
def sel1():
    return render_template("selection1.html")
@app.route('/sel2' ,methods=["GET","POST"])
def sel2():
    return render_template("selection2.html")

@app.route('/res1' ,methods=["GET","POST"])
def res1():
    if request.method=='POST':
         image = request.files['file']
         image_path = "static/" + image.filename
         image.save(image_path)
         if diseaseid==1:
             pred=predictions1.prediction(path=image_path)
         elif diseaseid==2:
             pred=predictions2.prediction(path=image_path)
         else:
             pred=predictions3.prediction(path=image_path)

    return render_template("res1.html",img=image_path,pred=pred)
@app.route('/res2' ,methods=["GET","POST"])
def res2():
    return render_template("res2.html")




# @app.route('/sub1',methods=["GET","POST"])
# def sub1():
#     if request.method=="POST":
#         image=request.files['imagefile']
#         image_path="static/"+image.filename
#         image.save(image_path)
#         pred=predictions1.prediction(path=image_path)
#     print(pred)
#     return render_template("sub1.html",img=image_path,n=pred)

# @app.route('/sub2', methods=["GET", "POST"])
# def sub2():
#         if request.method == "POST":
#             image = request.files['imagefile']
#             image_path = "static/" + image.filename
#             image.save(image_path)
#             pred = predictions2.prediction(path=image_path)

#         return render_template('sub2.html',img=image_path,n=pred)

# @app.route('/sub3', methods=["GET", "POST"])
# def sub3():
#         if request.method == "POST":
#             image = request.files['imagefile']
#             image_path = "static/" + image.filename
#             image.save(image_path)
#             pred = predictions3.prediction(path=image_path)

#         return render_template('sub3.html',img=image_path,n=pred)



# @app.route('/sub4',methods=["GET","POST"])
# def sub4():
#     if request.method=="POST":

#         userInput1=request.form.get("preg")
#         userInput2=request.form.get("glucose")
#         userInput3 = request.form.get("bpressure")
#         userInput4 = request.form.get("i")
#         userInput5 = request.form.get("bmi")
#         x=[userInput1,userInput2,userInput3,userInput4,userInput5]
#         x=ANNmaleria.ANNdiabetes(x)
#     return render_template("sub4.html",n=x)



# @app.route('/sub5',methods=["GET","POST"])
# def sub5():
#     if request.method=="POST":
#         userInput1 =request.form.get("preg")
#         userInput2 =request.form.get("glucose")
#         userInput3 = request.form.get("bpressure")
#         userInput4 = request.form.get("i")
#         userInput5 = request.form.get("bmi")
#         x=[userInput1,userInput5,userInput4,userInput3,userInput2]
#         x=list(map(int,x))
#         print(x)
#         x = ANNmaleria.ANNdiabetes(x)
#     return render_template("sub5.html",n=x)



# @app.route('/sub6',methods=["GET","POST"])
# def sub6():
#     if request.method=="POST":
#         userInput1=request.form.get("preg")
#         userInput2=request.form.get("glucose")
#         userInput3 = request.form.get("bpressure")
#         userInput4 = request.form.get("i")
#         userInput5 = request.form.get("bmi")
#         x=[userInput1,userInput5,userInput4,userInput3,userInput2]
#         x=ANNmaleria.ANNdiabetes(x)
#     return render_template("sub6.html",n=x)

if __name__=="__main__":
    app.run(debug=True)