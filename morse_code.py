def morse_code(s):
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
                     "//":" "
                    }
    
    translated_text = ""
    mcs = s.split()

    if s[0] in morse_code_mapping.keys() and s[0] != ".":
        for char in s:
            translated_text += " " + morse_code_mapping[char]
    
    if s[0] in morse_code_mapping.values():
        for char in mcs:
            for key,val in morse_code_mapping.items():
                if char == val:
                    translated_text += "" + key

    return translated_text 
    
text = input("Enter text:").upper()
print(morse_code(text))