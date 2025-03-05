class Dream:
    def __init__(self, dreamer:str, participants:set[str], parent:"Dream"=None):
        self.dreamer = dreamer
        self.participants = participants
        self.parent = parent
        self.isLost = False

def reality_check(events: list[str], person:str) -> str:
    inReality = set(nameLst)
    dreamDict:dict[list[str], Dream|None] = dict.fromkeys(nameLst, None)
    for event in events:
        sentence = event.replace(',', ' ').split()

        if "started" in sentence:
            dreamer = sentence[0]
            participants = {name for name in nameLst if name in sentence}

            if dreamDict[dreamer]:
                if not participants.issubset(dreamDict[dreamer].participants):
                    return "Invalid Input."
            else:
                if not participants.issubset(inReality):
                    return "Invalid Input."
                else:
                    inReality.difference_update(participants)

            for p in participants:
                dreamDict[p] = Dream(dreamer, participants, dreamDict[p])

        elif "kick" in sentence:
            lostInLimbo = set()

            # First assume that all are lost in limbo
            for name in nameLst:
                if name in sentence:
                    if dreamDict[name] is None:
                        return "Invalid Input."
                    lostInLimbo.update(dreamDict[name].participants)

            # Then rescure those who got the kick
            for name in nameLst:
                if name in sentence:
                    lostInLimbo.discard(name)
                    dreamDict[name] = dreamDict[name].parent
            
            # The ones who are remaining in lostInLimbo set actually got lost
            for name in lostInLimbo:
                dreamDict[name].isLost = True
                nameLst.remove(name)

            # Check if someone got back to reality
            for name in nameLst:
                if name in sentence and dreamDict[name] is None:
                    inReality.add(name)
    
    if dreamDict[person] is None:
        return person + " is in Reality."
    elif dreamDict[person].isLost:
        return person + " got lost in Limbo."
    else:
        return person + " is Dreaming..."

nameLst = ["Cobb", "Arthur", "Ariadne", "Eames"]

if __name__ == "__main__":
    N = int(input()) # Number of events
    events = [input() for _ in range(N)]
    person = input()
    print(reality_check(events, person))