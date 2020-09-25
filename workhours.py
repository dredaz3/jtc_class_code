#This is the equation for workable and billable hours
#3 classifcation setup 
office = ["Lori", "Nora", "Norman", "Covita"]
nonoffice =["William", "Paul"] #if non worker 90% is tier 2Supplementary Activites and 10% Active
nonofficerate1 = (.90 *hours)#this is the middle tier
nonofficerate2 = (.1 * hours) #this is the top tier

hours_q1 = [335.5, 3.5, 249.5, 61.5, 502.5]
hours_q2 = [303.75, 32.5, 221.5, 372.5]
hours_q3 = [269, 233, 148]
hours_q4 = [120.5, 43, 61, 121]

rate = 11, 12, 12, 12, 14, 19

total = hours * rate 

def formula(hours, rate, name):
    amount = (hours * rate) 
    newamount_9 = (amount) * .9
    newamount_1 =(amount) * .1
    return amount, newamount_1, newamount_9, rate, name, 

formula(335, 19, "Lori")
#sample Q1
hours_q1[:3]