import numpy as np

width = 4
height = 3

max_iterations = 100
epsilon = 0.01

rw = np.full((12, ), -0.4)
rw[4] = -0.5
# rw[9] = 0.2
rw[10] = -1.0
rw[11] = 1.0

T_up = np.zeros((12, 12))
T_down = np.zeros((12, 12))
T_left = np.zeros((12, 12))
T_right = np.zeros((12, 12))

# T_UP
T_up[0,1] = 0.8
T_up[0,3] = 0.1
T_up[0,0] = 0.1

T_up[1,2] = 0.8
T_up[1,1] = 0.1
T_up[1,4] = 0.1

T_up[2,2] = 0.9
T_up[2,5] = 0.1

T_up[3,4] = 0.8
T_up[3,6] = 0.1
T_up[3,0] = 0.1 

T_up[4,5] = 0.8
T_up[4,1] = 0.1
T_up[4,7] = 0.1 

T_up[5,5] = 0.8
T_up[5,8] = 0.1
T_up[5,2] = 0.1 

T_up[6,7] = 0.8 
T_up[6,9] = 0.1
T_up[6,3] = 0.1 

T_up[7,8] = 0.8 
T_up[7,10] = 0.1
T_up[7,4] = 0.1 

T_up[8,8] = 0.8 
T_up[8,11] = 0.1
T_up[8,5] = 0.1 

T_up[9,10] = 0.8
T_up[9,9] = 0.1
T_up[9,6] = 0.1

# T_DOWN
T_down[0,0] = 0.9 
T_down[0,3] = 0.1 

T_down[1,0] = 0.8 
T_down[1,1] = 0.1 
T_down[1,4] = 0.1 

T_down[2,1] = 0.8 
T_down[2,2] = 0.1 
T_down[2,5] = 0.1 

T_down[3,3] = 0.8 
T_down[3,0] = 0.1 
T_down[3,6] = 0.1 

T_down[4,3] = 0.8
T_down[4,1] = 0.1 
T_down[4,7] = 0.1 

T_down[5,4] = 0.8 
T_down[5,2] = 0.1 
T_down[5,8] = 0.1 

T_down[6,6] = 0.8 
T_down[6,3] = 0.1
T_down[6,9] = 0.1

T_down[7,6] = 0.8
T_down[7,4] = 0.1
T_down[7,10] = 0.1

T_down[8,7] = 0.8
T_down[8,5] = 0.1
T_down[8,11] = 0.1

T_down[9,9] = 0.9
T_down[9,6] = 0.1

# T_LEFT
T_left[0,0] = 0.9
T_left[0,1] = 0.1

T_left[1,0] = 0.1
T_left[1,2] = 0.1
T_left[1,1] = 0.8

T_left[2,2] = 0.9
T_left[2,1] = 0.1

T_left[3,0] = 0.8
T_left[3,3] = 0.1
T_left[3,4] = 0.1

T_left[4,1] = 0.8
T_left[4,3] = 0.1
T_left[4,5] = 0.1

T_left[5,2] = 0.8
T_left[5,4] = 0.1
T_left[5,5] = 0.1

T_left[6,3] = 0.8
T_left[6,6] = 0.1
T_left[6,7] = 0.1

T_left[7,4] = 0.8
T_left[7,6] = 0.1
T_left[7,8] = 0.1

T_left[8,5] = 0.8
T_left[8,8] = 0.1
T_left[8,7] = 0.1

T_left[9,6] = 0.8
T_left[9,9] = 0.1
T_left[9,10] = 0.1

# T_RIGHT
T_right[0,3] = 0.8
T_right[0,0] = 0.1
T_right[0,1] = 0.1

T_right[1,4] = 0.8
T_right[1,0] = 0.1
T_right[1,2] = 0.1

T_right[2,5] = 0.8
T_right[2,2] = 0.1
T_right[2,1] = 0.1

T_right[3,6] = 0.8
T_right[3,3] = 0.1
T_right[3,4] = 0.1

T_right[4,7] = 0.8
T_right[4,3] = 0.1
T_right[4,5] = 0.1

T_right[5,8] = 0.8
T_right[5,5] = 0.1
T_right[5,4] = 0.1

T_right[6,9] = 0.8
T_right[6,6] = 0.1
T_right[6,7] = 0.1

T_right[7,10] = 0.8
T_right[7,6] = 0.1
T_right[7,8] = 0.1

T_right[8,11] = 0.8
T_right[8,7] = 0.1
T_right[8,8] = 0.1

T_right[9,9] = 0.9
T_right[9,10] = 0.1


def update_value(T_up,T_down,T_right,T_left,rw,value, i):
    value_aux = np.zeros(12)
    
    for s in range(12):

        v_up = T_up[s,] * value.transpose()
        v_down = T_down[s,] * value.transpose()
        v_left = T_left[s,] * value.transpose()
        v_right = T_right[s,] * value.transpose()

        value_aux[s] = rw[s] + np.max((np.sum(v_up),np.sum(v_down),np.sum(v_left),np.sum(v_right)))

    value = value_aux

    aux = np.zeros((3, 4))
    aux[0,] = np.array((value[2],value[5],value[8],value[11]))
    aux[1,] = np.array((value[1],value[4],value[7],value[10]))
    aux[2,] = np.array((value[0],value[3],value[6],value[9]))
    
    np.set_printoptions(precision=3)
    print("Iteration: ", i)
    print(aux, "\n")
    return value_aux
    
def return_policy(T_up,T_down,T_right,T_left,value):   
    policy = []

    # obs.: somente 9 estados porque n�o ha a��o aplicada nos dois estados terminais
    for s in range(10):
        v_up = T_up[s,] * value.transpose()   
        v_down = T_down[s,] * value.transpose()
        v_left = T_left[s,] * value.transpose()
        v_right = T_right[s,] * value.transpose()
        
        policy.append(np.argmax(np.array((np.sum(v_up),np.sum(v_down),np.sum(v_left),np.sum(v_right)))))
    
    actions = ["UP","DW","LF","RG"]

    s1 = [actions[policy[2]],actions[policy[5]],actions[policy[8]],"+1"]
    s2 = [actions[policy[1]],actions[policy[4]],actions[policy[7]],"-1"]
    s3 = [actions[policy[0]],actions[policy[3]],actions[policy[6]],actions[policy[9]]]

    print("\n",s1,"\n",s2,"\n",s3, "\n")



    return(policy)
 

if __name__ == "__main__":
    value = np.zeros(12)

    for i in range(max_iterations):
        old_value = value
        value = update_value(T_up, T_down, T_right, T_left, rw, value, i)
        diff = np.sum(value - old_value)
        if abs(diff) < epsilon:
            print("Converged!")
            break


    policy = return_policy(T_up,T_down,T_right,T_left,value)
 