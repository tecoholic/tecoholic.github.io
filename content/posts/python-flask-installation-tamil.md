---
title: "Python Flask\u0B90 \u0BA8\u0BBF\u0BB1\u0BC1\u0BB5\u0BC1\u0BB5\u0BA4\u0BC1 \u0B8E\u0BAA\u0BCD\u0BAA\u0B9F\u0BBF?"
date: '2019-09-28T09:00:04'
slug: python-flask-installation-tamil
categories:
  - Python Flask - Tamil
---

இந்தக்கட்டுரை நீங்கள் ஏற்கனவே உங்கள் கணினியில் Python install செய்து வைத்துள்ளீர்கள் எனும் கோணத்தில் இருந்து எழுத்தப்பட்டது. Python உங்கள் கணினியில் இல்லை என்றால், https://www.python.org/downloads/ சென்று, பதிவிறக்கி உங்கள் கணினியில் நிறுவிக்கொள்ளவும்.

1. Python 3
------------



நீங்கள் MacOS அல்லது Linux பயன்படுத்துபவராக இருந்தால் 90% உங்கள் கணினியில் Python 2 இருக்கும். நீங்கள் Python 3-ஐ நிறுவிக்கொள்ளுதல் சிறப்பு.


> ℹ️ அனைத்து விதாமன Operating System-க்கும் Python 3 நிறுவுவது பற்றிய தகவலுக்கு https://realpython.com/installing-python/



உங்கள் கணினியில் உள்ள "Command Line" அல்லது "Terminal" செயலியைத் திறந்து கீழே கொடுக்கப்பட்டுள்ளவற்றை செய்யவும்.

**சிறுகுறிப்பு:** நான் MacOS பயன்படுத்துகிறேன், எனவே என்னுடைய Commandகள், MacOSக்கும், Linuxக்கும் சரியாகப்பொருந்தும். Windows பயன்படுத்துபவர்களுக்கு ஒரு சிலவை வேறு படலாம், கவனத்தில் கொள்ளவும்.

```bash
python --version
```

இது உங்கள் கணினியில் உள்ள கணினியில் இருக்கும் Pythonனின் பதிப்பைக்காட்டும். என்னுடைய இரண்டு கணினிகளின் வெளியீடு இதோ.

![Python Version Check](/img/wp-content/uploads/2019/09/tecoholic_multi_____ssh__and_zsh.png)

ஒன்றில் Python 2 இருப்பதைக்காணலாம். நீங்கள் Python 3 நிறுவினாலும், ஒரு சில சமயம் Python 2வே பிரதானமாக இருக்கும். அப்படி இருந்தால் கவலைப்படத் தேவையில்லை. `python3 --version` என்று அடித்துப்பார்த்து Python 3 இருக்கிறதா என்று சோதித்துக்கொள்ளவும்.

![python3-version.png](/img/wp-content/uploads/2019/09/python3-version.png)
2. Virtual Environment
-----------------------



Flask நிறுவுவதில் முதல் வேலை, அதற்கென தனி ஒரு virtual environemnt-ஐ உருவாக்குவது. இது நம்முடைய project சம்பந்தமான மற்றும் தேவையான விசயங்களை மட்டும் ஒரு இடத்தில் வைத்துக்கொள்ள உதவும். இன்னும் விளக்கமாக்ச்சொன்னால், இன்று நாம் ஒரு இணைய செயலியை எழுத முனைகிறோம், எனவே நாம் Flask நிறுவுகிறோம். நாளை நாம் PyQt துணைகொண்டு ஒரு desktop செயலியை உருவாக்க முயலும் பொழுது அதை நிறுவ வேண்டும். இரண்டுக்கும் சம்பந்தம் கிடையாது, எனவே அவைகளை system Python இல் நிறுவுவதைவிட, நாம் அவைகளுக்கு எனத் தனியாக ஒரு environmentஐ உருவாக்கி அவைகளை தனித்தனியே நிறுவி வைத்துவிட்டோம் என்றால், நாளை எந்த ஒரு மாற்றம் செய்தாலும், அது அந்த ஒரு projectஐ மட்டுமே பாதிக்குமோ தவிற நமதுக் கணினியில் இருக்கும் எல்லாவற்றையும் பாதிக்காது.

என்னடா இவன் "environment" உருவாக்கு என்கிறானே, இதுவே ஒரு பெரிய வேலையாக இருக்கும் போல இருக்கே என்று நீங்கள் பயப்பட வேண்டாம். அதற்கு Python நிறுவும் பொழுது கூடவே வந்த virtualenv என்ற கருவியைப் பயண்படுத்திக்கொள்ளலாம். Command line சென்று, நம் projectக்கு ஒரு directoryயை உருவாக்கி, அதில் ஒரு virtual environment ஐ உருவாக்குங்கள்.

```bash
mkdir flask-project
cd flask-project
virtualenv env --python=python3
```

![create-virtualenv.png](/img/wp-content/uploads/2019/09/create-virtualenv.png)

இப்பொழுது நீங்கள் `ls` என்று உள்ளிட்டுப் பார்த்தீர்களேயானால், அங்கு `env` என்று ஒரு folder இருப்பதைப் பார்க்களாம். இதுவே உங்கள் projectஇன் virtual environment.

3. Flask
---------



இப்பொழுது நாம் உருவாக்கிய virtual environmentக்குள் Flaskஐ நிறுவலாம். முதலில் அதனை activate செய்ய வேண்டும். அப்படி செய்யத்தவறினால், நாம் செய்யும் மாற்றங்கள் எல்லாம் கணினியின் system librariesஐப் பாதிக்கும்.

```bash
source env/bin/activate
```

![venv-ectivated.png](/img/wp-content/uploads/2019/09/venv-ectivated.png)

Activate ஆனவுடன், நம்முடை environmentஇன் பெயர் command lineஇல் முன்னே சேர்ந்து கொண்டதைக்காணலாம். இது நமக்கு நாம் எந்த environmentஇல் வேலை செய்யப்போகிறோம் என்பதைக் காட்டும். இப்பொழுது Flaskஐ நிறுவலாம்.

```bash
pip install Flask
```

![flask_installed.png](/img/wp-content/uploads/2019/09/flask_installed.png)

Flask நிறுவியாயிற்று. அதைக்கொண்டு செயலிகளை எப்படி உருவாக்குவது என்பதை அடுத்து வரும் கட்டுரைகளில் பார்ப்போம்.

உங்களுக்கு இதில் எதேனும் ஐயங்கள் இருந்தால் கீழ பதிவிடவும். நன்றி.

[![Creative Commons Licence](https://i.creativecommons.org/l/by-nc/4.0/88x31.png)](http://creativecommons.org/licenses/by-nc/4.0/)  
This work is licensed under a [Creative Commons Attribution-NonCommercial 4.0 International License](http://creativecommons.org/licenses/by-nc/4.0/).
