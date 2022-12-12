from tkinter import *
import time
import socket 
from _thread import *
import threading 

print_lock = threading.Lock() 



class Window(Frame):
	def connect(self):
		host = self.ip_box.get()
		port = int(self.port_box.get())

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.c = self.s
		self.s.connect((host, port))
		


		self.Main()

		 


	def __init__(self, master=None):
		Frame.__init__(self, master, bg='red' )        
		self.master = master
		
		self.log = Label(self.master,text="LOG",justify=LEFT)
		self.log.config(bg='green')
		self.log.pack()
		# widget can take all window
		self.pack(fill=BOTH)
		
		self.chat = []
		self.chatlabel = []
		
		############################################################
		menu = Menu(self.master)
		self.master.config(menu=menu)
		
		
		
		fileMenu = Menu(menu)
		fileMenu.add_command(label="Item")
		fileMenu.add_command(label="Exit", command=self.exitProgram)
		menu.add_cascade(label="File", menu=fileMenu)

		editMenu = Menu(menu)
		editMenu.add_command(label="Undo")
		editMenu.add_command(label="Redo")
		menu.add_cascade(label="Edit", menu=editMenu)
		
		##########################################################
		connections = Frame(self.master)
		
		ip_box_label= Label(connections,text="IP",justify=LEFT)
		ip_box_label.pack(side=LEFT)
		self.ip_box= Entry(connections, bd=2)
		self.ip_box.pack(side=LEFT)

		port_box_label= Label(connections,text="PORT",justify=LEFT)
		port_box_label.pack(side=LEFT)
		self.port_box= Entry(connections, bd=2)
		self.port_box.pack(side=LEFT)
		
		
		# create button, link it to clickExitButton()
		
		connect = Button(connections, text="Connect",command=self.connect)
		connect.pack(side=TOP)
		# place button at (0,0)
		
		connections.pack(padx=30,pady=30)
		###############################################################
		
		self.messages = Frame(self.master, bg='blue')
		self.messages.pack(fill=BOTH, expand=1)
		###############################################################
		self.composeMsg = Frame(self.master)
		
		
		self.msg_box= Entry(self.composeMsg, bd=2)
		self.msg_box.pack(side=LEFT, fill=X)

		
		self.send = Button(self.composeMsg, text="Send",command=self.sendMsg)
		self.send.pack(side=LEFT)
		
		
		self.composeMsg.pack(padx=30,pady=30)
		
		################################################################
	def sendMsg(self):
		content = self.msg_box.get()
		if not content:
				return
		
		
		self.chat.append({'sender':'Client', 'content':content})
		
		self.msg_box.delete(0,END)
		self.msg_box.insert(0,"")
		#self.chat.append({'sender':'client', 'content':"you : clientttttttttttttt"})

		#data = self.msg_box.get()
		#self.chat.append({'sender': 'server', 'content': data})

		self.c.send(str.encode(content))
		
		
	def addMessage(self,message):
		
		newMsg= Label(self.messages,text=message['sender']+ " : " + message['content'],justify=LEFT)
		
		return newMsg
	   
	def exitProgram(self):
		exit()
		
	def updateInfo(self):
		
		
		while self.chat:
				i = self.chat.pop(0)
				if i['sender'] == 'Client':
						color = 'yellow'
				else: 
						color = 'orange'
	
				a = self.addMessage(i)
				a.config(bg=color)
				a.pack(fill = X)
		
		
		
		self.after(1000, self.updateInfo)


	def threadedRecv(self):
		while True: 
			
			# data received from client 
			data = self.c.recv(1024)
			if data:
					print("\r\033[32mClient : "+data.decode()+"\033[34m\nYou : ", end="")
					#self.addMessage({'sender':'client','content':data.decode() })
					self.chat.append({'sender':'Server', 'content':data.decode()})

		# connection closed 
		c.close() 
	def threadedSend(self):
		while True: 
			
			print("\033[34mYou : ", end="")
			
			data = self.msg_box.get()

			self.c.send(str.encode(data))

		# connection closed 
		c.close() 


	def Main(self):
		
		
		start_new_thread(self.threadedRecv, ())
		#start_new_thread(self.threadedSend, ())
		#time.sleep(100000) 


if __name__ == '__main__': 
		root = Tk()
		app = Window(root)
		root.wm_title("Chat Application : Client")
		root.geometry("420x400")
		root.after(1000, app.updateInfo)

		#app.Main()


		root.mainloop()












