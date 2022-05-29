from collections import deque

graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom mango seller", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["tom mango seller"] = []
graph["jonny"] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if "mango seller" in person:
                return person
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

print(search("you")) # => tom mango seller

