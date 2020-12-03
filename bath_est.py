print('Thank you for chosing the Association of Advanced Construction\n')

print('This estimate will approximate the costs of a complete bathroom renewal\n')

print('Please understand, the more information you give us the more precise the estimate')

print('------------------------------------------------')
print('------------------------------------------------')

Cust_name = input('\nPlease enter your name:(first and last) ')
Date_user = input('\nPlease enter the date:(Mar. 07, 2017) ')

Cust_name,"""The Association of Advanced Construction and Computer Programming experts
have united to create a well developed estimate. We believe the customer should
have access to estimates without setting appointments and having the
convenience of acessing a complete bathroom renewal cost estimate. Please answer all questions honestly
and accordingly."""



import math

Window_M = input('\nDoes your bathroom have any windows? ')
if Window_M == 'yes':
    Window_H = int(input('\nPlease enter height in inches: '))
    Window_L = int(input('Please enter length in inches: '))
if Window_M == 'Yes':
    Window_H = int(input('\nPlease enter height in inches: '))
    Window_L = int(input('Please enter length in inches: '))
if Window_M == 'No':
    Window_H = 0
    Window_L = 0
elif Window_M == 'no':
    Window_H = 0
    Window_L = 0

print('\nPlease enter the dimensions of the bathroom.')
Measurement1 = float(input('\nEnter length in inches: '))
Measurement2 = float(input('Enter width in inches: '))
Measurement3 = float(input('Enter height in inches: '))
# Implemintation of list or data structure 
my_list1 = [Measurement1, Measurement2, Measurement3]

# The calculations are asked to be put into inches for simplicity
# Bu the numbers are all made in feet thus the division of 12

B_H = Measurement3/12
B_L = Measurement1/12
B_W = Measurement2/12


#======================================================== Everything Above
#================================== Are inputs for the estimate to be conducted 

#Implemintation of a Function and a class as spoken to you for extra credit


class TypeOfBath:
    def __init__(self):
        self.item_height = 0;
        self.item_width = 0;
        self.item_length = 0;
#Option given between a shower and a bath
#Neither was for a half bathroom
#The program runs and everything works fine but I would like to continue
#Developing this program
#An option will become for half bathrooms
def bath(item_height,item_width,item_length):
    bath_type = input('\nWould you like a shower or a bath? ')
    if bath_type == 'neither':
        item_height = 0;
        item_width = 0;
        item_length = 0;
            
    if bath_type == 'bath' or 'Bath':
        item_width = 32;
        item_height = 20;
        item_length = 60;
            
    if bath_type == 'shower' or 'Shower':
        item_length = 60;
        item_height = 0;
        item_width = 32;
        
    return item_height, item_width, item_length,
# Here I took the variables out of the class according to the input
#So that I could use them for the calculations
#Because each calculation is according to the choice made by the person
bath1 = TypeOfBath()
x = bath1.item_height
y = bath1.item_width
z = bath1.item_length
x,y,z = bath(x,y,z)
bath.item_height = x
bath.item_width = y
bath.item_length = z

#Because the measurements are in inches there is a transition
conv_z = bath.item_length/12
conv_y = bath.item_width/12
conv_x = bath.item_height/12

 
#Applications of while loop and branching
#The program asks for certain questions needed
while bath.item_height == 20: # Bath
    print('\nThe ceiling of the bath is usually tiled.')
    print('However, some customers prefer to tile all the walls except the cieling.')
    ceiling = input('\nDo you want the ceiling inside the bath to be tiled? ')
    if ceiling == 'yes' or 'Yes':
        tile_height = (B_H)-(conv_x)
        inside_tile = math.ceil((tile_height*conv_z)+(tile_height*conv_y*2)+(conv_z*conv_y))
        floor_tile_half = 0
        floor_tile_bath = math.ceil((B_L*B_W)-(conv_y*conv_z))
        wall_tile_half = 0
    while ceiling != 'yes' or 'Yes':
        tile_height = (B_H)-(conv_x)
        inside_tile = math.ceil((tile_height*conv_z)+(tile_height*conv_y*2))
        floor_tile_half = 0
        floor_tile_bath = math.ceil((B_L*B_W)-(conv_y*conv_z))
        wall_tile_half = 0
        break
    break

while bath.item_height == 0 and bath.item_length == 60: # Shower
    print('\nThe ceiling of a shower is usually tiled.')
    print('However, some customers prefer to tile all the walls except the cieling.')
    ceiling = input('\nDo you want the cieling inside the shower to be tiled? ')
    if ceiling == 'yes' or 'Yes':
        tile_height = (B_H)-(conv_x)
        inside_tile = math.ceil((tile_height*conv_z)+(tile_height*conv_y*2)+(conv_z*conv_y))
        floor_tile_half = 0
        floor_tile_bath = math.ceil((B_L*B_W)+(conv_y*conv_z))
        wall_tile_half = 0
        
    if ceiling != 'yes' or 'Yes':
        tile_height = (B_H)-(conv_x)
        inside_tile = math.ceil((tile_height*conv_z)+(tile_height*conv_y*2))
        floor_tile_half = 0
        floor_tile_bath = math.ceil((B_L*B_W)+(conv_y*conv_z))
        wall_tile_half = 0
    print('\nUsually, the tile of the shower floor is made up of the same tile used in the bathroom floor')
    decision3 = input('\nWill you be using a different tile inside the shower floor? ')
    if decision3 == 'yes' or 'Yes':
        floor_tile_bath = math.ceil(B_L*B_W)
        wall_tile_half = 0
    if decision3 != 'yes' or 'Yes':
        floor_tile_bath = math.ceil((B_L*B_W)-(conv_y*conv_z))
        wall_tile_half = 0 
        break
    break
print('\nMaterials needed:\n')

P_F_Tile = 15
Price_Floor_Tile = ((floor_tile_bath+floor_tile_half)*P_F_Tile)


P_inside = 12
Price_Inside_Tile = (P_inside*inside_tile)

P_Wall_Tile = 10
Price_wall_tile = (P_Wall_Tile*wall_tile_half)




F_Gal_PR = 400
F_Sheet = 32
F_Wonder = 15
F_CP = 400
F_Gal_P = 400
F_Container=10000

def molding_FL_Sum(B_L, B_W):
    m_FL_Sum = (B_W*2)+(B_L)
    return m_FL_Sum
TM_FL_M = math.floor(molding_FL_Sum(B_L, B_W))

Door_H = 80
Door_W = 34

def molding_TR_Sum(Window_H, Window_L, Door_H, Door_W):
    m_TR_Sum = (Window_H*2)+(Window_L*2)+(Door_H*2)+(Door_W)
    return m_TR_Sum/12
TM_TR_M = math.ceil(molding_TR_Sum(Window_H, Window_L, Door_H, Door_W))


Sheet_Sum = ((B_L*2)+(B_W*2))*B_H
A_Sheet = math.ceil(Sheet_Sum/F_Sheet)
TM_Sheet = math.ceil(Sheet_Sum/F_Sheet)
Wonder_Sum = (B_L*B_W)+(B_L*B_H)
A_Wonder = (Wonder_Sum/F_Wonder)
TM_Wonder = math.ceil(Wonder_Sum/F_Wonder)
Dump_Sum = ((B_L*B_H*2)+(B_W*B_L*2)+(B_H*B_W*2))
A_Dump = math.ceil(Dump_Sum/F_Container)
TM_Dump = math.ceil(Dump_Sum/F_Container)
PR_Sum = (B_H*B_L)+(B_H*B_W*2)+(B_W*B_L)
A_PR = math.ceil(PR_Sum/F_Gal_PR) # Needs to be rounded up
TM_PR = math.ceil(PR_Sum/F_Gal_PR) # Needs to be rounded up 
CP_Sum = (B_L*B_W)*2
A_CP = math.ceil(CP_Sum/F_CP) # Needs to be rounded up 
TM_CP = math.ceil(CP_Sum/F_CP) # Needs to be rounded up
P_Sum = (B_L*B_H)+((B_W*B_H)*2)
A_P = math.ceil(P_Sum/F_Gal_P) # Needs to be rounded up
TM_P = math.ceil(P_Sum/F_Gal_P)# Needs to be rounded up
print(TM_Dump, 'Container for demolition disposal')
print((TM_Sheet),'Pieces of Sheet Rock (4ftx8ft)')
print((TM_Wonder),'Pieces of Wonderboard (3ftx5ft)')
print((TM_PR), 'Gallon(s) of Killz water-based Primer')
print((TM_CP), 'Gallon(s) of Behr Flat Ceiling Paint')
print((TM_P), 'Gallon(s) of Behr Marquee Paint')
print(TM_FL_M, 'Feet of Baseboard')
print(TM_TR_M, 'Feet of Trim Molding')
print(floor_tile_bath+floor_tile_half, 'Squared Feet of Floor Tile')
print(inside_tile, 'Squared Feet of Inside Tile')
print('------------------------------------------------')
#Prices begin <=================================== Material Prices per one
P_Molding = 13

#Function
def molding_FL_MAT(P_Molding):
    molding_needed = TM_FL_M/8
    TC_FL_M_Calc = molding_needed*P_Molding
    return TC_FL_M_Calc
TC_FL_M = molding_FL_MAT(P_Molding)

P_Trim = 7 

def molding_TR_MAT(P_Trim):
    molding_needed = TM_TR_M/7
    TC_TR_M_Calc = molding_needed*P_Trim
    return TC_TR_M_Calc
TC_TR_M = molding_TR_MAT(P_Trim)

P_D = 500
print('Container for Demolition Disposal Cost: $', P_D*A_Dump)
P_Sheet = 11
print('Sheet Rock Total Cost: $', P_Sheet*A_Sheet)
P_Wonder = 12
print('Wonder Board Total Cost: $', math.ceil(P_Wonder*A_Wonder))
P_PR = 10
print('Killz Primer Total Cost: $', P_PR*A_PR)
P_CP = 45
print('Behr Flat Ceiling Paint Total Cost: $', P_CP*A_CP)
P_P = 50
print('Behr Marquee Paint Total Cost: $', P_P*A_P)
print('Baseboard Moldings Cost: $', TC_FL_M)
print('Window and Door Moldings Cost: $', TC_TR_M)
TC_P = (P_P*TM_P)
TC_CP = (P_CP*TM_CP)
TC_Wonder = (P_Wonder*TM_Wonder)
TC_Sheet = (P_Sheet*TM_Sheet)
TC_PR = (P_PR*TM_PR)
TC_D = (P_D*A_Dump)
M_Total_Cost = math.ceil(TC_Wonder + TC_Sheet + TC_PR + TC_CP + TC_P + TC_D + TC_FL_M + TC_TR_M)
print('------------------------------------------------')
print('Total Cost of Materials: $', M_Total_Cost)
print('Plus Toilet, Sink, Tub(if bath) and Mirror of choice')
print('------------------------------------------------')

#Labor must be considered into the total price
#LABOR_C = Labor cost
Labor_S = 35
Labor_S2 = 35
Labor_W = 35
Labor_PR = 1
Labor_CP = 2
Labor_P = 2
Labor_M = 4
Labor_C_M = Labor_M*(TM_TR_M+TM_FL_M)
Labor_C_P = Labor_P*P_Sum
Labor_CCP = Labor_CP*CP_Sum
Labor_CPR = Labor_PR*PR_Sum
Labor_CS = Labor_S*TM_Sheet
Labor_CS2 = Labor_S2*TM_Sheet
Labor_CW = Labor_W*TM_Wonder
Labor_CD = 900
Installations = 700
print('Labor of Demolition: $', Labor_CD)
print('Labor of Sheet Rock: $', Labor_CS)
print('Labor of Taping, Compound and Sanding: $', Labor_S2*TM_Sheet)
print('Labor of Wonder Board: $', Labor_CS)
print('Labor of Priming: $', Labor_CPR)
print('Labor of Ceiling Paint: $', Labor_CCP)
print('Labor of Paint: $', Labor_C_P)
print('Labor of Molding: $', Labor_C_M)
print('Labor of Floor Tile: $', Price_Floor_Tile)
print('Labor of Inside Tile Bath/Shower: $', Price_Inside_Tile)
print('Labor of Wall Tile: $', Price_wall_tile)
print('Installation of Toilet, Sink, Mirror and lights: $', Installations)
L_Total_Cost = math.ceil(Labor_CW+Labor_CS+Labor_CS2+Labor_CPR+Labor_CCP+Labor_C_P+Labor_CD+Labor_C_M+Price_Inside_Tile+Price_Floor_Tile+Price_wall_tile)
print('------------------------------------------------')
print('Total Cost of Labor: $',L_Total_Cost)
print('------------------------------------------------')
#Total Cost
print('')
print('Total Expenses: $', math.ceil(M_Total_Cost + L_Total_Cost))

print('\nOn',Date_user,Cust_name,'recieved an estimate of $',math.ceil(M_Total_Cost + L_Total_Cost))

print('\nFinal Programming Project By Manuel Navas on May 15, 2017\n')
pause = input('\nPress the Enter Key to continue')



