from tkinter import *



root=Tk()

root.config(background="orange")



startMenuLabel = Label(root,text="LocoMotive", fg = "black", bg =  "orange",font = "Helvetica 30 bold italic")
startMenuLabel.place(relx=.5, rely=.1, anchor="c")


startGame = Button(root,text="Start game",fg="black",bg ='#ff0000',font="Helvetica 15 bold",width=25,height=4,command=())
startGame.place(relx=.5, rely=.85, anchor="c")
startGame.config(highlightbackground='#e60000',background='#e60000')

rules = Button(root,text="Rules",fg="black",bg = "dark red",font="Helvetica 15 bold",width=15,height=3,command=())
rules.place(relx=.8, rely=.33, anchor="c")
rules.config(highlightbackground="green",background="green")

savedGames = Button(root,text="Saved games",fg="black",bg = "dark red",font="Helvetica 15 bold",width=15,height=3,command=())
savedGames.place(relx=.8, rely=.51, anchor="c")
savedGames.config(highlightbackground="green",background="green")

noOfPlayersLabel= Label(root,text = "Number of players:",bg="orange",font = "Helvetica 15 bold")
noOfPlayersLabel.place(relx=.1,rely=.3)


noOfPlayers = Entry(root,width = 1)
noOfPlayers.place(relx=.29,rely=.3)


noOfCPUPlayersLabel= Label(root,text = "Number of Comp players:",bg="orange",font = "Helvetica 15 bold")
noOfCPUPlayersLabel.place(relx=.1,rely=.5)


noOfCPUPlayers = Entry(root,width = 1)
noOfCPUPlayers.place(relx=.345,rely=.5)



root.geometry("800x600+250+250")
root.mainloop()