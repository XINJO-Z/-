while True :
	t = input ('請輸入要轉換的單位：')
	if t == '溫度'  :
		tem = input ('請輸入要轉換的溫度單位(攝氏/華氏)：')
		if tem == '攝氏':
			c = input ('請輸入數值：')
			c = float(c)
			c_a = c * 9 / 5 + 32
			print ('華氏為：',c_a)
		elif tem == '華氏':
			f = input ('請輸入數值：')
			f = float(f)
			f_a = (f - 32) * 5 / 9
			print ('攝氏為：',f_a)
		elif tem != '攝氏' or tem != '華氏' :
			print ('請輸入(攝氏/華氏)')
	if t == ('長度') :
		le = input ('請輸入要轉換的長度單位(公分/英吋)：')
		if le == '公分' :
			cm = input ('請輸入數值：')
			cm = float(cm)
			cm = cm * 2.54
			print ('英吋為：',cm)
		elif le == '英吋' :
			inch = input ('請輸入數值：')
			inch = float(inch)
			inch = inch / 2.54
			print ('公分為：',inch)
		elif tem != '公分' or tem != '英吋' :
			print ('請輸入(公分/英吋)')
	else :
		print ('目前只支援轉換溫度／長度')