import pytest
import numpy as np
file_name = "/home/student/cs2300/cs4300/hw1/de.txt"

#indentity matrix
id_mat = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1]
])

mat_D = []
mat_E = []

#creating the inverse of the matix
def create_Inv(id_mat, mat_D):
    mat = np.subtract(id_mat, mat_D)
    invmat = np.linalg.inv(mat)
    return invmat

#calculating the final matrix
def calc_fin(mat_inv, mat_E):
    mat = np.multiply(mat_D,mat_E)
    return mat

with open(file_name, 'r') as file:
    all = file.readlines()
    g = 0
    for line in all:
        if g < 3:
            nums = list(map(float, line.split()))
            mat_D.append(nums)
            g += 1
        else:
            nums = list(map(float, list(line.split())))
            mat_E.append(nums)

mat_inv = create_Inv(id_mat,mat_D)
fin = calc_fin(mat_inv,mat_E)
sol = np.matrix.round(fin)

for row in sol:
    print(row)

def test_mat():
    assert sol.any() == np.array([
        [400,500,500],
        [300,0,300],
        [200,200,0]
        ]).any()