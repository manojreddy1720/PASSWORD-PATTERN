# TASK-03: Advanced Password Pattern Validation via PDA & CFG

**Course:** 21CSC301T – Formal Language and Automata  
**Assessment:** CLA-2 Assessment Task 3  
**Author:** C. Manoj Reddy (RA2411026050038)  
**Institution:** SRM Institute of Science and Technology, Tiruchirappalli  

---

## Overview

This repository implements a formal **Password Pattern Validator** utilizing Pushdown Automata (PDA) and Context-Free Grammars (CFG):
1. **Hierarchical Passphrase Delimiter DPDA:** Verifies multi-tier structural wrapper brackets (`()`, `[]`, `{}`) using a 3-state Deterministic Pushdown Automaton with LIFO stack memory.
2. **Anti-Mirroring Palindrome Evaluator:** Rejects weak mirrored passphrases ($w c w^R$ via DPDA and $w w^R$ via NPDA) to thwart automated reverse-dictionary attacks.
3. **Stratified Grammar Parsing:** Context-free grammar models for structured multi-token passphrases with ambiguity elimination.

```bash
# Run unit tests
python3 test_task3.py
```
