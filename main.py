from flask import Flask, request


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
     <head>
         <style>
             form {{
                 background-color: red;
                 padding: 40px;
                 margin: 0 auto;
                 width: 540px;
                 font: 16px sans-serif;
                 border-radius: 15px;
             }}
             textarea {{0}}
                 margin: 20px 0;
                 width: 540px;
                 height: 120px;
             {{0}}
         </style>
     </head>
     <body>
        <h1>Web Caesar</h1>
        <form method='POST'>
        <label>
             <label for="Rotate by: 0">Rotate by: 0 </label>
             <input id="first-name" type="text" name="first_name" />
             <input type="submit" /> 
           
        </label>
     </body>
            
    </textarea> {{0}}
    
        

"""

@app.route("/")
def index():
    return form.format(...)

@app.route("/" , methods=['POST'])
def encrypt(rot = 0 , text = 0):
    name1 = rot 
    name2 = text
    return form.format(...)
    

if __name__ == "__main__":
    app.run(debug=True)