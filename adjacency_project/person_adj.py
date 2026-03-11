import random
class Person:
 
    def __init__(self, first_name, last_name):
       self.first_name = first_name
       self.last_name = last_name
       self.id = random.randint(1000, 9999)
       self.friends = 0

    def __str__(self):
        return (f"{self.id}: {self.first_name} {self.last_name}, Number of friends: {self.friends}")

    def update(self):
        self.friends = self.friends + 1


def display_adj(adj_dict):
    for key, value in adj_dict.items():
        print(f"{key.id}: {key.first_name} {key.last_name}, Number of friends: {key.friends}")
        for p in value:
            print(f"{p.first_name} {p.last_name} ({p.id})")


def build_adjacency(data):
    adj_dict = dict()
    for node in data: #node = tuple of names
        a = node[0]
        b = node[1]

        if a in adj_dict:
            adj_dict[a].append(b)
        else:
            adj_dict[a] = [b]

        a.update()

        if b in adj_dict:
            adj_dict[b].append(a)
        else:
            adj_dict[b] = [a]

        b.update()

    return adj_dict
    


if __name__ == '__main__':
    p1 = Person("Anita", "Racinez")
    p2 = Person("Clem", "Jameson")
    p3 = Person("Lars", "Eriksson")
    p4 = Person("Jed", "Jones")
    data = [(p1, p2), (p2, p3), (p1, p4), (p2, p4)]
    display_adj(build_adjacency(data))
