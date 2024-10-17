from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello, World!"

@app.route('/armstrong/<int:n>')
def armstrong(n):
    
    sum = 0
    length_n = len(str(n))
    copy_n = n

    while(n>0):
        digit = n % 10  # 8891 jab 10 se divide hoga to remainder bacha ga 1
        sum += digit ** length_n # pir 1 multiply hoga 4 sse 
        n = n//10  # pir 8891 '//' hoga 10 se answer will be 889.1 but show 889 hoga kyoke '//' decimal value ko ignore kar deta ha 
    
    if (sum==copy_n):
        print(f"{copy_n} is an armstrong number")
        result = {
          "number" : copy_n ,
          "armstrong" : True ,
          "Server IP" : "69.69.69"
         }
    
    else:
        print(f"{copy_n} is not an armstrong number") 
        result = {
          "number" : copy_n ,
          "armtrong" : False ,
          "Server IP" : "69.69.69"
         }
      
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)