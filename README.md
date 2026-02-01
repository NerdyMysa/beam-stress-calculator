Beam Stress Calculator

A simple Python project to analyze a simply supported beam with a central point load.  
This project applies classical beam theory to compute bending moment, stress, and safety factor.

Objective

This project calculates:

- Maximum bending moment  
- Maximum bending stress  
- Safety factor  

for a simply supported beam subjected to a central point load.

It is designed as a learning and demonstration project in both:
- structural mechanics (beam theory) 
- software engineering (modular code, testing, and GitHub workflow).

 Project Structure


- `src/beam.py` → Core calculation module  
- `test_run.py` → Interactive script to run the analysis   
- `requirements.txt` → Required Python packages  
- `.gitignore` → Files excluded from GitHub  

[ Installation : in order to use the program from your device

Clone the repository:

type in bash 
$ git clone https://github.com/your-username/beam-stress-calculator.git
$ cd beam-stress-calculator
$ pip install -r requirements.txt ]

To run the program, type in bash
$ winpty python test_run.py

In this project, we consider the hypothesis that we are working with small deformations so the theories used 
are only applicable in this context 

Bending moment :M = F * L / 4
Second Moment of area: I = b * h³ / 12
Bending stress :σ = M * y / I   with y = h/2
Security Factor:SF = σ_yield / σ


Lisa-Michèle KEMMEGNE
