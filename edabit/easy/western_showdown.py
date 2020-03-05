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

def showdown(p1, p2):
    if len(p1) == len(p2):
        p1_draw_index = 0
        p2_draw_index = 0
        
        while p1_draw_index < len(p1):
            if p1[p1_draw_index] != " ":
                break
            else:
                p1_draw_index += 1
            
        
        while p2_draw_index < len(p2):
            if p2[p2_draw_index] != " ":
                break
            else:
                p2_draw_index += 1
                
        if p1_draw_index == p2_draw_index:
            return "tie"
        elif p1_draw_index > p2_draw_index:
            return "p2"
        else:
            return "p1"
    else:
        return "Err: Please pass in 2 arguments of equal lengths and try again"
    
print(showdown("dude ", "dude"))        # Should return "Err: Please..."
print(showdown("dude", "dude"))         # Should return "tie"
print(showdown(" dude ", "dude  "))     # Should return "p2"
print(showdown("dude  ", "  dude"))     # Should return "p1"