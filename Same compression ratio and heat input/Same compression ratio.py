# COMPARISON OF OTTO CYCLE, DIESEL CYCLE AND DUAL CYCLE EFFICIENCY UNDER CONSTANT COMPRESSION RATIO AND HEAT INPUT
print("\nCOMPARISON OF OTTO CYCLE, DIESEL CYCLE AND DUAL CYCLE EFFICIENCY UNDER CONSTANT COMPRESSION RATIO AND HEAT INPUT\n")

# For this task we will compare the PV diagram of the otto and diesel cycle.
# We will find the work done in each cycle.
# The cycle with higher work done has the highest efficiency under constant heat input.
# The cycle with the lower work done has the least efficiency and Dual cycle falls in between.


# IMPORT ALL THE REQUIRED LIBRARIES

from pylab import *
import numpy as np
from tabulate import tabulate



# DEFINE THE FUNCTION INTEGRATE
# This function helps in calculating the area under the graph using trapeziod formula

def integrate(x, y):
    area = np.trapz(y=y, x=x)
    area = abs(area)
    return area

# CONSTANT PARAMETERS

# Compression ratio
r = 5
# Adiabatic constant of working fluid in this case air
gamma = 1.4
# Input heat
# Q1 is fixed and the formula used for calculation of Q1 is
# Q1 = mCv(T3 - T2) = mCp(T3d - T2d)
# And by using PV = mRT we can calculate the difference in the volume in diesel cycle (dvd)


# INITIALLY FIXED PARAMETERS

# Minimum pressure
p_min = 10 ** 5
# Maximum pressure
p_max = 20 * 10 ** 5
# Maximum volume
v_max = 0.3


# SHOWING ALL THE FIXED AND CONSTANT PARAMETERS

#CONSTANT DATA
Constant_head = ["CONSTANT PARAMETER", "VALUE"]
Constant_data = [["Compression Ratio",r],["Adiabatic constant",gamma]]

#FIXED DATA
Fixed_data = [["Minimum pressure",p_min],["Maximum pressure",p_max],["Maximum Volume",v_max],]
Fixed_head = ["FIXED PARAMETER", "VALUE"]

#Printing the data
print("The constant parameters for this task are \n")
print(tabulate(Constant_data, headers=Constant_head, tablefmt="grid"))
print("\nThe fixed parameters for this task are \n")
print(tabulate(Fixed_data, headers=Fixed_head, tablefmt="grid"))


# REQUIRED FORMULA:

# 1.Isentropic equation :
#                         PV^gamma = constant

# 2.Compression ratio   :
#                         r = v1/v2 = v4/v3

# 3.Cutoff ratio       :
#                         Under diesel cycle
#                         rc = v3/v2


# OTTO CYCLE

# FINDING THE PARAMETERS

# PROCESS 1-2:
# FINDING PARAMETERS AT POINT 1
p1 = p_min
v1 = v_max

# isentropic equation rewritten for process 1-2
c1 = p1 * v1 ** gamma

# FINDING PARAMETERS AT POINT 2
v2 = v1 / r
p2 = c1 / (v2 ** gamma)

# PROCESS 2-3:
# FINDING PARAMETERS AT POINT 3
p3 = p_max
v3 = v2

# isentropic equation rewritten for process 3-4
c2 = p3 * v3 ** gamma

# PROCESS 3-4:
# FINDING PARAMETERS AT POINT 4
v4 = v1
p4 = c2 / v4 ** gamma


# PLOTTING OF THE OTTO CYCLE PV DIAGRAM

# PROCESS 1-2

v = linspace(v2, v1, 50)
p = c1 / v ** gamma
plot(v, p, color='black')

# Area under the curve 1-2
AO12 = integrate(v, p)


# PROCESS 2-3

v = zeros(50) + v2
p = linspace(p2, p3)
plot(v, p, label='Otto cycle', color='red')

# Area under the curve 2-3
AO23 = integrate(v, p)


# PROCESS 3-4

v = linspace(v3, v4, 50)
p = c2 / v ** gamma
plot(v, p, color='red')

# Area under the curve 3-4
AO34 = integrate(v, p)


# PROCESS 4-1

v = zeros(50) + v1
p = linspace(p1, p4)
plot(v, p, color='red')

# Area under the curve 4-1
AO41 = integrate(v, p)


# NAMING EACH POINTS IN THE GRAPH
text(v1 + 0.0006, p1, '1', fontsize=12)
text(v2 - 0.006, p2, '2', fontsize=12)
text(v3 - 0.006, p3, '3', fontsize=12)
text(v4 + 0.0006, p4 - 30000, '4', fontsize=12)


# DIESEL CYCLE

# REDETERMINING THE INITIAL PARAMETER

p_mind = p_min
v_maxd = v_max

# FINDING THE PARAMETERS

# PROCESS 1-2
# FINDING PARAMETERS AT POINT 1
p1d = p_mind
v1d = v_maxd

# isentropic equation rewritten for process 1-2
c1d = p1d * v1d ** gamma

# FINDING PARAMETERS AT POINT 2
v2d = v1d / r
p2d = c1d / v2d ** gamma


# Change in volume from constant haet supplied
#it is calculated from the input heat which is common for both the processes
dvd = ((p3-p2)*v2)/(1.4*p2d)

# process 2-3
# FINDING PARAMETERS AT POINT 3
p3d = p2d
v3d = v2d + dvd

# isentropic equation rewritten for process 3-4
c2d = p3d * v3d ** gamma

# PROCESS 3-4
# FINDING PARAMETERS AT POINT 4
v4d = v1d
p4d = c2d / v4d ** gamma

# Change in volume from constant haet supplied
dvd = ((p3-p2)*v2)/(1.4*p2d)


# PLOTTING OF THE DIESEL CYCLE PV DIAGRAM

# PROCESS 1-2

v = linspace(v2d, v1d, 50)
p = c1d / v ** gamma
plot(v, p, color='black')

# Area under the curve 1-2
AD12 = integrate(v, p)


# PROCESS 2-3

v = linspace(v2d, v3d, 50)
p = zeros(50) + p2d
plot(v, p, label='Diesel cycle', color='blue')

# Area under the curve 2-3
AD23 = integrate(v, p)


# PROCESS 3-4

v = linspace(v3d, v4d, 50)
p = c2d / v ** gamma
plot(v, p, color='blue')

# Area under the curve 3-4
AD34 = integrate(v, p)


# PROCESS 4-1

v = zeros(50) + v1d
p = linspace(p1d, p4d)
plot(v, p, label='Intersection of both cycles', color='black')

# Area under the curve 4-1
AD41 = integrate(v, p)


# NAMING EACH POINTS IN THE GRAPH
text(v1d + 0.0006, p1d, '1', fontsize=12)
text(v2d - 0.006, p2d, '2', fontsize=12)
text(v3d, p3d, '3d', fontsize=12)
text(v4d + 0.0006, p4d + 5000, '4d', fontsize=12)


# LABELING THE GRAPH
xlabel('Volume', fontsize=24)
ylabel('Pressure', fontsize=24)
legend()


# PROCESS IN THE GRAPH
print("\nThe process 1-2-3-4 represents the OTTO CYCLE.\nThe process 1-2-3d-4d represents the DIESEL CYCLE.\n")

# AREA UNDER THE CURVE FOR OTTO CYCLE
Otto_work = AO34 + AO41 - AO12 - AO23
print("Work done during the Otto Cycle = ", Otto_work)

# AREA UNDER THE CURVE FOR DIESEL CYCLE
Diesel_work = AD34 + AD41 - AD12 + AD23
print("Work done during the Diesel Cycle = ", Diesel_work)

# CONDITION UNDER CONSTANT HEAT INPUT
print("\nFor constant heat input Efficiency depends only on the work done in the cycle.\n")

#RESULT
print("\nRESULT:\n")

# CONDITION TO FIND THE HIGHER EFFICIENCY CYCLE

# Condition for Diesel cycle
if Diesel_work > Otto_work:
    print("For constant compression ratio and heat input the Diesel cycle provides highest efficiency. Thus the efficiency trends as\n     DIESEL > DUAL > OTTO")

# Condition for Otto cycle
elif Otto_work > Diesel_work:
    print("For constant compression ratio and heat input the Otto cycle provides highest efficiency. Thus the efficiency trends as\n     OTTO > DUAL > DIESEL")

# Condition for both
else:
    print("For constant compression ratio and heat input both the Diesel cycle and Otto cycle provides same efficiency. Thus the efficiency trends as\n     OTTO = DUAL = DIESEL")


# SHOWING THE PLOT
show()
