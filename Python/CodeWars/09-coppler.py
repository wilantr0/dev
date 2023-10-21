f = float(input())
c = float(input())
vr = float(input())
vs = float(input())

ckm = (c*3600)/1000

fp = f*((ckm+vr)/(ckm+(vs)))

fp2 = ("%.02f" % fp)

print(str(fp2)+' Hz')
