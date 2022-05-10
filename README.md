# Dice score

## Formula
$DICE = \frac{|X\cap Y|}{|X|+|Y|}$

## dice fucntion
inputs: s1, s2
- Annotation on a single signal segment.
- For example, if (3,4) and (7,8) are selected, then s1 = \[\[3,4],\[7,8\]\]

output: dice score
- Based on the formula above.
- In range \[0,1\]
- If both have no selected part then return 1.
