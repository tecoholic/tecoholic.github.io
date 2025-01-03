---
layout: post
title: "Python Flask என்றால் என்ன?"
date: 2019-09-27 03:05:01
category: Python-flask-tamil
tags: flask python
---

> Python Flask என்பது ஒரு இணைய மென்பொருள்க் குறுங்கட்டமைப்பு.


### இணைய மென்பொருள்க் குறுங்கட்டமைப்பா - என்ன சொல்றீங்க?



Flask ஒரு micro web framework. அது ஒரு web application (இணைய செயலி) எழுதத் தேவையான எல்லா வரைமுறைகளையும் நமக்கு வகுத்துத் தருகிறது. அதே சமயம், அப்படி எழுதப்படும் செயலிகள் எல்லாவற்றிலும் எல்லா செயல்பாடுகளும் உள்ளடங்க வேண்டும் என்ற கட்டாயம் இல்லை. நாம் ஒரே ஒரு கோப்பு (file) கொண்டும் ஒரு முழு செயலியை உருவாக்கலாம், அல்லது ஓராயிரம் கோப்புகள் கொண்டும் உருவாக்காலாம். அது முழுக்க முழுக்க நம் தேவையைப் பொருத்தது.

எடுத்துக்காட்டாக, இந்த 👇 நாங்கே வரிகளில் ஒரு முழு செயலியை உருவாக்கிவிட முடியும்.

```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home:
 return "Hello World!"
```

மேலே உள்ள நிரலை ஒரு கோப்பில் போட்டு நாம் ஒரு webserver-இல் நிறுவி, அதற்கு www.sample-flask-application.com என்ற ஒரு முகவரியையும் கொடுத்துவிட்டோம் என்றால், நாம் எப்பொழுதெல்லாம் அந்த இணைய முகவரிக்குப் போகிறோமோ அப்பொழுதெல்லாம் நமக்கு Hello World! என்னும் செய்தி காத்திருக்கும்.

### அனால் இணையத்தின் மொழி HTML அல்லவா?



என்னது இது? இணைத்தின் பக்கங்கள் HTML-உம் JavaScript, CSS ஆகிய மொழிகளிலும்தானே எழுதப்படும், இவன் என்ன Pythonஐக் கொண்டு வந்து வைத்துக்கொண்டு பிதற்றுகிறான் என்று நீங்கள் யோசிப்பது எனக்குக் கேட்கிறது. நீங்கள் கூறும் மொழிகள் எல்லாம் இணையப்பக்கங்களின் மொழிகள், அதாவது Client Side. நாம் நம் browserஇல் இணையத்தில் இருக்கும் பக்கங்களைப் பார்க்கப் பயன்படும் மொழிகள். இங்கு நாம் பேசிக்கொண்டு இருக்கும் Python என்பது Server Side மொழி. அதாவது client side வரக்கூடிய பக்கங்களை உருவாக்கித்தரும் செயலியை நாம் எழுத Pythonஐப் பயன்படுத்துகிறோம்.

![slice1](/img/wp-content/uploads/2019/09/slice1.png)

Python Flaskஐக் கொண்டு, நாம் HTMLஆல் ஆன பக்கங்களை உருவக்க முடியும். அதை எப்படி செய்வது என்பதை அடுத்து அடுத்து வரும் கட்டுரைகளில் பார்க்கலாம். நன்றி.

[![Creative Commons Licence](https://i.creativecommons.org/l/by-nc/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc/4.0/)  
This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).
