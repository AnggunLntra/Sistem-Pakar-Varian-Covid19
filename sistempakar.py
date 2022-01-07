from flask import Flask, session, redirect, url_for, render_template, request, escape
app = Flask(__name__)
app.secret_key = 'isinya password buat session'
app.static_folder = 'static'

daftarGejala = ['demam','batuk','kehilangan indera perasa','sesak napas','sulit berpikir jernih','pusing','mailase','mual','kelelahan dan nyeri otot','batuk terus menerus','sakit perut','batuk kering','flu','muntah','gangguan pendengaran','hilang selera makan','mulut kering','ruam disekujur tubuh','mata merah dan berair','suhu tinggi','kehilangan atau perubahan pada indera perasa dan penciuman','kelelahan','keringat di malam hari','tenggorokan gatal','Sakit kepala','hilangnya indera penciuman','sakit tenggorokan','nyeri sendi','pegal-pegal']
daftarVirus = ['alpha','beta','gamma','delta','lambda','kappa','eta','mu','omicron']
gejala = 0

def checkGejala():
    if request.form.get('pilihan') == 'ya':
      return True
    if request.form.get('pilihan') == 'tidak':
      return False
    else:
        return checkGejala()

@app.route('/')
def index():
   session.pop('namaPasien', None)
   session.pop('gejalaPasien', None)
   session.pop('logs', None)
   session.pop('logs2', None)
   session['gejalaPasien'] = 0
   session['logs'] = 0
   session['logs2'] = 0
   return render_template('index.html', link = url_for('index'))

@app.route('/welcome',methods = ['POST', 'GET'])
def welcome():
   if request.method == 'POST':
      name = request.form.get('Name')
      session['namaPasien'] = name
      gejalanya = session['gejalaPasien']
      pertanyaan = daftarGejala[gejalanya]
      return render_template("welcome.html", name = name,  pertanyaan = pertanyaan, link = url_for('index'))

@app.route('/result',methods = ['POST', 'GET'])
def result():
   name = session['namaPasien']
   if request.method == 'POST':
      #=============================================================Logs 0
      if session['logs'] == 0 and checkGejala():
         if session['gejalaPasien'] == 0: #  P1
            session['gejalaPasien'] = 1
            session['logs'] = 1
            return redirect(url_for('diagnosa'))
      #=============================================================Logs 1
      elif session['logs'] == 1  and checkGejala():
         if session['gejalaPasien'] == 1: #  P1
            session['gejalaPasien'] = 2
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 19 and session['logs2'] == 0: #  P7
            session['gejalaPasien'] = 9
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 9 and session['logs'] == 1: #  P2
            session['gejalaPasien'] = 10
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 20: #  P6
            terjangkitVirus = daftarVirus[7] 
            return render_template("result.html", name = name, terjangkitVirus = terjangkitVirus, awal = url_for('index'))
         elif session['gejalaPasien'] == 25: #  P6
            terjangkitVirus = daftarVirus[3] 
            return render_template("result.html", name = name, terjangkitVirus = terjangkitVirus, awal = url_for('index'))
         elif session['gejalaPasien'] == 12  and session['logs'] == 1:  #P9
            session['gejalaPasien'] = 21
            session['logs'] = 2
            return redirect(url_for('diagnosa'))            
      #=============================================================Logs 2
      elif session['logs'] == 2 and checkGejala():
         if session['gejalaPasien'] == 2: # P1
            session['gejalaPasien'] = 3
            session['logs'] = 3
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 9 :#  P7
            session['gejalaPasien'] = 20
            session['logs'] = 3
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 10: #  P2
            session['gejalaPasien'] = 24
            session['logs'] = 3
            return redirect(url_for('diagnosa'))   
         elif session['gejalaPasien'] == 12: #  P6
            session['gejalaPasien'] = 16
            session['logs'] = 3
            return redirect(url_for('diagnosa')) 
         elif session['gejalaPasien'] == 21: #  P9
            session['gejalaPasien'] = 22
            session['logs'] = 3
            return redirect(url_for('diagnosa'))              
       #=============================================================Logs 3
      elif session['logs'] == 3 and checkGejala():
         if session['gejalaPasien'] == 3: # P1
            session['gejalaPasien'] = 4
            session['logs'] = 4
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 20 :# P7
            terjangkitVirus = daftarVirus[6] 
            return render_template("result.html", name = name, terjangkitVirus = terjangkitVirus, awal = url_for('index'))
         elif session['gejalaPasien'] == 12: #  P4
            session['gejalaPasien'] = 13
            session['logs'] = 4
            return redirect(url_for('diagnosa'))  
         elif session['gejalaPasien'] == 24: #  P2
            session['gejalaPasien'] = 25
            session['logs'] = 4
            return redirect(url_for('diagnosa')) 
         elif session['gejalaPasien'] == 16: #  P6
            session['gejalaPasien'] = 18
            session['logs'] = 4
            return redirect(url_for('diagnosa'))    
         elif session['gejalaPasien'] == 22: #  P9
            session['gejalaPasien'] = 23
            session['logs'] = 4
            return redirect(url_for('diagnosa'))                                           
      #=============================================================Logs 4
      elif session['logs'] == 4 and checkGejala():
         if session['gejalaPasien'] == 4: # P1
            session['gejalaPasien'] = 5
            session['logs'] = 5
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 25: #  P2
            session['gejalaPasien'] = 26
            session['logs'] = 5
            return redirect(url_for('diagnosa')) 
         elif session['gejalaPasien'] == 13: #  P4
            session['gejalaPasien'] = 14
            session['logs'] = 5
            return redirect(url_for('diagnosa'))   
         elif session['gejalaPasien'] == 18: #  P6
            session['gejalaPasien'] = 24
            session['logs'] = 5
            return redirect(url_for('diagnosa'))  
         elif session['gejalaPasien'] == 23: #  P9
            session['gejalaPasien'] = 24
            session['logs'] = 5
            return redirect(url_for('diagnosa'))                                             
      #=============================================================Logs 5
      elif session['logs'] == 5 and checkGejala():
         if session['gejalaPasien'] == 5: # P1
            session['gejalaPasien'] = 6
            session['logs'] = 6
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 26: #  P2
            terjangkitVirus = daftarVirus[1] 
            return render_template("result.html", name = name, terjangkitVirus = terjangkitVirus, awal = url_for('index'))
         elif session['gejalaPasien'] == 14: #  P4
            session['gejalaPasien'] = 15
            session['logs'] = 6
            return redirect(url_for('diagnosa'))  
         elif session['gejalaPasien'] == 24: #  P6
            session['gejalaPasien'] = 25
            session['logs'] = 6
            return redirect(url_for('diagnosa'))                                                                                             
      #=============================================================Logs 6
      elif session['logs'] == 6 and checkGejala():
         if session['gejalaPasien'] == 6: # P1
            session['gejalaPasien'] = 7
            session['logs'] = 7
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 15: # P4
            session['gejalaPasien'] = 16
            session['logs'] = 7
            return redirect(url_for('diagnosa'))   
         elif session['gejalaPasien'] == 25: #  P6
            session['gejalaPasien'] = 27
            session['logs'] = 7
            return redirect(url_for('diagnosa')) 
         elif session['gejalaPasien'] == 28: #  P9
            terjangkitVirus = daftarVirus[8]
            return render_template("result.html", name = name, terjangkitVirus = terjangkitVirus, awal = url_for('index'))             
      #=============================================================Logs 7
      elif session['logs'] == 7 and checkGejala():
         if session['gejalaPasien'] == 7: # P1
            session['gejalaPasien'] = 8
            session['logs'] = 8
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 16: # P4
            session['gejalaPasien'] = 24
            session['logs'] = 8
            return redirect(url_for('diagnosa'))  
         elif session['gejalaPasien'] == 27: #  P6
            terjangkitVirus = daftarVirus[5]
            return render_template("result.html", name = name, terjangkitVirus = terjangkitVirus, awal = url_for('index'))                            
         elif session['gejalaPasien'] == 5: # P3
            session['gejalaPasien'] = 11
            session['logs'] = 8
            return redirect(url_for('diagnosa'))            
      #=============================================================Logs 8
      elif session['logs'] == 8 and checkGejala():
         if session['gejalaPasien'] == 8: # P1
            terjangkitVirus = daftarVirus[0]
            return render_template("result.html", name = name, terjangkitVirus = terjangkitVirus, awal = url_for('index'))
         elif session['gejalaPasien'] == 24: # P4
            session['gejalaPasien'] = 25
            session['logs'] = 9
            return redirect(url_for('diagnosa')) 
         elif session['gejalaPasien'] == 11: # P3
            session['gejalaPasien'] = 21
            session['logs'] = 9
            return redirect(url_for('diagnosa'))                         
      #=============================================================Logs 9      
      elif session['logs'] == 9 and checkGejala():
         if session['gejalaPasien'] == 25: # P4
            session['gejalaPasien'] = 26
            session['logs'] = 10
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 21: # P3                    
            terjangkitVirus = daftarVirus[2]
            return render_template("result.html", name = name, terjangkitVirus = terjangkitVirus, awal = url_for('index'))
      # #=============================================================Logs 10  
      elif session['logs'] == 10 and checkGejala():
         if session['gejalaPasien'] == 26: # P4
            session['gejalaPasien'] = 27
            session['logs'] = 11
            return redirect(url_for('diagnosa'))                
      #=============================================================Logs 11
      elif session['logs'] == 11 and checkGejala():
         if session['gejalaPasien'] == 27: # P4
            terjangkitVirus = daftarVirus[3]
            return render_template("result.html", name = name, terjangkitVirus = terjangkitVirus, awal = url_for('index'))
      #=============================================================Logs
      else:
         if session['gejalaPasien'] == 0: #  P7
            session['gejalaPasien'] = 19
            session['logs'] = 1
            session['logs2'] = 0
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 1: #  P2
            session['gejalaPasien'] = 9
            session['logs'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 24: #  P4
            session['gejalaPasien'] = 12
            session['logs'] = 3                
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 10: # P6
            session['gejalaPasien'] = 12
            session['logs'] = 2
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 12: # P5
            session['gejalaPasien'] = 20
            session['logs'] = 1
            return redirect(url_for('diagnosa'))  
         elif session['gejalaPasien'] == 20: # P8
            session['gejalaPasien'] = 25
            session['logs'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 9: # P9
            session['gejalaPasien'] = 12
            session['logs'] = 1
            return redirect(url_for('diagnosa'))
         elif session['gejalaPasien'] == 25: # P9
            session['gejalaPasien'] = 28
            session['logs'] = 6
            return redirect(url_for('diagnosa')) 
         elif session['gejalaPasien'] == 28: # P3
            session['gejalaPasien'] = 5
            session['logs'] = 7
            return redirect(url_for('diagnosa'))            

         

@app.route('/diagnosa',methods = ['POST', 'GET'])
def diagnosa():
   name = session['namaPasien']
   pertanyaan = daftarGejala[session['gejalaPasien']]
   return render_template("diagnosa.html", pertanyaan = pertanyaan, name = name, link = url_for('index'))

@app.route('/home')
def home():
   return render_template("home.html")


if __name__ == '__main__':
   app.run(debug = True)