#imports

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np




#read in data
df1=pd.read_excel("PerformanceData_Unitxx_ZayedMostafa.xlsx",sheet_name="Steady_State",skiprows=[],header=0)
df2=pd.read_excel("PerformanceData_Unitxx_ZayedMostafa.xlsx",sheet_name="Uncertainties",skiprows=[],header=0)
#plot data
x="Ambient Temperature (⁰F)"
y="Coefficient of Performance (W/W)"
dx= "Ambient Temperature (⁰F)"
dy="Coefficient of Performance (W/W)"
fig, ax = plt.subplots(layout='constrained')
ax.errorbar(df1[x],df1[y],xerr=df2[dx], yerr=df2[dy], fmt='o', color='Red',
             ecolor='black', elinewidth=1, capsize=5,label="COP")
plt.grid()
ax.set_xlabel(r'$Ambient\ Temperature\ [^oF]$')
ax.set_ylabel(r'$Coefficient\ of\ Performance\ [W/W]$')
# get handles
handles, labels = ax.get_legend_handles_labels()
# remove the errorbars
handles = [h[0] for h in handles]
# use them in the legend
ax.legend(handles, labels, loc='best',numpoints=1)

#Secondary y axis
def COP2EER(y):
    """Convert COP to EER"""
    return y*3.412
def EER2COP(y):
    """Convert EER to COP"""
    return y/3.412

secax_y = ax.secondary_yaxis('right', functions=(COP2EER,EER2COP))
secax_y.set_ylabel(r'$Energy\ Efficiency\ Ratio\ [Btu/W-h]$')

#Secondary x axis
def fahrenheit_to_celsius(x):
    return (x - 32) / 1.8

def celsius_to_fahrenheit(x):
    return x * 1.8 + 32



secax_x = ax.secondary_xaxis(
    'top', functions=(fahrenheit_to_celsius, celsius_to_fahrenheit))
secax_x.set_xlabel(r'$Ambient\ Temperature\ [^oC]$')

#Tertiary x axis
def fahrenheit_to_kelvin(x):
    return (((x - 32) / 1.8) +273.15)

def kelvin_to_fahrenheit(x):
    return (x -273.15)* 1.8 + 32

# use of a float for the position:
secax_x2 = ax.secondary_xaxis(
    1.22, functions=(fahrenheit_to_kelvin, kelvin_to_fahrenheit))
secax_x2.set_xlabel(r'$Ambient\ Temperature\ [K]$')

ax.set_xlim(45,105)
ax.set_ylim(2.5,4.5)

#show/save results
plt.tight_layout()
plt.savefig("PerformanceData_Unitxx_ZayedMostafa.png", dpi=500)
plt.show()
