#so.

#how about
# i do this with geom and unoccupied spaces.
#like


from geom import geom

def main():

    l=[]
    new_elements=[]
    blockers=[]
    for element in l:
        #make a decision
        #about placing or not placing something
        #with chance based patterns it should be fine.
        #to just keep going.

        #pick what to place
        p=patternfit(element)
        #pick a location on the element
        #maybe interpolate and pick a position

        #so then, i should remove the old element
        #and replace with new elements.

        #for detecting patterns
        #i need to attach things somehwere.

        #could be just a dict pointing to attached objects

if __name__=="__main__":
    main()
