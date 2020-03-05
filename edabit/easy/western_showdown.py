"""
Wild Roger is participating in a Western Showdown, meaning he has to draw (pull
out and shoot) his gun faster than his opponent in a gun standoff.

Given two strings,"p1" and "p2", return _which_ person drew their gun the
fastest. If both are drawn at the same time, return "tie".

Examples:
(a) 
showdown(
  "   Bang!        ",
  "        Bang!   "
) ➞ "p1"

 # p1 draws his gun sooner than p2
 
(b) 
showdown(
  "               Bang! ",
  "             Bang!   "
) ➞ "p2"

(c)
showdown(
  "     Bang!   ",
  "     Bang!   "
) ➞ "tie"

NOTES:
Both strings are the same length.
"""