#This is the equation for workable and billable hours
#3 classifcation setup 
office = ["Lori", "Nora", "Norman", "Covita"]
nonoffice =["William", "Paul"] #if non worker 90% is tier 2Supplementary Activites and 10% Active
nonofficerate1 = (.90 *hours)#this is the middle tier
nonofficerate2 = (.1 * hours) #this is the top tier

total = hours * rate 

def formula(hours, rate, class_):
    amount = hours * rate * class_

