import pygal
import webbrowser
import pandas as pd
from pygal.style import LightColorizedStyle as LCS,RotateStyle as RS

df = pd.read_csv('new-cases-of-hiv-infection.csv')


def getsvg(year): 
    country = {}  
    cont = 0
    print('go')
    while True:    
        try:
            if df["Year"][cont] == year and type(df["Code"][cont]) == type('str'):
                #print('1')
                name = df["Code"][cont]
                name = name[:2].lower()            
                country[name] = df["Incidence - HIV/AIDS - Sex: Both - Age: All Ages (Number) (new cases of HIV)"][cont]               
            else:
                pass
            cont += 1
        except:
            break
    return country
        
#print(country)
#wm.add("North America", country)
#wm.render_to_file('sss.svg')
#a=webbrowser.get('windows-default')
#webbrowser.open('sss.svg')

for year in range(1990,2018,1):
    wm = pygal.maps.world.World()
    wm.title = "HIV"
    country = getsvg(year)
    wm.add("HIV", country)
    wm.render_to_file(str(year)+'.svg')
a=webbrowser.get('windows-default')
webbrowser.open('basic2.html')
    
    
