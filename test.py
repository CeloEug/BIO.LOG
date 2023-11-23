from database import c

animal = c.execute("SELECT * FROM lifeForm")

## index             [0]
## domain TEXT       [1]
## kingdom TEXT      [2] 
## family TEXT       [3]
## species TEXT      [4] 
## description TEXT  [5]
## image TEXT        [6]

i = 0
for anim in animal: 
    i += 1
    print(
    str(i) + '\t' + (str(anim[0]) if anim[0] is not None else "Nothing") + " " + '\t' +
    (str(anim[1]) if anim[1] is not None else 'Nothing') + " " + '\t' +
    (str(anim[2]) if anim[2] is not None else 'Nothing') + " " + '\t' +
    (str(anim[3]) if anim[3] is not None else 'Nothing') + " " + '\t' +
    (str(anim[5]) if anim[5] is not None else 'Nothing') + " " + '\t'
    )
    
