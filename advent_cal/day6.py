######### DAY 6 ##########

#my_map = ["COM)B","B)C","C)D","D)E","E)F","B)G","G)H","D)I","E)J","J)K","K)L"]

class Node(object):
    def __init__(self, name, parent, isCOM):
        self.name = name
        self.parent = parent
        self.isCOM = isCOM
    
    def update_parent(self, parent):
        self.parent = parent

def create_orbit_mapping(my_map):
    registered_objects = {"COM": Node("COM", None, True)}

    for i in my_map:
        nodes = i.split(")")
        #split map entry to extract objects
        parent_name = nodes[0]
        child_name = nodes[1]

        #if "parent" (the node object that's being orbited around) doesn't exist, then create it but with an unknown parent
        if parent_name not in registered_objects.keys():
            registered_objects[parent_name] = Node(parent_name, None, False)
        
        #if the "child" (the orbiting object) already exists, just update its parent (the object it's orbiting around)
        #otherwise just create a new node with known parent
        if child_name in registered_objects.keys():
            registered_objects[child_name].update_parent(registered_objects[parent_name])
        else:
            registered_objects[child_name] = Node(child_name, registered_objects[parent_name], False)
    
    return registered_objects


def compute_orbits(my_map):
    number_orbits = 0

    registered_objects = create_orbit_mapping(my_map)

    for obj in registered_objects.items():
        current_node = obj[1]
        while not current_node.isCOM:
            number_orbits +=1
            current_node = current_node.parent
    return number_orbits

def compute_orbit_transfers_to_santa(my_map):
    number_transfers = 0

    registered_objects = create_orbit_mapping(my_map)
    my_orbit = registered_objects['YOU'].parent
    santas_orbit = registered_objects['SAN'].parent

    santas_ancestors = [santas_orbit.name]
    current_node = santas_orbit
    while not current_node.isCOM:
        santas_ancestors.append(current_node.parent.name)
        current_node = current_node.parent
    
    my_current_node = my_orbit
    while my_current_node.name not in santas_ancestors:
        number_transfers = number_transfers + 1
        my_current_node = my_current_node.parent
    
    number_transfers = number_transfers + santas_ancestors.index(my_current_node.name)

    return number_transfers

filename = "data/day6.txt"

if __name__ == '__main__':
    with open(filename) as f:
        my_map = f.readlines()
    my_map = [x.strip() for x in my_map] 
    
    #print(compute_orbits(my_map))
    print(compute_orbit_transfers_to_santa(my_map))