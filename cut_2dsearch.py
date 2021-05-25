import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
import mplhep as hep

#######################
x_tt = 40.288       ##
x_ttV = 0.07893     ##
x_dy = 1108         ##
x_ww = 5.707        ##
x_wz = 2.307        ##
x_zz = 0.4376       ##
x_st = 2.54         ##
x_dm1t = 0.003629  ##
x_dm2t = 0.0005515  ##
lumi = 3000000      ##
#######################
# 80g > 0.003629
# 0.1 > 0.003023 
# 0.2 > 0.00123
# 0.3 > 0.0006888
# 0.5 > 0.0002840
# 0.8 > 0.0001039
# 1   > 5.934e-05
# 2   > 5.501e-06
# 3   > 5.711e-07
# 5   > 9.159e-09

tt_gen_evt = 10000000
another_evt = 1000000

met_tt_0 = np.load('met_e0.npy')
met_tt_1 = np.load('met_e1.npy')
met_tt_2 = np.load('met_e2.npy')
met_tt_3 = np.load('met_e3.npy')
met_tt_4 = np.load('met_e4.npy')
met_tt_5 = np.load('met_e5.npy')
met_tt_6 = np.load('met_e6.npy')
met_tt_7 = np.load('met_e7.npy')
met_tt_8 = np.load('met_e8.npy')
met_tt_9 = np.load('met_e9.npy')

met_ttV = np.load('met_ttV.npy')
met_dy = np.load('met_dy.npy')
met_ww = np.load('met_ww.npy')
met_wz = np.load('met_wz.npy')
met_zz = np.load('met_zz.npy')
met_st = np.load('met_st.npy')
met_dm = np.load('met_80g.npy')
#dm2 = np.load('met_array/met_sp2_2t.npy')
met_tt = np.concatenate((met_tt_0,met_tt_1,met_tt_2,met_tt_3,met_tt_4,met_tt_5,met_tt_6,met_tt_7,met_tt_8,met_tt_9),axis=0)




ht_tt_0 = np.load('mt2_e0.npy')
ht_tt_1 = np.load('mt2_e1.npy')
ht_tt_2 = np.load('mt2_e2.npy')
ht_tt_3 = np.load('mt2_e3.npy')
ht_tt_4 = np.load('mt2_e4.npy')
ht_tt_5 = np.load('mt2_e5.npy')
ht_tt_6 = np.load('mt2_e6.npy')
ht_tt_7 = np.load('mt2_e7.npy')
ht_tt_8 = np.load('mt2_e8.npy')
ht_tt_9 = np.load('mt2_e9.npy')

ht_ttV = np.load('mt2_ttV.npy')
ht_dy = np.load('mt2_dy.npy')
ht_ww = np.load('mt2_ww.npy')
ht_wz = np.load('mt2_wz.npy')
ht_zz = np.load('mt2_zz.npy')
ht_st = np.load('mt2_st.npy')
ht_dm = np.load('mt2_80g.npy')
#dm2 = np.load('met_array/met_sp2_2t.npy')
ht_tt = np.concatenate((ht_tt_0,ht_tt_1,ht_tt_2,ht_tt_3,ht_tt_4,ht_tt_5,ht_tt_6,ht_tt_7,ht_tt_8,ht_tt_9),axis=0)


s1 = []
s2 = []
s3 = []

for n in range(400):
	x1 = []
	y1 = []
	z1 = []
	i = n + 200
	for m in range(100):
		j = m + 300
		mask = (met_tt > i) & (ht_tt > j)
		tt = met_tt[mask]
		mask = (met_ttV > i) & (ht_ttV > j)
		ttV = met_ttV[mask]
		mask = (met_dy > i) & (ht_dy > j)
		dy = met_dy[mask]
		mask = (met_ww > i) & (ht_ww > j)
		ww = met_ww[mask]
		mask = (met_wz > i) & (ht_wz > j)
		wz = met_wz[mask]
		mask = (met_zz > i) & (ht_zz > j)
		zz = met_zz[mask]
		mask = (met_st > i) & (ht_st > j)
		st = met_st[mask]
		mask = (met_dm > i) & (ht_dm > j)
		dm = met_dm[mask]
		wght_tt = x_tt * lumi/ tt_gen_evt
		wght_ttV = x_ttV *lumi/ another_evt
		wght_dy =  x_dy *lumi/ another_evt
		wght_ww =  x_ww *lumi/ another_evt
		wght_wz = x_wz *lumi/ another_evt
		wght_zz =  x_zz *lumi/ another_evt
		wght_st =  x_st *lumi/ another_evt
		wght_dm =  x_dm1t *lumi/ another_evt
		bkg = (len(tt)*wght_tt+len(ttV)*wght_ttV+len(dy)*wght_dy+len(ww)*wght_ww+len(wz)*wght_wz+len(zz)*wght_zz+len(st)*wght_st)
		sig = len(dm)*wght_dm
		sn = np.sqrt((2*(sig+bkg)*np.log(1+(sig/bkg)))-(2*sig))
		#sn = sig / bkg
		print(sn)
		x1.append(i)
		y1.append(j)
		z1.append(sn)


	for k in range(400):
		if z1[k] == max(z1):
			print(z1[k],"max significance")
			print(k)
			s1.append(x1[k])
			s2.append(y1[k])
			s3.append(z1[k])
			break

	print(i)


for i in range(len(s3)):
	if s3[i] == max(s3):
		print(s1[i], "max met cut")
		print(s2[i], "max mt2 cut")
		print(s3[i], "significance")
		

'''
x5 = []
y5 = []
for i in range(1000):
	mask = (tt > i)
	tt = tt[mask]
	mask = (ttV > i)
	ttV = ttV[mask]
	mask = (dy > i)
	dy = dy[mask]
	mask = (ww > i)
	ww = ww[mask]
	mask = (wz > i)
	wz = wz[mask]
	mask = (zz > i)
	zz = zz[mask]
	mask = (st > i)
	st =  st[mask]
	mask = (dm > i)
	dm = dm[mask]
	#mask = (dm2 > i)
	#dm2 = dm2[mask]
	wght_tt = x_tt * lumi/ tt_gen_evt
	wght_ttV = x_ttV *lumi/ another_evt
	wght_dy =  x_dy *lumi/ another_evt
	wght_ww =  x_ww *lumi/ another_evt
	wght_wz = x_wz *lumi/ another_evt
	wght_zz =  x_zz *lumi/ another_evt
	wght_st =  x_st *lumi/ another_evt
	#wght_dm2 =  x_dm2t *lumi/ another_evt
	#        bkg = np.sqrt(len(tt)*wght_tt+len(ttV)*wght_ttV+len(dy)*wght_dy+len(ww)*wght_ww+len(wz)*wght_wz+len(zz)*wght_zz+len(st)*wght_st+len(dm2)*wght_dm2)
	#        sig = len(dm2)*wght_dm2

	wght_dm =  x_dm1t *lumi/ another_evt
	bkg = np.sqrt(len(tt)*wght_tt+len(ttV)*wght_ttV+len(dy)*wght_dy+len(ww)*wght_ww+len(wz)*wght_wz+len(zz)*wght_zz+len(st)*wght_st+len(dm)*wght_dm)
	sig = len(dm)*wght_dm

	sn = sig / bkg
	x5.append(i)
	y5.append(sn)


for i in range(1000):
	if y5[i] == max(y5):
		print(x5[i], "max met cut")
		print(y5[i], "significance")

tt_0 = np.load('met_array/met_e0.npy')
tt_1 = np.load('met_array/met_e1.npy')
tt_2 = np.load('met_array/met_e2.npy')
tt_3 = np.load('met_array/met_e3.npy')
tt_4 = np.load('met_array/met_e4.npy')
tt_5 = np.load('met_array/met_e5.npy')
tt_6 = np.load('met_array/met_e6.npy')
tt_7 = np.load('met_array/met_e7.npy')
ttV = np.load('met_array/met_ttV.npy')
dy = np.load('met_array/met_dy.npy')
ww = np.load('met_array/met_ww.npy')
wz = np.load('met_array/met_wz.npy')
zz = np.load('met_array/met_zz.npy')
st = np.load('met_array/met_st.npy')
dm = np.load('met_array/met_sp2_0p8t.npy')
tt = np.concatenate((tt_0,tt_1,tt_2,tt_3,tt_4,tt_5,tt_6,tt_7),axis=0)
x6 = []
y6 = []
for i in range(1000):
	j = 1000 - i
	mask = (tt < j)
	tt = tt[mask]
	mask = (ttV < j)
	ttV = ttV[mask]
	mask = (dy < j)
	dy = dy[mask]
	mask = (ww < j)
	ww = ww[mask]
	mask = (wz < j)
	wz = wz[mask]
	mask = (zz < j)
	zz = zz[mask]
	mask = (st < j)
	st =  st[mask]
	mask = (dm < j)
	dm = dm[mask]
	#mask = (dm2 > i)
	#dm2 = dm2[mask]
	wght_tt = x_tt * lumi/ tt_gen_evt
	wght_ttV = x_ttV *lumi/ another_evt
	wght_dy =  x_dy *lumi/ another_evt
	wght_ww =  x_ww *lumi/ another_evt
	wght_wz = x_wz *lumi/ another_evt
	wght_zz =  x_zz *lumi/ another_evt
	wght_st =  x_st *lumi/ another_evt
	#wght_dm2 =  x_dm2t *lumi/ another_evt
	#        bkg = np.sqrt(len(tt)*wght_tt+len(ttV)*wght_ttV+len(dy)*wght_dy+len(ww)*wght_ww+len(wz)*wght_wz+len(zz)*wght_zz+len(st)*wght_st+len(dm2)*wght_dm2)
	#        sig = len(dm2)*wght_dm2

	wght_dm =  x_dm1t *lumi/ another_evt
	bkg = np.sqrt(len(tt)*wght_tt+len(ttV)*wght_ttV+len(dy)*wght_dy+len(ww)*wght_ww+len(wz)*wght_wz+len(zz)*wght_zz+len(st)*wght_st+len(dm)*wght_dm)
	sig = len(dm)*wght_dm

	sn = sig / bkg
	x6.append(j)
	y6.append(sn)
#	print(i,j)

for i in range(1000):
	if y6[i] == max(y6):
		print(x6[i], "max met cut")
		print(y6[i], "significance")
'''

'''
## normalize
tt_gen_evt = 10000000
another_evt = 1000000
wght_tt = np.ones(tt.shape) * x_tt * lumi/ tt_gen_evt
wght_ttV = np.ones(ttV.shape) * x_ttV *lumi/ another_evt
wght_dy = np.ones(dy.shape) * x_dy *lumi/ another_evt
wght_ww = np.ones(ww.shape) * x_ww *lumi/ another_evt
wght_wz = np.ones(wz.shape) * x_wz *lumi/ another_evt
wght_zz = np.ones(zz.shape) * x_zz *lumi/ another_evt
wght_st = np.ones(st.shape) * x_st *lumi/ another_evt

wght_dm = np.ones(dm.shape) * x_dm1t *lumi/ another_evt
#wght_dm2 = np.ones(dm2.shape) * x_dm2t *lumi/ another_evt





stak = [np.clip(st,0,1000,out=st),np.clip(zz,0,1000,out=zz),np.clip(wz,0,1000,out=wz),np.clip(ww,0,1000,out=ww),np.clip(dy,0,1000,out=dy),np.clip(ttV,0,1000,out=ttV),np.clip(tt,0,1000,out=tt)]


stak = [st,zz,wz,ww,dy,ttV,tt]
we = [wght_st,wght_zz, wght_wz, wght_ww, wght_dy, wght_ttV, wght_tt]
co = ['dodgerblue','green','yellow','violet','cyan','slategray','blue']
co2 = ['black','black','black', 'black', 'black','black','black']
la = ['Single top','ZZ','WZ','WW','Drell-Yan','Top pair + V','Top pair']


## Plotting
plt.style.use(hep.style.CMS)
plt.xlim(0,1000)
plt.ylim(0.0000001, 100000000000000)
#plt.ylim(0,700000)
plt.hist(stak, range=(0,1000), weights=we, bins=20, color=co, label = la, stacked=True)
plt.hist(stak, range=(0,1000), weights=we, bins=20, color=co2,histtype='step', stacked=True)
plt.hist(dm, range=(0,1000), weights=wght_dm, bins=20, color='red',histtype='step', label='$M$$_{\chi}$ = 10 GeV\n$M$$_{Y}$ = 1 TeV')
plt.hist(dm2, range=(0,1000), weights=wght_dm2, bins=20, color='darkred',histtype='step', label='$M$$_{\chi}$ = 10 GeV\n$M$$_{Y}$ = 2 TeV')
plt.yscale('log')
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)
plt.title("$\sqrt{s}$ = 14 TeV, L = 3.0 ab$^{-1}$", loc='left',fontsize=15)
plt.xlabel("Sub-leading lepton $M$$_{T}$ [GeV]",fontsize=15)
#plt.xlabel("$E$$^{miss}_{T}$ [GeV]", fontsize=15)
plt.ylabel("Expected Number of Events | 50 GeV", fontsize=15)
plt.minorticks_on()
plt.legend(fontsize=12)
plt.savefig("mt_14TeV_sublog.png")



## cut plot
plt.style.use(hep.style.CMS)
#plt.plot(x1,y1,color = 'red', label = 'Sub-leading Lepton $M$$_{T}$')
#plt.plot(x2,y2,color = 'yellow', label = 'Leading Lepton $M$$_{T}$')
#plt.plot(x3,y3,color = 'green', label = 'Dilepton $M$$_{T}$')
#plt.plot(x4,y4,color = 'black', label = '$M$$_{T2}$')
plt.plot(x5,y5,color = 'blue', label = 'over $E$$^{miss}_{T}$')
plt.plot(x6,y6,color = 'red', label = 'below $E$$^{miss}_{T}$')

plt.xlim(0,1000)
plt.ylim(0,1.0)
plt.xlabel("Cut Value [GeV]", fontsize=15)
plt.ylabel("Significance", fontsize=15)
plt.minorticks_on()
plt.title("$\sqrt{s}$ = 14 TeV, L = 3.0 ab$^{-1}$", loc='left',fontsize=15)
plt.legend(fontsize=12)
plt.savefig("test_s2_0p1t.png")
'''
