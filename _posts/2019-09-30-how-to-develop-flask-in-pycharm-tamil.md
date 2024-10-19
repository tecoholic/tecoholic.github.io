---
layout: post
title: "PyCharmஇல் Flask செயலி உருவாக்குவது எப்படி?"
date: 2019-09-30 04:30:39
category: Python-flask-tamil
tags: 
---
PyCharm என்பது ஒரு ஒருங்கினைந்த நிரலாக்க மென்பொருள். ஆங்கிலத்தில் Integrated Development Environment (IDE) என செல்லும் ஒரு நிரலாக்கக் கருவி. நாம் செய்யும் வேலையின் தரம் நாம் பயன்படுத்தும் கருவிகளைக்கொண்டே இருக்கிறது. ஒரு சிற்பிக்கு அது நன்றாகத் தெரியும். மென்பொருள் உருவாக்கம் சிலை செதுக்குவதைக் காட்டிலும் கடினமான விடயமா என்று தெரியாது, உறுதியாகச் சிக்கலான ஒன்று என்றே நான் கூறுவேன். எனவே நாம் பயன்படுத்தும் கருவிகளும் அதற்கு நிகரானதாக இருக்கு வேண்டும். Notepad, Notedpad++, Emacs, Eclipse, VIM, Atom, VS Code என பலவற்றில் நிரல் எழுதி இப்பொழுது கடைசி 3 ஆண்டுகளாக வருடம் 7-8ஆயிரம் செலவழித்து Professional Edition வாங்கிப் பயன்படுத்தும் அளவிற்கு உடன் நிற்பது PyCharmதான்.

இனி Python Flask தொடரில் வரும் கட்டுரைகள் எல்லாம் நான் அதிலேயெ எழுதப்போகிறேன். நீங்களும் பயன்படுத்துமாறு கேட்டுக்கொள்கிறேன். (உங்க Mind voice கேக்குது. இல்லை. எனக்கு இதில் எந்த ஆதாயமும் இல்லை)

Flask தொடரில் இதற்கு முன் வந்த கட்டுரைகள்:
1. [Python Flask என்றால் என்ன?](https://arunmozhi.in/2019/09/27/what-is-python-flask/)
2. [Python Flaskஐ நிறுவுவது எப்படி?](https://arunmozhi.in/2019/09/28/python-flask-installation-tamil/)
3. [Flaskஇல் நம் முதல் செயலி](https://arunmozhi.in/2019/09/29/flask-first-application-tamil/)
### என்னாது? 7-8 ஆயிரம் செலவழிக்கனுமா?


**இல்லை.**

PyCharm இல் இரண்டு பதிப்புகள் உள்ளன. ஒன்று காசு கொடுத்து வாங்க வேண்டிய Professional Edition, மற்றொன்று **இலவசமாகக்** கிடைக்கும் Community Edition. இந்த தொடரில் நான் பயன்படுத்தப்போவது எல்லாமே Community Edition தான். இன்னும் ஏன் யோசனை? https://www.jetbrains.com/pycharm/download/

### PyCharm இல்லாமல் இந்தத் தொடரை மேலும் படிக்க முடியாதா?



கண்டிப்பாக முடியும். உங்களுக்கு PyCharm வேண்டாம் என்றால், தாராலமாக உங்களுக்கு பிடித்த கருவிகளைப் பயன்படுத்தாலாம். நாம் Flask கற்றுக்கொள்ள PyCharm அவசியம் கிடையாது. ஆங்காங்கே நான் இடும் படங்கள் PyCharm இன் படங்களாக இருக்க வாய்ப்பு உள்ளது, அதற்கு நிகரான விசயங்களை உங்களுடைய கருவியிலும் பார்த்துக்கொள்ளவும்.

Flask Project உருவாக்கம்
------------------------



PyCharmஐ திறந்து கொள்ளவும்.

![launch-window.png](/img/wp-content/uploads/2019/09/launch-window.png)

அதில் Create New Project-ஐச் சொடுக்கவும்.

![create-project.png](/img/wp-content/uploads/2019/09/create-project.png)

வரும் பெட்டியில் நாம் கொடுக்க வேண்டியது இரண்டு விசயங்கள்:

1. **நம் Project-ஐ எங்கு சேமிக்கப்போகிறோம்.** உங்களுக்கு பிடித்தமான இடத்தை அங்கு கடைசியில் இருக்கு "Browse" பொத்தானை அமுக்கி தேர்வு செய்து கொள்ளவும். புதிதாக ஒரு folder உருவாக்க வேண்டும் எனில் அதை கடைசியில் டைப் செய்து விடுங்கள். எ.கா. என் கணினியில் நான் code எனும் folderஇல் எல்லா projectகளையும் சேர்த்து வைத்து உள்ளேன். அதனால் code எனும் போல்டரை தேர்வு செய்துவிட்டு, `/flaskapp` என்பதை தட்டச்சு செய்துவிட்டேன்.
2. நாம் எந்த Python version ஐப் பயன்படுத்தப்போகிறோம். உங்கள் கணினியில் ஒரே ஒரு Python மட்டும் இருக்கலாம், அல்லாது பலவையும் இருக்கலாம். எனது கணினியைப் பாருங்கள்


![python-interpreters.png](/img/wp-content/uploads/2019/09/python-interpreters.png)

இதில் நாம் எதை நம் செயலி உருவாக்கத்திற்கு பயம்படுத்தப் போகிறோமோ அதைத் தேர்வு செய்ய வேண்டும். நாம் Python 3யைத்தான் இக்கட்டுரைத் தொடரில் பயன்படுத்தவிருக்கிறோம். எனவே Python 3ஐ தேர்வு செய்து கொள்ளுங்கள்.

தேர்வு செய்தவுடன் Create பொத்தானை சொடுக்கவும். இப்பொழுது PyCharm நமக்கான project folderஐ உருவாக்கி அதனுள் ஒரு virutal environmentஐ நமக்கு உருவாக்கித் தந்துவிடும். அது முடிந்தவுடன், PyCharmஇன் project/editor window திறந்து விடும்.

![project-window.png](/img/wp-content/uploads/2019/09/project-window.png)

இதில் நாம் தெரிந்துகொள்ள வேண்டிய இடங்கள் 5.

1. இங்குதான் நாம் நம் தரவுகளை எழுதுவோம்
2. இது நம் projectஇல் உள்ள கோப்புகளை பார்வையிட மற்றும் மாற்றங்கள் செய்ய உதவும் Project Tree
3. நம் project folderக்குள் எதேனும் கட்டளைகள் இட விரும்பினால் அதற்கு தேவையான Terminal. இதின் சிறப்பு என்னவென்றால், நாம் `source env/bin/activate` என்று நமது environmentஐ நாம் activate செய்யத்தேவையில்லை. அது தானாகவே activate ஆகிவிடும். நாம் நேராக நமது வேலையை செய்யலாம்.
4. Python Console - இது உங்களுக்கு எதாவது சிறு சிறு Python வரிகளை சோதித்துப்பாக்க பயன்படும்.
5. Configuration Manager - இங்கு நாம் நமது செயலியை இயக்கிப் பார்க்கத் தேவையானவற்றை பதிவு செய்து, இயக்கி, பிழைகளை கண்டறியும் இடம்.


Flask செயலி எழுதுதல்
--------------------



கீழே உள்ள terminalஐத் திறந்து, Flaskஐ நிறுவும் கட்டளையை இடவும்

```bash
pip install flask
```

![install-flask.png](/img/wp-content/uploads/2019/09/install-flask.png)

அது முடிந்ததும், project treeஇல் உங்கள் project folderஇன் மேல் வலது-"க்ளிக்" செய்து ஒரு புது Python கோப்பை உருவாக்கவும். அதற்கு `app.py` என்று பெயரிடுங்கள்.

![new-file-creation.png](/img/wp-content/uploads/2019/09/new-file-creation.png)

இப்பொழுது திறந்து இருக்கும் அந்த கோப்பில் நம் முதல் செயலிக்கான தரவைப் தட்டச்சு செய்து கொள்ளுங்கள்.

```py
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
 return "Hello World!"
```

நீங்கள் தட்டச்சு செய்யும் பொழுதே PyCharm உங்களுக்கு உதவ ஆரம்பிப்பதைக் காணலாம்.

![type-suggestions.png](/img/wp-content/uploads/2019/09/type-suggestions.png)

முழு தரவையும் தட்டச்சு செய்தவுடன் "Save" செய்து கோப்பை பத்திரப்படுத்திவிடவும்.

![hello-world.png](/img/wp-content/uploads/2019/09/hello-world-1.png)
செயலியை இயக்கி சோதிப்பது
------------------------



வலதுபுறம் மேலே உள்ள "Add Configuration" பொத்தானை சொடுக்கவும். உடனே அது ஒரு New Configuration பெட்டியத் திறக்கும்.

![new-configuration.png](/img/wp-content/uploads/2019/09/new-configuration.png)

இதில் உள்ள + குறியை சொடுக்கி ஒரு Python configurationஐ உருவாக்கவும்.

![new-config-create-menu.png](/img/wp-content/uploads/2019/09/new-config-create-menu.png)

அங்கு நிங்கள் செய்ய வேண்டியவை 4

![filled-config.png](/img/wp-content/uploads/2019/09/filled-config.png)
1. Script Pathஇல் உள்ள folder பொத்தானை சொடுக்கி உங்கள் projectக்குள் இருக்கும் virtual environment (venv)க்குள் bin -> flask என்பதைத் தேர்வு செய்து கொள்ளவும்.
2. Parametersஇல் run எனத் தட்டச்சு செய்யவும்.
3. Environment Variablesஇல் `FLASK_APP=app;FLASK_ENV=development;` என்பதைச் சேர்க்கவும்.
4. Nameஇல் "Dev Server" என்று கொடுக்கவும்



அதை OK கொடுத்து மூடி விடவும். இப்பொழுது Dev Sever என்று ஒரு Configuration உங்களுக்கு உருவாகி இருக்கும். அதன் அருகில் உள்ள run பொத்தானை அமுக்கினால், நம்முடைய Flask server வேலை செய்ய ஆரம்பிப்பதைக் காணலாம்.

![run-button.png](/img/wp-content/uploads/2019/09/run-button.png)
![run-window.png](/img/wp-content/uploads/2019/09/run-window.png)

இதில் Flaskஇன் server ஆரம்பமாகி, நம்முடைய செயலியை நாம் பார்க்க செல்ல வேண்டிய முகவரி இருக்கும். அந்த முகவரியை சொடுக்கினால், சென்ற கட்டுரையைப் போலவே நமக்கு Hello World எனும் செய்தி காத்திருக்கும்.

### முடிவுரை



ஒரு terminalஐயும் text editorஐயும் வைத்து செய்த வேலையை இப்படி என்ன என்னமோ configuration எல்லாம் செய்து பயன்படுத்த வேண்டுமா என்று நினைத்தால், கவலைப்படாதீர்கள். இந்த ஒரு முறை இதை செய்து விட்டோம் என்றால் அடுத்த முறை நாம் எதுவும் செய்ய வேண்டியது இல்லை.

![relaunch.png](/img/wp-content/uploads/2019/09/relaunch.png)

திறந்தவுடன் நமக்கு நம்முடைய project காட்டும். சோதித்துப்பார்க்க நாம் நேரடியாக Dev sever ஐ ஆரம்பிக்காலாம். வேலை முடிந்ததும் மூடி விடலாம். Text Editor, terminal, virtual environment activate செய்வது, Flask app பதிவிட்டு பிறகு run செய்வது என பல விசயங்களில் கவனம் சிதறவிடத் தேவையில்லை.

உங்களுக்கு இதில் எதேனும் ஐயங்கள் இருந்தால் கீழ பதிவிடவும். நன்றி.

[![Creative Commons Licence](https://i.creativecommons.org/l/by-nc/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc/4.0/)  
This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).
