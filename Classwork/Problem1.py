# ABC company Ltd. is Interested to computerize the pay calculation
# of their employee In the form of Basic Pay, Dearness Allowance (DA) 
# and House Rent Allowance (HRA). DA and HRA certain of Basic pay(
#     For example, DA Is 80% of Basic Pay, and HRA Is 30% of Basic pay). 
# They have the deduction in the salary as PF which is 12% of Basic pay. 
# Propose a computerized solution for the above said problem.
# input : basic Pay
# Process: Calculate Salary
# (Basic Pay = (Basic Pay * 0.8) + (Basic Pay * 0.3) - (Basic Pay * 0.12))

bp = float(input("Enter the basic pay:"))
netpay = bp + (bp * 0.8) + (bp * 0.3) - (bp*0.12)
print ('Net pay:',netpay)
