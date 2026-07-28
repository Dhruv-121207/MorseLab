from flask import Flask,redirect,render_template,flash,request,url_for,session
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

morse_code_mapping = {"A":".-",
                     "B":"-...",
                     "C":"-.-.",
                     "D":"-..",
                     "E":".",
                     "F":"..-.",
                     "G":"--.",
                     "H":"....",
                     "I":"..",
                     "J":".---",
                     "K":"-.-",
                     "L":".-..",
                     "M":"--",
                     "N":"-.",
                     "O":"---",
                     "P":".--.",
                     "Q":"--.-",
                     "R":".-.",
                     "S":"...",
                     "T":"-",
                     "U":"..-",
                     "V":"...-",
                     "W":".--",
                     "X":"-..-",
                     "Y":"-.--",
                     "Z":"--..",
                     "0":"-----",
                     "1":".----",
                     "2":"..---",
                     "3":"...--",
                     "4":"....-",
                     "5":".....",
                     "6":"-....",
                     "7":"--...",
                     "8":"---..",
                     "9":"----.",
                     "!":"-.-.--",
                     "@":".--.-.",
                     "&":".-...",
                     "(":"-.--.",
                     ")":"-.--.-",
                     "+":".-.-.",
                     "=":"-...-",
                     ":":"---...",
                     "'":".----.",
                     ",":"--..--",
                     "/":"-..-.",
                     "?":"..--..",
                     '"':'.-..-.',
                     " ":"//",
                     ".":".-.-.-",
                     "//":" ",
                     "-":"-....-"
                    }
text_mapping = {v: k for k, v in morse_code_mapping.items()}

def encode_text(text):
    result = ""
    invalid_chars = set()
    for char in text:
        if char in morse_code_mapping:
            result += " " + morse_code_mapping[char]
        else:
            invalid_chars.add(char)
    if invalid_chars:
        return result,f"Invalid characters: {','.join(sorted(invalid_chars))}"

    return result,None

def decode_morse(text):
    result = ""
    invalid_chars = set()
    for char in text.split():
        if char in text_mapping:
            result += "" + text_mapping[char]
        else:
            invalid_chars.add(char)
    if invalid_chars:
        return result,f"Invalid characters: {','.join(sorted(invalid_chars))}"
        
    return result,None

@app.route("/",methods=["POST","GET"])
@app.route("/home",methods=["POST","GET"])
def home():

    text = ""
    result = None

    if request.method == "POST":
        text = request.form.get("text","").strip().upper()
        action = request.form.get("action")

        if action == "encode":
            result,error = encode_text(text)
            if error:
                flash(error,"warning")

        elif action == "decode":
            result,error = decode_morse(text)
            if error:
                flash(error,"warning")
        else:
            return redirect(url_for("home"))

        session['text'] = text
        session['result'] = result
        return redirect(url_for("home"))


    text = session.pop('text', "")
    result = session.pop('result', "")

    return render_template("index.html", text=text, result=result)

if __name__ == "__main__":
    app.run(debug=True)