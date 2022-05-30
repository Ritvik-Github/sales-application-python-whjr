from tkinter import *
root = Tk()
root.title("Sales Application")
root.geometry("700x700")
root.config(bg="yellow")
month = ("January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December")
profits = (20000, 45000, 78000, 97000, 12000, 456000,
           65000, 54000, 10000, 30000, 70000, 90000)
max_profit = max(profits)
max_profit_index = profits.index(max_profit)
max_profit_month = month[max_profit_index]
min_profit = min(profits)
min_profit_index = profits.index(min_profit)
min_profit_month = month[min_profit_index]
label_months_set = Label(root, text="Months: " +
                         str(month), fg="white", bg="darkblue")
label_profits_set = Label(
    root, text="The Profits According To The Months: " + str(profits), fg="white", bg="darkblue")
label_max_profit = Label(root)
label_min_profit = Label(root)
def show_prof():
      label_max_profit["text"] = "The maximum profit of " + str(max_profit) +" was recorded in the month of " + str(max_profit_month)
      label_min_profit["text"] = "The minimum profit of " + str(min_profit) +" was recorded in the month of " + str(min_profit_month)
btn_show = Button(root,text = "Show The Minimum And Maximum Profits Through The Months",command = show_prof)
btn_show.pack()
label_months_set.pack()
label_max_profit.pack()
label_min_profit.pack()
print(max_profit_index)
print("The maximum profit of " + str(max_profit) +
      " was recorded in the month of " + str(max_profit_month))
print(min_profit_index)
print("The minimum profit of "+str(min_profit) +
      " was recorded in the month of "+str(min_profit_month))

root.mainloop()