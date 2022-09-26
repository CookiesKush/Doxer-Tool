import os, shutil
from time import sleep
from colorama import Fore
from cookies_package import clear, setTitle


class Doxer:
	def __init__(self):
		self.main_banner = f"""
		{Fore.RESET}[{Fore.GREEN}1{Fore.RESET}] {Fore.LIGHTWHITE_EX}Name
		{Fore.RESET}[{Fore.GREEN}2{Fore.RESET}] {Fore.LIGHTWHITE_EX}Phone Number
		{Fore.RESET}[{Fore.GREEN}3{Fore.RESET}] {Fore.LIGHTWHITE_EX}Dead
		{Fore.RESET}[{Fore.GREEN}4{Fore.RESET}] {Fore.LIGHTWHITE_EX}IP
		{Fore.RESET}[{Fore.RED}420{Fore.RESET}] {Fore.RED}Exit
		"""

	def init(self):
		self.menu()

	def create_folder(self, str):
		if not os.path.exists(str): os.mkdir(str)
		else: 
			print(f"{Fore.LIGHTRED_EX}Folder already exists {Fore.RESET}")
			yh_no = input(f"{Fore.LIGHTWHITE_EX}Do you want to remove it? {Fore.YELLOW}[y/n]{Fore.RESET} ").lower()
			if yh_no == "y" or yh_no == "yes":
				shutil.rmtree(str)
				os.mkdir(str)
			else: print(f"{Fore.LIGHTRED_EX}Folder not removed {Fore.RESET}")

	def file_check(self, str):
		if os.path.isfile(str): 
			os.remove(str)

	def menu(self):
		setTitle("Doxer")
		clear()
		print(self.main_banner)
		option = input(f" {Fore.CYAN}Select {Fore.YELLOW}>>{Fore.RESET} ")

		if option == "1": 		# Full Name
			self.ID()
		elif option == "2":		# Phone Number
			self.PHONE()
		elif option == "3":		# Dead
			self.DEAD()
		elif option == "4":# IP
			self.IP()
		elif option == "420":	# Exit
			self.EXITMENU()
		else:					# Invalid Option
			clear()
			print(f"{Fore.LIGHTRED_EX}Please choose a valid choice !{Fore.RESET}")
			sleep(3)
			self.menu()

	def ID(self):
		setTitle("Doxer | Tab: [ID]")
		clear()
		First_name 	= input(f"{Fore.LIGHTWHITE_EX}First name {Fore.YELLOW}>>{Fore.RESET} ")
		Last_name 	= input(f"{Fore.LIGHTWHITE_EX}Last Name {Fore.YELLOW}>>{Fore.RESET} ")
		folder = f"DOX-ID-{First_name}-{Last_name}"
		self.create_folder(folder)
		clear()

		self.file_check(f'{folder}\\ID.txt')

		with open(f'{folder}\\ID.txt', 'a+') as f:
			f.writelines(f'\nhttps://pipl.com/search/?q='+Last_name+'+'+First_name)
			f.writelines(f'\nhttps://www.facebook.com/search/top/?init=quick&q='+Last_name+' '+First_name)
			f.writelines(f'\nhttps://www.spokeo.com/'+Last_name+'-'+First_name)
			f.writelines(f'\nhttps://www.flickr.com/search/people/?username='+Last_name+' '+First_name)
			f.writelines(f'\nhttps://www.linkedin.com/pub/dir/'+Last_name+'/'+First_name)
			f.writelines(f'\nhttps://plus.google.com/s/'+Last_name+' '+First_name+'/people')
			f.writelines(f'\nhttps://www.tumblr.com/search/'+Last_name+'+'+First_name)
			f.writelines(f'\nhttp://www.youtube.com/results?search_query='+Last_name+'+'+First_name)
			f.writelines(f'\nhttps://www.peekyou.com/'+Last_name+'_'+First_name)
			f.writelines(f'\nhttps://twitter.com/search?f=users&vertical=default&q= '+Last_name+' '+First_name)
			f.writelines(f'\nhttps://www.beenverified.com/lp/e030ee/1/loading?utm_id=peekyou_Peekyou_Contact_Address_Results_Button&age=&bvid=&city=&fn='+Last_name+'&ln='+First_name)
			f.writelines(f'\nhttps://www.peoplelooker.com/lp/5ee6b8/1/loading?utm_id=peekyou_peekyou_PL_phonebook_widget_web&fn='+Last_name+'&ln='+First_name+'&city=&state=&age=&bvid=&utm_source=peekyou&utm_medium=channel_partner&utm_campaign=peekyou_PL_phonebook_widget_web&utm_content=static#.')
			f.writelines(f'\nhttps://myspace.com/search?q='+Last_name+' '+First_name)
			f.writelines(f'\nhttps://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui='+Last_name+'+'+First_name)
			f.writelines(f'\nhttp://www.libramemoria.com/avis/?Nom='+Last_name+'&Prenom='+First_name)
			f.writelines(f'\nhttps://www.avis-de-deces.net/avis/par-nom/?lastname='+Last_name+'&firstname='+First_name)
		
		f.close()
		print(f"{Fore.YELLOW}Info written to {Fore.LIGHTGREEN_EX}{folder}/ID.txt")
		sleep(3)
		self.menu()

	def PHONE(self):
		setTitle("Doxer | Tab: [Phone]")
		clear() 
		Num = input(f"{Fore.LIGHTWHITE_EX}Phone Number {Fore.YELLOW}>>{Fore.RESET} ")
		folder = f"DOX-PHONE-{Num}"
		self.create_folder(folder)
		clear()

		self.file_check(f'{folder}\\Phone-Number.txt')

		with open(folder + '\\Phone-Number.txt', 'a+') as a:
			a.writelines(f'\nhttp://www.okcaller.com/'+Num)
			a.writelines(f'\nhttps://www.facebook.com/search/top/?init=quick&q='+Num)
			a.writelines(f'\nhttp://www.france-inverse.com/annuaire-inverse/'+Num)
			a.writelines(f'\nhttps://www.whitepages.com/phone/'+Num)
			a.writelines(f'\nhttps://www.anywho.com/phone/'+Num)
			a.writelines(f'\nhttps://www.pagesjaunes.fr/annuaireinverse/recherche?quoiqui='+Num)
			a.writelines(f'\nhttp://canada411.pagesjaunes.ca/fs/'+Num)
		
		a.close()
		print(f"{Fore.YELLOW}Info written to {Fore.LIGHTGREEN_EX}{folder}/Phone-Number.txt")
		sleep(3)
		self.menu()

	def DEAD(self):
		setTitle("Doxer | Tab: [Dead]")
		clear()
		First_name 	= input(f"{Fore.LIGHTWHITE_EX}First Name {Fore.YELLOW}>>{Fore.RESET} ")
		Last_name 	= input(f"{Fore.LIGHTWHITE_EX}Last Name {Fore.YELLOW}>>{Fore.RESET} ")
		folder = f"DOX-DEAD-{First_name}-{Last_name}"
		self.create_folder(folder)
		clear()

		self.file_check(f'{folder}\\Dead.txt')

		with open(folder + '\\Dead.txt', 'a+') as p:
			p.writelines(f'\nhttp://www.libramemoria.com/avis/?Nom='+Last_name+'&Prenom='+First_name)
			p.writelines(f'\nhttps://www.avis-de-deces.net/avis/par-nom/?lastname='+Last_name+'&firstname='+First_name)
			p.writelines(f'\nhttp://enmemoria.lavanguardia.com/buscar?keywords='+Last_name+'+'+First_name+'&type=death&_fstatus=search') 

		p.close()
		print(f"{Fore.YELLOW}Info written to {Fore.LIGHTGREEN_EX}{folder}/Dead.txt")
		sleep(3)
		self.menu()

	def IP(self):
		setTitle("Doxer | Tab: [IP]")
		clear()
		ip = input(f"{Fore.LIGHTWHITE_EX}IP Address {Fore.YELLOW}>>{Fore.RESET} ")
		folder = f"DOX-IP-{ip}"
		self.create_folder(folder)
		clear()

		self.file_check(f'{folder}\\IP.txt')

		with open(folder + '\\IP.txt', 'a+') as t:
			t.writelines(f'\nhttps://www.g-force.ca/en/hosting/ip-whois?ip='+ip)
			t.writelines(f'\nhttp://whatismyipaddress.com/ip/'+ip)
			t.writelines(f'\nhttps://dig.whois.com.au/ip/'+ip)

		t.close()
		print(f"{Fore.YELLOW}Info written to {Fore.LIGHTGREEN_EX}{folder}/IP.txt")
		sleep(3)
		self.menu()

	def EXITMENU(self):
		setTitle("U will be missed!")
		clear()
		print (f"{Fore.LIGHTRED_EX}Exiting. . .{Fore.RESET}")
		sleep(2)
		os._exit(1)


if __name__ == '__main__':
	# Start the program
	doxer = Doxer()
	doxer.init()
