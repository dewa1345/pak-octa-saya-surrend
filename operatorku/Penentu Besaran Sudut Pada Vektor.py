import numpy as np

def hitung_sudut_vektor(vek_A, vek_B):
    dot_product = np.dot(vek_A, vek_B)
    magnitude_vek_A = np.linalg.norm(vek_A)
    magnitude_vek_B = np.linalg.norm(vek_B)
    
    cos_theta = dot_product / (magnitude_vek_A * magnitude_vek_B)
    theta_radian = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    theta_derajat = np.degrees(theta_radian)
    
    return theta_derajat

def input_vektor():
    vektor = input("Masukkan komponen vektor (format: x,y,...): ")
    return np.array([float(x) for x in vektor.split(',')])
