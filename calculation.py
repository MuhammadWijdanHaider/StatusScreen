HARD_LIMIT = 100
def calc(temp:dict):
    nums = []
    for i in temp:
        try:
            te = temp[i]
            ins = int(te)
            nums.append([i, ins])
        except ValueError:
            pass
    for i in len(nums):
        
        pass
    
    # for i in nums:
    #      print(i)
    


dat = {
    'Name': ' Fenris Ulvsvik', 
    'Creator': ' Momonga', 
    'Backstory': ' Created by the leader of the Supreme Beings, Momonga, from his own blood.', 
    'Race': ' Demi-Human', 
    'Racial Class(s)': ' Lycanthrope(15), Werewolf(10), Alpha Predator(5)', 
    'Available Levels': ' 0', 
    'State Points': ' 0', 
    'Level': ' 100', 
    'Sense of Justice': ' -500(Extreme Evil)', 
    'HP': ' 65', 
    'MP': ' 90', 
    'Physical Attack': ' 89', 
    'Physical Defence': ' 70', 
    'Agility': ' 89', 
    'Magic Attack': ' 89', 
    'Magic Defence': ' 70', 
    'Resist': ' 75', 
    'Special': ' 100', 
    'Job Class(s)': 'Cleric(10), Battle Cleric(5), Fallen Cleric(10), Fallen Priestess(10), Cursed Priestess(5), Arch Commander(5), Field Marshal(5), Warlord(5), Architect of War(5), Lunar Mage(5), Vile Caster(5)', 
    'Flavor Text': " She likes to keep to herself. The people she considers family are; her creator and master, Lord Momonga, her sister, Shalltear Bloodfallen, and her siblings. She will go to any lengths for her family. She is deeply in love with her creator and will do anything he asks her to do. She doesn't mind sharing her creator with others. She has good relations with her fellow NPCs. She doesn't mind working with those from the outside world...."}

calc(dat)



