t = input ('請輸入要轉換的溫度單位：')
if t == '攝氏':
	c = input ('請輸入數值：')
	c = float(c)
	c_a = c * 9 / 5 + 32
	print ('華氏為：',c_a)
if t == '華氏':
	f = input ('請輸入數值：')
	f = float(f)
	f_a = f - 32 * 5 / 9
	print ('攝氏為：',f_a)