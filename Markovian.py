# Task 1 Clique Factors
def phi1(a,b):
    return 4 if a == b else 2

def phi2(b,c):
    return 5 if b == c else 1

def phi3(a,c):
    return 3 if a == c else 1

# Task 2 Construct the Joint Distribution
def all_comp():
    joint_prop = {}
    for i in range(2):
        for j in range(2):
            for k in range(2):
                joint_prop[i,j,k] = phi1(i, j) * phi2(j, k) * phi3(i, k)

    return joint_prop

# Task 3 Compute the Partition Function
def cal_partition(unnorm_prob):
    z = 0
    for prob in unnorm_prob.values():
        z+= prob
    return z    
    
   

# Task 4 Normalize the Distribution
def normalize():
    pass

# Task 5 Probability Query Function
def query(a,b,c):
    pass

# Task 6 compute marginal probabilities:
def marginal(variable, value):
    mar_pro = 0
    for i in [0, 1]:
        for j in [0, 1]:
            if variable == 'A':
                mar_pro += query(value, j, i)
            elif variable == 'B':
                mar_pro += query(j, value, i)
            else:
                mar_pro += query(i, j, value)
    return mar_pro

def main():
    joint_prop = all_comp()
    print(joint_prop)

if __name__ == '__main__':
    main()
