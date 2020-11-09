import uproot as ROOT
import uproot_methods as upm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
import mplhep as hep
import sys


## argument check
try:
  input = raw_input
except:
  pass



if len(sys.argv) < 2:
	print(" running method: macro_file_name.py input_file_name.root")

## Read your Tree
dat1 = ROOT.open(sys.argv[1])["Delphes"]
dat2 = ROOT.open(sys.argv[2])["Delphes"]
dat3 = ROOT.open(sys.argv[3])["Delphes"]
dat4 = ROOT.open(sys.argv[4])["Delphes"]
dat5 = ROOT.open(sys.argv[5])["Delphes"]
dat6 = ROOT.open(sys.argv[6])["Delphes"]
dat7 = ROOT.open(sys.argv[7])["Delphes"]

## Convert ROOT to jagged arrays
MET1_arr, Elec1_PT_arr, Muon1_PT_arr, Jet1_PT_arr = dat1.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)
MET2_arr, Elec2_PT_arr, Muon2_PT_arr, Jet2_PT_arr = dat2.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)
MET3_arr, Elec3_PT_arr, Muon3_PT_arr, Jet3_PT_arr = dat3.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)
MET4_arr, Elec4_PT_arr, Muon4_PT_arr, Jet4_PT_arr = dat4.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)
MET5_arr, Elec5_PT_arr, Muon5_PT_arr, Jet5_PT_arr = dat5.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)
MET6_arr, Elec6_PT_arr, Muon6_PT_arr, Jet6_PT_arr = dat6.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)
MET7_arr, Elec7_PT_arr, Muon7_PT_arr, Jet7_PT_arr = dat7.arrays(['MissingET.MET', 'Electron.PT', 'Muon.PT', 'Jet.PT'],outputtype=tuple)


## preselection
# lepton cut
nl2_cut_MET1 = MET1_arr[((Elec1_PT_arr.count()) + (Muon1_PT_arr.count()) >= 2)]
nl2_cut_MET2 = MET2_arr[(Elec2_PT_arr.count()) + (Muon2_PT_arr.count()) >= 2]
nl2_cut_MET3 = MET3_arr[(Elec3_PT_arr.count()) + (Muon3_PT_arr.count()) >= 2]
nl2_cut_MET4 = MET4_arr[(Elec4_PT_arr.count()) + (Muon4_PT_arr.count()) >= 2]
nl2_cut_MET5 = MET5_arr[(Elec5_PT_arr.count()) + (Muon5_PT_arr.count()) >= 2]
nl2_cut_MET6 = MET6_arr[(Elec6_PT_arr.count()) + (Muon6_PT_arr.count()) >= 2]
nl2_cut_MET7 = MET7_arr[(Elec7_PT_arr.count()) + (Muon7_PT_arr.count()) >= 2]

# jet cut
j2_nl2_cut_MET1 = MET1_arr[((Elec1_PT_arr.count()) + (Muon1_PT_arr.count()) >= 2) & ((Jet1_PT_arr.count()) >= 2)]
j2_nl2_cut_MET2 = MET2_arr[((Elec2_PT_arr.count()) + (Muon2_PT_arr.count()) >= 2) & ((Jet2_PT_arr.count()) >= 2)]
j2_nl2_cut_MET3 = MET3_arr[((Elec3_PT_arr.count()) + (Muon3_PT_arr.count()) >= 2) & ((Jet3_PT_arr.count()) >= 2)]
j2_nl2_cut_MET4 = MET4_arr[((Elec4_PT_arr.count()) + (Muon4_PT_arr.count()) >= 2) & ((Jet4_PT_arr.count()) >= 2)]
j2_nl2_cut_MET5 = MET5_arr[((Elec5_PT_arr.count()) + (Muon5_PT_arr.count()) >= 2) & ((Jet5_PT_arr.count()) >= 2)]
j2_nl2_cut_MET6 = MET6_arr[((Elec6_PT_arr.count()) + (Muon6_PT_arr.count()) >= 2) & ((Jet6_PT_arr.count()) >= 2)]
j2_nl2_cut_MET7 = MET7_arr[((Elec7_PT_arr.count()) + (Muon7_PT_arr.count()) >= 2) & ((Jet7_PT_arr.count()) >= 2)]


## Normalization factor
x_ttbar = 50.9
x_ww = 5.142
x_wz = 2.075
x_zz = 0.397
x_singletop = 2.289
x_dm10 = 0.0002683
x_dm100 = 0.0002523
lumi = 150000

tot_evt = 10000.0
tot_evt2 = 100000.0


ttbar = j2_nl2_cut_MET1.flatten()
ww = j2_nl2_cut_MET2.flatten()
wz = j2_nl2_cut_MET3.flatten()
zz = j2_nl2_cut_MET4.flatten()
sintop = j2_nl2_cut_MET5.flatten()
dm10 = j2_nl2_cut_MET6.flatten()
dm100 = j2_nl2_cut_MET7.flatten()

'''
ttbar = Elec1_PT_arr.flatten()
ww = Elec2_PT_arr.flatten()
wz = Elec3_PT_arr.flatten()
zz = Elec4_PT_arr.flatten()
sintop = Elec5_PT_arr.flatten()
dm10 = Elec6_PT_arr.flatten()
dm100 = Elec7_PT_arr.flatten()


ttbar = Muon1_PT_arr.flatten()
ww = Muon2_PT_arr.flatten()
wz = Muon3_PT_arr.flatten()
zz = Muon4_PT_arr.flatten()
sintop = Muon5_PT_arr.flatten()
dm10 = Muon6_PT_arr.flatten()
dm100 = Muon7_PT_arr.flatten()


ttbar = Jet1_PT_arr.flatten()
ww = Jet2_PT_arr.flatten()
wz = Jet3_PT_arr.flatten()
zz = Jet4_PT_arr.flatten()
sintop = Jet5_PT_arr.flatten()
dm10 = Jet6_PT_arr.flatten()
dm100 = Jet7_PT_arr.flatten()
'''

weight_ttbar = np.ones(ttbar.shape) * x_ttbar * lumi / tot_evt2
weight_ww = np.ones(ww.shape) * x_ww * lumi / tot_evt
weight_wz = np.ones(wz.shape) * x_wz * lumi / tot_evt
weight_zz = np.ones(zz.shape) * x_zz * lumi / tot_evt
weight_singletop = np.ones(sintop.shape) * x_singletop * lumi / tot_evt
weight_dm10 = np.ones(dm10.shape) * x_dm10 * lumi / tot_evt
weight_dm100 = np.ones(dm100.shape) * x_dm100 * lumi / tot_evt

## stack variables setting
x = [sintop,zz,wz,ww,ttbar]
we = [weight_singletop,weight_zz,weight_wz,weight_ww,weight_ttbar]
co = ['yellow','purple', 'limegreen', 'cyan', 'blue']
la = ['Single top', 'ZZ', 'WZ', 'WW', 'top pair']


## Draw histogram
plt.style.use(hep.style.ROOT)
plt.rcParams["figure.figsize"] = (8,8)
plt.xlim(0,500)
plt.ylim(0.01, 100000000)
plt.hist(x, range=(0,500), weights=we, bins=8, color=co, label = la, stacked=True)
plt.hist(dm10, range=(0,500),weights=weight_dm10, bins=8, label='$M$$_{\chi}$ = 10 GeV',color='red', histtype='step')
plt.hist(dm100, range=(0,500),weights=weight_dm100, bins=8, label='$M$$_{\chi}$ = 100 GeV',color='darkred', histtype='step')


plt.yscale('log')
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)
plt.title("$\sqrt{s}$ = 13 TeV, L = 150 fb$^{-1}$", loc='left',fontsize=15)
plt.xlabel("$E$$^{miss}_{T}$ [GeV]", fontsize=15)
#plt.xlabel("Jet $p$$_{T}$ [GeV]", fontsize=15)
#plt.xlabel("Electron $p$$_{T}$ [GeV]", fontsize=15)
#plt.xlabel("Muon $p$$_{T}$ [GeV]", fontsize=15)
plt.ylabel("Expected Number of Events | 40 GeV", fontsize=15)
plt.minorticks_on()
plt.legend(fontsize=12)
plt.savefig("pre_met_j2l2.png")

