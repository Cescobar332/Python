import pandas as pd
import numpy as np
import random

lista = np.random.choice(np.arange(1, 5), p = [0.3, 0.2, 0.2, 0.3], size = 1000)
nino = []
joven = []
adulto = []
abuelo = []

edad2= []

for i in lista:
  if i == 1:
    nino.append(random.randint(0, 9))
    a = np.random.normal(loc= 4.5, scale= 1.0)
    edad2.append(a)
  elif i == 2:
    joven.append(random.randint(10, 25))
    a = np.random.normal(loc= 17.5, scale= 1.0)
    edad2.append(a)
  elif i == 3:
    adulto.append(random.randint(26, 55))
    a = np.random.normal(loc= 40.5, scale= 1.0)
    edad2.append(a)
  elif i == 4:
    abuelo.append(random.randint(56, 120))
    a = np.random.normal(loc= 88, scale= 1.0)
    edad2.append(a)
edad = nino + joven + adulto + abuelo



df = pd.DataFrame({'Edad': edad,
                   'Edad2': edad2,
                   'Edad3': pd.qcut(df.Edad, 4, labels=["Child", "Young", "Adult", "Old"])})
df