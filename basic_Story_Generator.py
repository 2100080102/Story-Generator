import random
def generate_story():
    #story is generated on 4W's that is when, where, who, what based on that some keywords are stored in a list and using the choice the story is generated
    when=["Few years agp","Yesterday","Today"]
    where=["at Wankhede","at Lords","at Eden Gardens"]
    who=["MS Dhoni","Sachin Tendulkar","VVS Laxman"]
    what=["Scored 91 in world cup final","scored 228 runs in test match","scored 125 runs"]
    random_story=random.choice(when)+" "+random.choice(where)+" "+random.choice(who)+" "+random.choice(what)
    return random_story
print(generate_story())

