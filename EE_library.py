#!/usr/bin/env python

''' Mike's EE Library as study tool '''

#R2 = resistor with greater Ohm value
#two resistor voltage divider (Series Resistors)
def voltage_divider(Vi, R1, R2):
      Vo = Vi * (R2/ float(R1 + R2))

      return Vo

print voltage_divider(6, 2000, 6000)

#Two(2) Parllel Resistor equation (Rp)
def parallel_resistors(R1, R2):
      Rp = (R1*R2) / (R1 + R2)
      
      return Rp

print parallel_resistors(1400, 1400)

#Series Resistors (Rs)
def series_resistors(R1, R2):
      Rs = R1 + R2

      return Rs

print series_resistors(700, 2700)

#Ohms Law
def Ohms_current(V, R):
      i = V/R
      return i
def Ohms_resistance(V,i):
      R = i/V
      return R
def Ohms_Voltage(i,R):
      V = i * R
      return V

print "current through circuit is: ", Ohms_current(11, 3.4)

#Kirchoff Voltage Law : Vrise + Vdrop = 0 (entire circuit )
#Kirchoff Current Law : ∑in + ∑out = 0  (current of branches going in and out of node)

''' Circuit analysis
Node Voltage Method
1. develop reference voltage (often Ground)
2. identify Voltage 'nodes' on circuit
3. solve easy ones
4. use Kirchoff current law to create equations
5. solve

Mesh Current Method
1. identify current 'loops' in the mesh ( like a screen window)
2. solve easy ones
3. use Kirchoff Voltage law to develop equations
4. solve
'''

#Coulomb = charge (q) is amp (current) per unit measure time

''' Capacitors

   C = Coulombs aka charge (q) / Volts (V)    .. Farad = Coulombs / Volts
   C = q/V
  
   C = Farad
   capacitors in series :  1 / Cequivalent = 1/C + 2/C + 3/c ...
   Then plug in values for Cequivalent into C = q/V to find charge
   '''

def Capacitor_charge(Farad_value, Voltage):
      q = Farad_value * Voltage
      return q

def capacitor_in_series(Battery_voltage, *args):
      C_equivalent = 0
      for Farad in args:
            C_equivalent += (1/float(Farad))
      C_equivalent = 1/float(C_equivalent)

      return Capacitor_charge(C_equivalent, Battery_voltage)

print capacitor_in_series(9, 12, 4, 6)
