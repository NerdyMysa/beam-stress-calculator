def bending_moment( force,length):
    return (force*length)/4 

def second_moment_of_area(width,height):
    return (width*height**3)/12 

def bending_stress(moment, width, height):
    I = second_moment_of_area(width, height)  
    return moment * (height / 2) / I

def safety_factor(yield_stress, stress): 
    return yield_stress / stress


def analyze_beam(force, length, width, height, yield_stress):
    M = bending_moment(force, length)
    stress = bending_stress(M, width,height)
    SF = safety_factor(yield_stress, stress)

    return {
        "moment": M,
        "stress": stress,
        "safety_factor": SF
    }
