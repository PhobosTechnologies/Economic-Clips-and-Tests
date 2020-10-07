end_of_game = False

# how can we make something that would dynamically fill its own maps?

while not end_of_game:
    game_grid = [
                    [
                        [0],
                        [2],
                        [3],
                        [4],
                        [5]
                    ], [
                        [],
                        [],
                        [],
                        [],
                        []
                    ], [
                        [],
                        [],
                        [],
                        [],
                        []
                    ], [
                        [],
                        [],
                        [],
                        [],
                        []
                    ]
                ]










#     In Python, a list is a dynamic array.You can create one like this:
# lst = []  # Declares an empty list named lst

#     Or you can fill it with items:
# lst = [1, 2, 3]

#     You can add items using "append":
# lst.append('a')

# for item in lst:
    #do stuff with it here

# for idx, item in enumerate(lst):
    #idx is the current idx, while item is lst[idx]

# del lst[0] # delete first item
# lst.remove(x) #remove the first occurance of x in the list

# for item in lst[:]: #notice the [:] which makes a slice
    #now we can modify lst, since we are iterating over a copy of it