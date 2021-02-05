import uproot as ROOT
import uproot_methods as upm
import numpy as np
import awkward1 as ak
import numba, numpy

###############################################
##### All of this code made by Taiwoo Kim #####
##### Lab 208, NS1, Department of Physics #####
######## Kyungpook National University ########
############### Daegu, KOREA ##################
############# resisov@nate.com ################
###############################################

## This is prototype ver 1.2.0                                     ##
## Array Based Calculaor for massless daughter particles!          ##
## Usage : import mt2calculator                                    ##
##         ABC = Mt2()                                             ##
##         results = ABC.cal_mt2(pt1, phi1, pt2, phi2, met, phi3)  ##
##         print(results)                                          ##
## Please input visible daughers at 1 and 2, and input met at 3    ##
## Have a good day and please cite my paper arXiV: coming soon     ##
## and also cite associated mt2 papers arXiV:                      ##
##                                     arXiV:                      ##
##                                     arXiV:                      ##


class Mt2:
	def cal_mt2(self,pt1,phi1,pt2,phi2,met,phi3):
		visApx = pt1 * np.cos(phi1)
		visApy = pt1 * np.sin(phi1)
		visBpx = pt2 * np.cos(phi2)
		visBpy = pt2 * np.sin(phi2)
		invpx = met * np.cos(phi3)
		invpy = met * np.sin(phi3)
		return self.get_mt2(visApx, visApy, visBpx, visBpy, invpx, invpy)

	def get_mt2(self,visApx, visApy, visBpx, visBpy, invpx, invpy):
		global invVector
		global visAVector
		global visBVector
		invVector = np.array([np.zeros(invpx.shape),invpx,invpy])
		visAVector = np.array([np.zeros(visApx.shape),visApx,visApy])
		visBVector = np.array([np.zeros(visBpx.shape),visBpx,visBpy])
		return self.massless(visAVector,visBVector,invVector)

	def massless(self,visAVector,visBVector,invVector):
		pax = visAVector[1]
		pay = visAVector[2]
		pbx = visBVector[1]
		pby = visBVector[2]
		pmissx = invVector[1]
		pmissy = invVector[2]

		test_pax = []
		test_pay = []
		test_pbx = []
		test_pby = []
		test_pmissx = []
		test_pmissy = []
		for i in range(len(pax)):
			test_pax.append(pax[i])
			test_pay.append(pay[i])
			test_pbx.append(pbx[i])
			test_pby.append(pby[i])
			test_pmissx.append(pmissx[i])
			test_pmissy.append(pmissy[i])

		pax = np.array(test_pax)
		pay = np.array(test_pay)
		pbx = np.array(test_pbx)
		pby = np.array(test_pby)
		pmissx = np.array(test_pmissx).flatten()
		pmissy = np.array(test_pmissy).flatten()

		masq = np.zeros(pax.shape)
		Easq = pax * pax + pay * pay
		Ea = np.sqrt(Easq)
		mbsq = np.zeros(pax.shape)
		Ebsq = pbx * pbx + pby * pby
		Eb = np.sqrt(Ebsq)
		pmissxsq = pmissx * pmissx
		pmissysq = pmissy * pmissy
		scale = np.ones(pax.shape)
		metsq = (pmissxsq + pmissysq) ** 0.5

		for i in range(len(Ea)):
			if (Ea[i] > Eb[i]):
				scale[i] = Ea[i] / 100
			elif (Ea[i] < Eb[i]):
				scale[i] = Eb[i] / 100
			if Ea[i] == 0:
				scale[i] = 1
			if ((metsq / 100)[i] > scale[i]):
				scale[i] = metsq[i] / 100
		print("ok")

		scalesq = scale * scale
		pax /= scale
		pay /= scale
		pbx /= scale
		pby /= scale
		Ea /= scale
		Eb /= scale
		Easq /= scalesq
		Ebsq /= scalesq

		pmissx /= scale
		pmissy /= scale
		pmissxsq /= scalesq
		pmissysq /= scalesq
		precision = np.ones(pax.shape) * 0.001

		theta = np.zeros(pax.shape)
		for i in range(len(theta)):
			if pax[i] != 0:
				theta[i] = np.arctan(pay[i]/pax[i])

		s = np.sin(theta)
		c = np.cos(theta)
		pxtemp = pax * c + pay * s
		pax = pxtemp
		pay = np.zeros(pax.shape)
		pxtemp = pbx * c + pby * s
		pytemp = -s * pmissx + c * pmissy
		pbx = pxtemp
		pby = pytemp
		pxtemp = pmissx * c + pmissy * s
		pytemp = -s * pmissx + c * pmissy
		pmissx = pxtemp
		pmissy = pytemp

		a2 = 1 - pbx * pbx / (Ebsq)
		b2 = -pbx * pby/(Ebsq)
		c2 = 1 - pby * pby / (Ebsq)
		d21 = (Easq * pbx) / Ebsq
		d20 = - pmissx + (pbx*(pbx * pmissx + pby *pmissy)) / Ebsq
		e21 = (Easq * pby) / Ebsq
		e20 = -pmissy + (pby * (pbx * pmissx + pby * pmissy)) / Ebsq
		f22 = -(Easq * Easq / Ebsq)
		f21 = -2 * Easq * (pbx * pmissx + pby * pmissy) / Ebsq
		f20 = 0.0 + pmissxsq + pmissysq - (pbx * pmissx + pby * pmissy) * (pbx * pmissx + pby * pmissy) / Ebsq

		Deltasq0 = 0.0
		Deltasq_low = Deltasq0 + precision
		nsols_low = self.nsols_massless(Deltasq_low,Easq,d21,d20,e21,e20,f22,f21,f20,pax,Ea,a2,b2,c2)

		mt2_b = np.ones(nsols_low.shape)

		for i in range(len(mt2_b)):
			if (nsols_low[i] > 1):
				mt2_b[i] = 0

		Deltasq_high1 = 2 * Eb * (pmissx*pmissx + pmissy*pmissy)**0.5 -2 * pbx * pmissx -2 *pby * pmissy
		Deltasq_high2 = np.zeros(Deltasq_high1.shape)
		Deltasq_high = Deltasq_high1

		for i in range(len(Deltasq_high)):
			if (Deltasq_high1[i] < Deltasq_high2[i]):
				Deltasq_high[i] = Deltasq_high2[i]

		nsols_high = self.nsols_massless(Deltasq_high,Easq,d21,d20,e21,e20,f22,f21,f20,pax,Ea,a2,b2,c2)
		minmass = np.zeros(nsols_high.shape)
		maxmass = minmass
		for i in range(len(nsols_high)):
			if (nsols_high[i] == nsols_low[i]):
				foundhigh=0
				#minmass = np.zeros(nsols_high.shape) # mn
				maxmass[i] = Deltasq_high[i]**0.5

				for mass in range(0,int(maxmass[i]*10)):
					Deltasq_high[i] = mass*mass/100 - 0 #mnsq
					if (nsols_high[i]>0):
						foundhigh=1
						Deltasq_low[i] = (mass-0.1)*(mass-0.1) - 0 #mnsq
				if foundhigh==0:
					mt2_b[i] = np.sqrt(Deltasq_low[i]+0) #mnsq

				if (nsols_high[i] == nsols_low[i]):
					mt2_b[i] =  np.sqrt(Deltasq_low[i])

		minmass = Deltasq_low ** 0.5
		maxmass = Deltasq_high ** 0.5
		midmass = np.zeros(maxmass.shape)
		Delta_mid = np.zeros(maxmass.shape)
		nsols_mid = np.zeros(maxmass.shape)
		print("debug")
		cnt = 0
		for i in range(len(maxmass)):
			while (maxmass[i] -minmass[i] > precision[i]):
				midmass[i] = (minmass[i]+maxmass[i])/2.
				Delta_mid = midmass[i] * midmass[i] - 0 #mnsq
				nsols_mid = self.nsols_onepoint(Delta_mid,Easq[i],d21[i],d20[i],e21[i],e20[i],f22[i],f21[i],f20[i],pax[i],Ea[i],a2[i],b2[i],c2[i])
				if (nsols_mid != nsols_low[i]):
					maxmass[i] = midmass[i]
				if (nsols_mid == nsols_low[i]):
					minmass[i] = midmass[i]
			mt2_b[i] = minmass[i]
			cnt += 1
			if (cnt % 1000 == 0):
				print("Don't worry",cnt)

		print("Mt2 Finish")
		print(mt2_b)
		return mt2_b


	def nsols_onepoint(self,Dsq,Easq,d21,d20,e21,e20,f22,f21,f20,pax,Ea,a2,b2,c2):
		delta = Dsq / (2*Easq)
		d2 = d21 * delta + d20
		e2 = e21 * delta + e20
		f2 = f22 * delta * delta + f21 * delta + f20
		a = 1
		b = 1
		if pax > 0:
			a = Ea / Dsq
			b = -Dsq / (4 * Ea)
		else:
			a = -Ea / Dsq
			b = Dsq / (4 * Ea)

		A4 = a*a*a2
		A3 = 2*a*b2/Ea
		A2 = (2*a*a2*b+c2+2*a*d2)/(Easq)
		A1 = (2*b*b2+2*e2)/(Easq*Ea)
		A0 = (a2*b*b+2*b*d2+f2)/(Easq*Easq)

		A0sq = A0 * A0
		A1sq = A1 * A1
		A2sq = A2 * A2
		A3sq = A3 * A3
		A4sq = A4 * A4

		B3 = 4 * A4
		B2 = 3* A3
		B1 = 2 * A2
		B0 = A1
		C2 = -(A2/2 - 3*A3sq/(16*A4))
		C1 = -(3*A1/4. -A2*A3/(8*A4))
		C0 = -A0 + A1*A3/(16*A4)
		D1 = -B1 - (B3*C1*C1/C2 - B3*C0 -B2*C1)/C2
		D0 = -B0 -B3 * C0 * C1 / (C2*C2) + B2*C0/C2
		E0 = -C0 - C2 * D0 * D0 / (D1 * D1) + C1 * D0 / D1

		t1 = A4
		t2 = A4
		t3 = C2
		t4 = D1
		t5 = E0    
		nsol = self.signone_n(t1,t2,t3,t4,t5) - self.signone_p(t1,t2,t3,t4,t5)
		return nsol

	def nsols_massless(self,Dsq,Easq,d21,d20,e21,e20,f22,f21,f20,pax,Ea,a2,b2,c2):
		delta = Dsq / (2*Easq)
		d2 = d21 * delta + d20
		e2 = e21 * delta + e20
		f2 = f22 * delta * delta + f21 * delta + f20
		a = np.ones(delta.shape)
		b = np.ones(delta.shape)

		for i in range (len(pax)):
			if (pax[i] > 0):
				a[i] = Ea[i] / Dsq[i]
				b[i] = -Dsq[i] / (4 * Ea[i])
			else:
				a[i] = -Ea[i] / Dsq[i]
				b[i] = Dsq[i] / (4 * Ea[i])
		A4 = a*a*a2
		A3 = 2*a*b2/Ea
		A2 = (2*a*a2*b+c2+2*a*d2)/(Easq)
		A1 = (2*b*b2+2*e2)/(Easq*Ea)
		A0 = (a2*b*b+2*b*d2+f2)/(Easq*Easq)

		A0sq = A0 * A0
		A1sq = A1 * A1
		A2sq = A2 * A2
		A3sq = A3 * A3
		A4sq = A4 * A4

		B3 = 4 * A4
		B2 = 3* A3
		B1 = 2 * A2
		B0 = A1
		C2 = -(A2/2 - 3*A3sq/(16*A4))
		C1 = -(3*A1/4. -A2*A3/(8*A4))
		C0 = -A0 + A1*A3/(16*A4)
		D1 = -B1 - (B3*C1*C1/C2 - B3*C0 -B2*C1)/C2
		D0 = -B0 -B3 * C0 * C1 / (C2*C2) + B2*C0/C2
		E0 = -C0 - C2 * D0 * D0 / (D1 * D1) + C1 * D0 / D1

		t1 = A4
		t2 = A4
		t3 = C2
		t4 = D1
		t5 = E0
		nsol = self.signchange_n(t1,t2,t3,t4,t5) - self.signchange_p(t1,t2,t3,t4,t5)
		return nsol



	def signchange_n(self,t1,t2,t3,t4,t5):
		nsc = np.zeros(t1.shape)
		for i in range(len(t1)):
			if (t1[i] * t2[i] > 0):
				nsc[i] += 1
			if (t2[i] * t3[i] > 0):
				nsc[i] += 1
			if (t3[i] * t4[i] > 0):
				nsc[i] += 1
			if (t4[i] * t5[i] > 0):
				nsc[i] += 1
		return nsc


	def signchange_p(self,t1,t2,t3,t4,t5):
		nsc = np.zeros(t1.shape)
		for i in range(len(t1)):
			if (t1[i] * t2[i] < 0):
				nsc[i] += 1
			if (t2[i] * t3[i] < 0):
				nsc[i] += 1
			if (t3[i] * t4[i] < 0):
				nsc[i] += 1
			if (t4[i] * t5[i] < 0):
				nsc[i] += 1
		return nsc

	def signone_n(self,t1,t2,t3,t4,t5):
		nsc = 0
		if t1 * t2 > 0:
			nsc += 1
		if t2 * t3 > 0:
			nsc += 1
		if t3 * t4 > 0:
			nsc += 1
		if t4 * t5 > 0:
			nsc += 1
		return nsc

	def signone_p(self,t1,t2,t3,t4,t5):
		nsc = 0
		if t1 * t2 < 0:
			nsc += 1
		if t2 * t3 < 0:
			nsc += 1
		if t3 * t4 < 0:
			nsc += 1
		if t4 * t5 < 0:
			nsc += 1
		return nsc
