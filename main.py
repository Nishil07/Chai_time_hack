from flask import Flask, render_template, redirect, url_for, request
import numpy as np

A={'Wheat':50,'Bread':10,'Rice':70,'Onions':50,'Potatoes':45}
B={'Crocin':10,'Soframycin':5,'Dettol':30,'Sanitizer':20}
C={'Crocin':3,'Soframycin':6,'Dettol':4}
D={'Capsicum':40,'Potatoes':10,'Rice':10}
E={'Wheat':27,'Bread':32,'Onions':26,'Potatoes':33}
F={'Bread':20,'Wheat':20,'Rice':15}
G={'Dettol':10,'Sanitizer':5}
S={'Wheat':5,'Bread':5}
T={'Soframycin':10,'Dettol':5}
U={'Rice':100,'Onions':50,'Potatoes':35}
W={'Crocin':10,'Soframycin':5,'Dettol':3,'Sanitizer':2}
stores={'Vasant Nagar':['A','B','C','D'],'Churchgate':['E','F','G'],'Gowalia Tank':['S','T','U','W']}
L=[A,B,C,D,E,F,G,S,T,U,W]
LL=['A','B','C','D','E','F','G','S','T','U','W']
slots=np.zeros((10,6),int)


def slot_booking():
    f=0
    print('select your nearest area by pressing\nVasant Nagar\nChurchgate\nGowalia Tank')
    y=input()
    if y in stores:
        print('Choose your preferable shop')
        for i in range(len(stores[y])):
            print(stores[y][i])
        z=input()
        while(f==0):
            print('The slots are as follows:\nPress the respective numbers\n0:9:30-10:00\n1:10:00-10:30\n2:10:30-11:00\n3:11:00-11:30\n4:11:30-12:00\n5:12:00-12:30')
            d=int(input())
            if(slots[LL.index(z),d]<2):
                slots[LL.index(z),d]+=1
                f=1
            else:
                print('please select another slot this one is already full')


def disp(option):
    if(option == "Availability of Stock"):
        return redirect('/arealist')
    if(option == "Shopkeeper"):
        return redirect('/shopkeeper')
    if(option == "Slot booking"):
        return redirect('/slotarea')



app = Flask(__name__)


@app.route('/arealist', methods=['POST','GET'])
def arealist():
    if request.method == 'POST':
        selected_option = request.form['menu']
        return render_template('storelist.html', data = stores[selected_option])
    else:
        return render_template('area.html', data = stores)

@app.route('/storelist', methods=['POST','GET'])
def storelist():
    if request.method == 'POST':
        selected_option = request.form['menu']
        return render_template('stock.html', data = L[LL.index(selected_option)])
    else:
        return render_template('area.html', data = stores)


#===================================================================================================================
#
#===================================================================================================================


@app.route('/shopkeeper', methods=['POST','GET'])
def shop():
    if request.method == 'POST':
        pin = int(request.form['pin'])
        return render_template('shop.html', data = L[pin-123], user=(pin-123))
    else:
        return render_template('shopkeeper.html')

@app.route('/add/<path>', methods=['POST','GET'])
def add(path):
    if request.method == 'POST':
        item = request.form['item']
        quantity = request.form['quantity']
        L[int(path)][item] = quantity
        return render_template('shop.html', data = L[int(path)], user = path)
    else:
        return render_template('add.html', data = L[int(path)], user = path)

@app.route('/update/<path>', methods=['POST','GET'])
def update(path):
    if request.method == 'POST':
        item = request.form['item']
        quantity = request.form['quantity']
        L[int(path)][item] = quantity
        return render_template('shop.html', data = L[int(path)], user = path)
    else:   
        return render_template('update.html', data = L[int(path)], user = path)

#===================================================================================================================
#
#===================================================================================================================

@app.route('/slotarea', methods=['POST','GET'])
def slotarea():
    if request.method == 'POST':
        selected_option = request.form['menu']
        return render_template('slotstore.html', data = stores[selected_option])
    else:
        return render_template('slotarea.html', data = stores)

@app.route('/slotstore', methods=['POST','GET'])
def slotstore():
    if request.method == 'POST':
        selected_option = request.form['menu']
        return render_template('slot.html', data = L[LL.index(selected_option)], store = selected_option, message = '')
    else:
        return render_template('area.html', data = stores)

@app.route('/slot/<path>', methods=['POST','GET'])
def slot(path):
    if request.method == 'POST':
        selected_option = request.form['menu']
        if(slots[LL.index(path),int(selected_option)]<2):
            slots[LL.index(path),int(selected_option)]+=1
            message = 'Booked Successfully'
        else:
            message = 'Please select Another Slot this one is already full!!!'
        return render_template('slot.html', data = L[LL.index(path)], store = path, message = message)
    else:
        return render_template('area.html', data = stores)



#===================================================================================================================
#
#===================================================================================================================

@app.route('/app', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        selected_option = request.form['menu']
        return disp(selected_option)
    else:
        return render_template('index.html')


@app.route('/hello')
def hello(): 
    return "hey"
    
if __name__ == "__main__":
    app.run()