<p align='center'><img src="img/GausQash.png" width="250"></p>

# GausQash
## Quantum Key Derivation/Hashing Circuit (Gaussian Photonic Operations)
- this is a strawberryfields adaptation of the [qash-qkdc](https://github.com/TimeMelt/qash-qkdc) hash circuit
- this notebook uses gaussian/photonic QPU operations to conduct hashes
- this circuit only works with gaussian backends (fock only simulators/devices not compatible)

#### *Security Note*: this circuit is not officially battle tested in any capacity and therefore unverified to be cryptographically secure, or programmatically useful in any manner
- If anyone wants to benchmark and/or pentest these circuits feel free to do so
- any feedback related to improving these circuits security and/or usability is highly appreciated

#### Donations (optional):
- Any donation, no matter how small, is greatly appreciated!! 
- [click here to donate](https://buy.stripe.com/fZe4i46ht5mEfMkeUY)

#### Citation (this project):
- please cite this project/repo if using it in research and/or development (USE IN RESEARCH/DEVELOPMENT IS ENCOURAGED)

#### Credits:
- hash circuit based on [qash-qkdc](https://github.com/TimeMelt/qash-qkdc) 
- quantum libraries provided by [StrawberryFields](https://github.com/XanaduAI/strawberryfields): 
    > Nathan Killoran, Josh Izaac, Nicolás Quesada, Ville Bergholm, Matthew Amy, and
    > Christian Weedbrook. "Strawberry Fields: A Software Platform for Photonic Quantum Computing",
    > [Quantum, 3, 129](https://quantum-journal.org/papers/q-2019-03-11-129/) (2019).

    > Thomas R. Bromley, Juan Miguel Arrazola, Soran Jahangiri, Josh Izaac, Nicolás Quesada,
    > Alain Delgado Gran, Maria Schuld, Jeremy Swinarton, Zeid Zabaneh, and Nathan Killoran.
    > "Applications of Near-Term Photonic Quantum Computers: Software and Algorithms",
    > [Quantum Sci. Technol. 5 034010](https://iopscience.iop.org/article/10.1088/2058-9565/ab8504/meta) (2020).