# vectors
# vectors are points in some finite
# dimension space
# height inch , weight pund , age years
import math

height_weight_age = [70, 170, 40]
# exam one , exam two , exam three  , etc ..
grades = [95, 80, 75, 62]


def sum_vectors():
    v1 = [1, 2, 3]
    v2 = [6, 7, 5]
    v3 = [v_i + w_i for v_i, w_i in zip(v1, v2)]
    print("in", v1, "+", v2)
    print("out", v3)


def multiply_vector_by_scaler():
    v1 = [1, 2, 3]
    sc = 10
    res = [x * sc for x in v1]
    print("in", v1, "*", sc)
    print("out", res)


def vector_mean():
    v1 = [2, 7, 13]
    n = len(v1)
    sum_ = sum(a for a in v1)
    print("in", v1)
    print("sum", sum_)
    print("mean", sum_ / n)


# dot product of vecs
# is for v1
#
def vector_dot_proudct():
    v1 = [1, 2, 3]
    v2 = [6, 7, 5]
    dot = sum(v1_i * v2_i for v1_i, v2_i in zip(v1, v2))
    print("in", v1, " dot ", v2)
    print("out dot proudct", dot)


# magnitude of the vector is  length of the vector
def vector_magnitude():
    v1 = [1, 2, 3]
    dot = sum(v1_i * v2_i for v1_i, v2_i in zip(v1, v1))
    magnitude = math.sqrt(dot)
    print("in vec", v1)
    print("out magnitude: ", magnitude)


# distance btw two vectors

def squared_distance():
    v1 = [1, 2, 3]
    v2 = [6, 7, 5]
    suptract_to_victors = [v1_i - v2_i for v1_i, v2_i in zip(v1, v2)]
    squard_distance = sum(v1_i * v2_i for v1_i, v2_i in zip(suptract_to_victors, suptract_to_victors))
    distance = math.sqrt(squard_distance)
    print("in", v1, " - ", v2)
    print("out distance btw  two vectors", distance)


# sum_vectors()
# multiply_vector_by_scaler()
# vector_mean()
# vector_dot_proudct()
# vector_magnitude()
squared_distance()
