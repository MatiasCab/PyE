def prob_A(A, o):
    prob_A = A/o
    return prob_A

# A = {1, 2, 3} o = {1, 2, 3, 4, 5, 6}
#Par
if __name__ == "__main__":
    A = 3
    o = 6
    
    print(f"Y este sera nuestro resultado: {prob_A(A, o)}")
    
# A = {1, 2, 3} o = {1, 2, 3, 4, 5, 6}
#Impar
if __name__ == "__main__":
    A = 3
    o = 6
    
    print(f"Y este sera nuestro resultado: {prob_A(A, o)}")

#Impar menor o igual a 3
# b = {1, 3} h = {1, 2, 3}
if __name__ == "__main__":
    b = 2
    h = 3
    
    print(f"Y este sera nuestro resultado: {prob_A(b, h)}")
    


#Impar menor o igual a 3 dado t
# t = {1, 3, 5} j = {1, 2, 3}
def prob_A_dado_B (prob_B, prob_A_y_B):
    prob_A_dado_B = prob_A_y_B/prob_B
    return prob_A_dado_B

if __name__ == "__main__":
    prob_A_y_B = 2
    prob_B = 3
    
    print(f"Y este sera nuestro resultado: {prob_A_dado_B(prob_B,  prob_A_y_B)}")


# Su primero es una niña y el segundo tiene que ser niña
# B = {(m, m), (m, h)} A = {(m, m)}
def prob_A_dado_B (prob_B, prob_A_y_B):
    prob_A_dado_B = prob_A_y_B/prob_B
    return prob_A_dado_B

if __name__ == "__main__":
    prob_A_y_B = 1
    prob_B = 2
    
    print(f"Y este sera nuestro resultado: {prob_A_dado_B(prob_B,  prob_A_y_B)}")
    
    
# SAlguno tiene que ser niña y el otro tambien 
# B = {(m, m), (m, h), (h, m)} A = {(m, m)}
def prob_A_dado_B (prob_B, prob_A_y_B):
    prob_A_dado_B = prob_A_y_B/prob_B
    return prob_A_dado_B

if __name__ == "__main__":
    prob_A_y_B = 1
    prob_B = 3
    
    print(f"Y este sera nuestro resultado: {prob_A_dado_B(prob_B,  prob_A_y_B)}")