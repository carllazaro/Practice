# Print a downward half-pyramid pattern of stars

# * * * * *  
# * * * *  
# * * *  
# * *  
# *

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print("*", end  = " ")
    print()