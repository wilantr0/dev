gender = input().upper()
CV = float(input())
CB = int(input())
PL = int(input())
HG = float(input())
PS = int(input())

CVx = ''
CBx = ''
PLx = ''
HGx = ''
PSx = ''

if gender == 'MALE':
    if CV > 4.3 and CV < 5.9:
        CVx = 'NORMAL'
    else:
        CVx = 'VISIT THE DOCTOR'
    if CB > 4500 and CB < 11000:
        CBx = 'NORMAL'
    else:
        CBx = 'VISIT THE DOCTOR'
    if PL > 150000 and PL < 400000:
        PLx = 'NORMAL'
    else:
        PLx = 'VISIT THE DOCTOR'
    if HG > 13.5 and HG < 17.5:
        HGx = 'NORMAL'
    else:
        HGx = 'VISIT THE DOCTOR'
    if PS > 41 and PS < 53:
        PSx = 'NORMAL'
    else:
        PSx = 'VISIT THE DOCTOR'
if gender == 'FEMALE':
    if CV > 3.5 and CV < 5.5:
        CVx = 'NORMAL'
    else:
        CVx = 'VISIT THE DOCTOR'
    if CB > 4500 and CB < 11000:
        CBx = 'NORMAL'
    else:
        CBx = 'VISIT THE DOCTOR'
    if PL > 150000 and PL < 400000:
        PLx = 'NORMAL'
    else:
        PLx = 'VISIT THE DOCTOR'
    if HG > 12.0 and HG < 16.0:
        HGx = 'NORMAL'
    else:
        HGx = 'VISIT THE DOCTOR'
    if PS > 36 and PS < 46:
        PSx = 'NORMAL'
    else:
        PSx = 'VISIT THE DOCTOR'

print('Red blood cells: ' + CVx)
print('White blood cells: ' + CBx)
print('Platelets: ' + PLx)
print('Hemoglobin: ' + HGx)
print('Hematocrit: ' + PSx)
