import pandas as pd
import numpy as np
import tkinter as tk
import tkintermapview as tkmv


rep_table = pd.read_excel("Representantes.xlsx")
states = {
    'AC': [],
    'AL': [],
    'AP': [],
    'AM': [],
    'BA': [],
    'CE': [],
    'ES': [],
    'GO': [],
    'MA': [],
    'MT': [],
    'MS': [],
    'MG': [],
    'PA': [],
    'PB': [],
    'PR': [],
    'PE': [],
    'PI': [],
    'RJ': [],
    'RN': [],
    'RS': [],
    'RO': [],
    'RR': [],
    'SC': [],
    'SP': [],
    'SE': [],
    'TO': [],
    'DF': [],
    'EX': []
}

print(states)

for i in range(len(rep_table)):
    ele = rep_table.iloc[i].tolist()
    states[ele[3]].append(ele)
    
print(states["SP"])

window = tk.Tk()
window.geometry("900x730")


def btnAC():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[0]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnAL():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[1]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnAP():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[2]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    
        
    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnAM():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[3]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnBA():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[4]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnCE():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[5]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnES():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[6]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnGO():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[7]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnMA():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[8]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnMT():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[9]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnMS():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[10]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnMG():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[11]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnPA():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[12]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnPB():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[13]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnPR():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[14]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnPE():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[15]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass 
        
    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
       
def btnPI():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[16]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnRJ():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[17]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    
        
    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnRN():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[18]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass  
         
    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
     
def btnRS():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[19]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    
        
    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnRO():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[20]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass  
      
    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
        
def btnRR():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[21]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass  
      
    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
        
def btnSC():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[22]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass   
   
    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
          
def btnSP():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[23]]:
        print(a[4])
        try:
            print( str(a[6]))
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]), command=lambda p: tk.messagebox.showinfo("Info", str(a[6])))
        except:
            pass    
  
    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
          
def btnSE():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[24]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
                
def btnTO():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[25]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    

    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
def btnDF():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[26]]:
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    
    
    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
        
def btnEX():
    try:
        map_widget.desatroy()
    except:
        pass
    
    map_widget = tkmv.TkinterMapView(window, height=730, width=820, corner_radius=0)
    for a in states[list(states.keys())[27]]:
        print(a)
        print(a[4])
        try:
            maker = map_widget.set_address(address_string = str(a[4]) + ", Brazil", marker = True, text = str(a[2]))
        except:
            pass    
            
    map_widget.set_position(-10,-55)
    map_widget.set_zoom(4)

    map_widget.grid(column="1", row="0", rowspan="30")
    
    
btn = tk.Button(window, text="AC", command=btnAC, height=1, width=20)
btn.grid(column="0", row=1)

btn = tk.Button(window, text="AL", command=btnAL, height=1, width=20)
btn.grid(column="0", row=2)

btn = tk.Button(window, text="AP", command=btnAP, height=1, width=20)
btn.grid(column="0", row=3)

btn = tk.Button(window, text="AM", command=btnAM, height=1, width=20)
btn.grid(column="0", row=4)

btn = tk.Button(window, text="BA", command=btnBA, height=1, width=20)
btn.grid(column="0", row=5)

btn = tk.Button(window, text="CE", command=btnCE, height=1, width=20)
btn.grid(column="0", row=6)

btn = tk.Button(window, text="ES", command=btnES, height=1, width=20)
btn.grid(column="0", row=7)

btn = tk.Button(window, text="GO", command=btnGO, height=1, width=20)
btn.grid(column="0", row=8)

btn = tk.Button(window, text="MA", command=btnMA, height=1, width=20)
btn.grid(column="0", row=9)

btn = tk.Button(window, text="MT", command=btnMT, height=1, width=20)
btn.grid(column="0", row=10)

btn = tk.Button(window, text="MS", command=btnMS, height=1, width=20)
btn.grid(column="0", row=11)

btn = tk.Button(window, text="MG", command=btnMG, height=1, width=20)
btn.grid(column="0", row=12)

btn = tk.Button(window, text="PA", command=btnPA, height=1, width=20)
btn.grid(column="0", row=13)

btn = tk.Button(window, text="PB", command=btnPB, height=1, width=20)
btn.grid(column="0", row=14)

btn = tk.Button(window, text="PR", command=btnPR, height=1, width=20)
btn.grid(column="0", row=15)

btn = tk.Button(window, text="PE", command=btnPE, height=1, width=20)
btn.grid(column="0", row=16)

btn = tk.Button(window, text="PI", command=btnPI, height=1, width=20)
btn.grid(column="0", row=17)

btn = tk.Button(window, text="RJ", command=btnRJ, height=1, width=20)
btn.grid(column="0", row=18)

btn = tk.Button(window, text="RN", command=btnRN, height=1, width=20)
btn.grid(column="0", row=19)

btn = tk.Button(window, text="RS", command=btnRS, height=1, width=20)
btn.grid(column="0", row=20)

btn = tk.Button(window, text="RO", command=btnRO, height=1, width=20)
btn.grid(column="0", row=21)

btn = tk.Button(window, text="RR", command=btnRR, height=1, width=20)
btn.grid(column="0", row=22)

btn = tk.Button(window, text="SC", command=btnSC, height=1, width=20)
btn.grid(column="0", row=23)

btn = tk.Button(window, text="SP", command=btnSP, height=1, width=20)
btn.grid(column="0", row=24)

btn = tk.Button(window, text="SE", command=btnSE, height=1, width=20)
btn.grid(column="0", row=25)

btn = tk.Button(window, text="TO", command=btnTO, height=1, width=20)
btn.grid(column="0", row=26)

btn = tk.Button(window, text="DF", command=btnDF, height=1, width=20)
btn.grid(column="0", row=27)

btn = tk.Button(window, text="EX", command=btnEX, height=1, width=20)
btn.grid(column="0", row=28)





window.mainloop()