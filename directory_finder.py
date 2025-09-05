import requests
url = input("Enter the domain to find directories:")
wordlist = input("Enter the path of the Wordlist:") #path of the wordlist that contains directories
with open(wordlist, "r") as file:
	words = [line.strip() for line in file]
found_urls = []
if not url.endswith("/"):
	url += "/"
for i in words:
	fullurl = url + i
	try:
		response = requests.get(fullurl)
		stcode = response.status_code
		if stcode in [200, 301, 302]:
			found_urls.append(fullurl)
			print(f"[+] {fullurl} Found | Status: {stcode}")
	except requests.exceptions.RequestException as e:
		print(f"[-] Error accessing {fullurl}: {e}")
#for writing found urls inside a .txt file
option = input("Do you want to save the found urls? (yes/no):")
if option == "yes":
	with open("found_directories.txt", "a") as f1:
		for urls in found_urls:
			f1.write(urls + "\n")
	print(f"Saved {len(found_urls)} inside found_directories.txt")
print(f"Scanned {len(words)} directories.")
