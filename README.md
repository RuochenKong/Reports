# Dice score

## Formula
$DICE = \frac{2\times |X\cap Y|}{|X|+|Y|}$

https://en.wikipedia.org/wiki/S%C3%B8rensen%E2%80%93Dice_coefficient

## *dice* fucntion
inputs: *s1*, *s2*
- Annotation on a single signal segment.
- For example, if (3,4) and (7,8) are selected, then *s1* = \[\[3,4],\[7,8\]\]

output: dice score
- Based on the formula above.
- In range \[0,1\]
- If both have no selected part then return 1.

implementation process:
- calculate the intersect part by *intersecseg*, stored as the same formate as annotations.
- calculate the length of *intersects*, *s1* and *s2*.
- apply to the formula.

## *intersecseg* function
inputs: *s1*, *s2*

output: 
- The intersection parts between *s1* and *s2*
- Formate as a list of lists

implementation process:
- Start at the first element of *s1* and *s2*. Assume s1\[0\] = \[l1,r1\], s2\[0\] = \[l2,r2\]
- Find the intersect part and add into the result. inter = \[l,r\] = \[max(l1,l2),min(r1,r2)\]
- If r1 < l2 then s1 move to next element. Similarly, if r2 < l1 then s2 move to next element
