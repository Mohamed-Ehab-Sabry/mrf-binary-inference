# Markov Random Field (Triangle Network)

This repository contains a pure Python, from-scratch implementation of a Markov Random Field (MRF) forming a triangle network with three binary variables ($A, B, C \in \{0,1\}$). 

This project was built to demonstrate exact inference, partition function calculation, and marginalization without relying on external probability libraries.

## ⚠️ Implementation Restrictions
This implementation strictly adheres to the following assignment rules:
- **No Built-in Shortcuts:** No external functions are used for probability calculations, normalization, marginalization, or predefined combinatorics.
- **No Hardcoding:** All joint probability tables and final probability values are computed dynamically from the factor functions.
- **No Plagiarism:** Written completely from scratch without copy-pasting from external sources or AI bots.

## 🕸️ Network Structure
The network has a circular structure with three edges forming the maximal cliques $\{A, B\}$, $\{B, C\}$, and $\{C, A\}$.

The clique potentials (factors) are defined as follows:
- $\phi_1(A, B)$ = 4 if $A = B$, and 2 if $A \neq B$
- $\phi_2(B, C)$ = 5 if $B = C$, and 1 if $B \neq C$
- $\phi_3(C, A)$ = 3 if $C = A$, and 1 if $C \neq A$

## 📋 Tasks Implemented
1. **Factor Functions:** Explicit implementation of $\phi_1$, $\phi_2$, and $\phi_3$.
2. **Unnormalized Joint Distribution:** Generation of all combinations of $(A, B, C)$ and calculation of unnormalized probabilities using factor multiplication.
3. **Partition Function ($Z$):** Computation of the partition function by summing the unnormalized distribution.
4. **Normalization:** Calculation of the normalized probability table.
5. **General Probability Query:** A function to query the specific probability of any $(A, B, C)$ configuration.
6. **Marginal Probability:** A function to compute the marginal probability of any single variable state (e.g., $P(A=1)$ or $P(C=0)$).

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Mohamed-Ehab-Sabry/mrf-triangle-network.git
   cd mrf-triangle-network
   ```
2. Run the main script (assuming your code is in `main.py`):
   ```bash
   python main.py
   ```

## 👥 Contributors
- [Mohamed Ehab Sabry](https://github.com/Mohamed-Ehab-Sabry)
- [Ayman Ahmed](https://github.com/Ayman-Abd-Elsamie)
- [Mai Elsehet](https://github.com/maielsehet)
- [Mariam Badr](https://github.com/Mariam-Badr-MB)
- [Youssef Amgad Elkhatib](https://github.com/Youssef-Amgad-Elkhatib)
- [Youssef Naggar](https://github.com/Youssef-Naggar)
