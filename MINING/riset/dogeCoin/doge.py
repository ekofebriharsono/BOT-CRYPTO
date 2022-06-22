import time
import initFunctionDoge as fs


print("Add Miner")
fs.addDataMiner("eko","EC-UserId-619418","DOGEToken=qMFJW4NLodtg1YSu86f8jp7rMLiYDW6M; PHPSESSID=fgm3iin4cnq8tkeol5k47deiq6; bitmedia_fid=eyJmaWQiOiI3ZWY5YjJlNWZjZDY4MjJiZmM4NDMzOWQ4OTllYjA1NiIsImZpZG5vdWEiOiI1MmQxMmZkZjE3YjIyYzU1NmZhODYzYTFiNjQwYzg0NCJ9; HstCfa4244642=1639838223307; HstCmu4244642=1639838223307; HstCnv4244642=1; _cc_id=84cfc66236cf2e4539b20485b5e33ae5; _cc_cc=ACZ4XmNQsDBJTks2MzMyNktOM0o1MTW2TDIyMLEwTTJNNTZOTDVlAILEvZ9EQTQEcF87r874UZbhPyMjw7mjh5hh7O4vljDm7n2XBWDs1+uecsPYhxfPYYGx3y1BsI9vmgIX/9BwH6736o+1OjD1z5D0AgAprjnP; _cc_aud=ABR4XmNgYGBI3PtJFEhBADMDA9cMMHNRK4hkfFgPJAFnvAVT; panoramaId_expiry=1639924629719; __dtsu=4C301639838225B5E20E10D6898CDC05; sticky_ads_view_53016_22811=1; HstCla4244642=1639839402168; HstPn4244642=9; HstPt4244642=9; HstCns4244642=2")
fs.addDataMiner("adhiq","EC-UserId-620435","DOGEToken=Z6nhDmFlM8BQmrtGp4j5uxUCvYhxzE3W; PHPSESSID=l0vtnihsc3k7thmid0baskg5j7; __dtsu=6D001639548790820464C42E7731E768; HstCfa4244642=1639840293615; HstCla4244642=1639840366053; HstCmu4244642=1639840293615; HstPn4244642=2; HstPt4244642=2; HstCnv4244642=1; HstCns4244642=1; bitmedia_fid=eyJmaWQiOiIxYjgxNzA4YzViYWI3ZTI3ZjI4NjgxMDA0ZmVhMzlhNSIsImZpZG5vdWEiOiIyNzFlMThjMGRmZTk0ZjRkYjAxMjgxOGU3NWExZmIwNSJ9; sticky_ads_view_53016_22811=1")
# fs.addDataMiner("ulum","EC-UserId-620774","PHPSESSID=b71d0386ef562df837e6acf7b704f992; __dtsu=6D001639548790820464C42E7731E768; SHIBToken=wFxRMgmcYXRfUo6TpvhtLhOV7z7EBNvh")
# fs.addDataMiner("nawawi","EC-UserId-622302","PHPSESSID=5c5a5e5d0ebdee07b5181df142f7905f; __dtsu=10401639837084414030CA6A57F96C1D; SHIBToken=fqdjmQ36d1yNoPsCmjyjjaPKit10l1FN")
fs.addDataMiner("hasbi","EC-UserId-570852","DOGEToken=CSYywnrgBygKDrGRxZcnNn122O3SQmPg; __dtsu=6D0016374349384D4AD8CD19448AC406; _cc_id=8ee29ad9ddde652c1b4feacfdea93627; bitmedia_fid=eyJmaWQiOiI1NTM1MDY3NmNkZDE2NWRiMDAzY2UwMTQ1ODQ3MTlkYyIsImZpZG5vdWEiOiIwNjc5ZTY5MWQ0YjcxZDZhMjk3NjFlOGRjMzhlZTg2OSJ9; HstCfa4244642=1639668805681; HstCmu4244642=1639668805681; PHPSESSID=r5ucsgaf8t67t0t7dsbesi67q1; HstCnv4244642=2; sticky_ads_view_53016_22811=1; HstCns4244642=3; panoramaId_expiry=1639908935775; HstCla4244642=1639823475097; HstPn4244642=96; HstPt4244642=101")

while True:
	print("Starting DOGE")
	for data in fs.dataMiner:
		try:
			wallet = data[1]
			name = data[0]
			cookie = data[2]
			
			if "EC" not in wallet: 
				exit("Your Wallet Invalid!")
			else: 
				print("Doge")
				fs.appDoge(cookie , name)

		except KeyboardInterrupt:
			exit()
	time.sleep(60)