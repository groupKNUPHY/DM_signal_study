from rootpy.io import root_open
from rootpy.plotting import Hist, HistStack, Legend, Canvas

## rootpy for matplotlib 
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
import rootpy.plotting.root2matplotlib as rplt

## opening your own root file. please change "input*.root" to your own file name
myfile1 = root_open("../DM_10GeV_bpt.root")
myfile2 = root_open("../DM_20GeV_bpt.root")
myfile3 = root_open("../DM_50GeV_bpt.root")
myfile4 = root_open("../DM_100GeV_bpt.root")
myfile5 = root_open("../BKG_ttbar_bpt.root")
#myfile3 = root_open(".root")
#myfile4 = root_open("input4.root")
#myfile5 = root_open("input5.root")
#myfile6 = root_open("input6.root")

## cloning your histogram input*.root file.
## please change pt term to your own name of histogram

## Normaliztion factor
xsec1 = 0.0002683
xsec2 = 0.0002647
xsec3 = 0.0002629
xsec4 = 0.0002523
xsec5 = 50.9

lumi = 150.0

tot_evt = 10000.0
tot_evt2 = 100000.0

weight1 = xsec1 * lumi / tot_evt
weight2 = xsec2 * lumi / tot_evt 
weight3 = xsec3 * lumi / tot_evt
weight4 = xsec4 * lumi / tot_evt
weight5 = xsec5 * lumi / tot_evt2

myhist1 = myfile1.pt.Clone()
myhist2 = myfile2.pt.Clone()
myhist3 = myfile3.pt.Clone()
myhist4 = myfile4.pt.Clone()
myhist5 = myfile5.pt.Clone()
#myhist6 = myfile4.mpt.Clone()
#myhist7 = myfile5.met.Clone()
#myhist8 = myfile6.met.Clone()

## Normalize
myhist1.Scale(weight1)
myhist2.Scale(weight2)
myhist3.Scale(weight3)
myhist4.Scale(weight4)
myhist5.Scale(weight5)

## Set parameters for plotting
font_path = "/usr/share/fonts/stix/STIXGeneralItalic.otf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font',family=font_name)
plt.rcParams["figure.figsize"] = (10,6)
#plt.hist(myhist1,range=(0,400), bins=400, label='DM Signal Event',color='blue', histtype='step')
#plt.hist(myhist2, range=(0,400), bins=400, label='tt~ BKG',color='red', histtype='step')
#plt.hist(POW tt~ sample,range=(0,400), bins=400, label='POW tt~ sample',color='orange', histtype='step')
plt.xlim(0, 300)
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)
plt.title("b quark $p$$_{T}$", fontsize=15)
plt.title("150 fb$^{-1}$ [13 TeV]",loc='right', fontsize=15)
plt.xlabel("p$_{T}$ [GeV]", fontsize=15)
plt.ylabel("Expected Number of Events | 5 GeV", fontsize=15)
plt.yscale('log')
#plt.text(250, 200, "MADGRAPH 5",  ha='center',va='center',fontsize=25)
plt.minorticks_on()
rplt.hist(myhist1, linewidth=3,label='$\chi_D$ 10 GeV',color="darkred")
rplt.hist(myhist2, linewidth=3,label='$\chi_D$ 20 GeV',color="red")
rplt.hist(myhist3, linewidth=3,label='$\chi_D$ 50 GeV',color="tomato")
rplt.hist(myhist4, linewidth=3,label='$\chi_D$ 100 GeV',color="orange")
rplt.hist(myhist5, linewidth=3,label='top pair BKG',color="blue")
plt.legend(fontsize=15)
plt.savefig("sig_bpt.png")


