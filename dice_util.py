def mergeseg(s):
	if s == []:
		return s
	res = [s[0]]
	indr = 0
	for i in range(1,len(s)):
		if s[i][0] < res[0][1]:
			res[0][1] = s[i][1]
		else:
			res.append(s[i])
			indr += 1
	return res


def intersecseg(s1,s2):
	ls1 = len(s1)
	ls2 = len(s2)

	res = []
	for seg1 in s1:
		for seg2 in s2:
			if seg1[1] < seg2[0] or seg2[1] < seg1[0]:
				continue
			nl = max(seg1[0],seg2[0])
			nr = min(seg1[1],seg2[1])
			res.append([nl,nr])
	res.sort()
	return mergeseg(res)

def calsegLen(s):

	if s == []:
		return 0
	res = 0
	for seg in s:
		res += seg[1] - seg[0]
	return res


def dice(s1,s2):
	s1.sort()
	s2.sort()
	inter = intersecseg(s1,s2)
	leninter = calsegLen(inter)

	len1 = calsegLen(s1)
	len2 = calsegLen(s2)
	lensum = len1+len2

	if lensum == 0:
		return 1

	res = 2 * leninter/lensum

	return res
