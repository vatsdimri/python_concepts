import copy

original = [[1, 2], [3, 4]]
new = original # only the reference to the original object is copied. No new object is created

new[0][0] = 10
print("If we modify the Inner objects:                    ")
print(f"original: {original}")
print(f"new: {new}")


new[0] = [2, 3, 4]
print("If we modify the Outer objects:                    ")
print(f"original: {original}")
print(f"new: {new}")


############# Shallow Copy ###############
shallow = copy.copy(original)

# if we modify the nested list in the shallow copy
print("If we modify the Inner objects:                    ")
shallow[0][0] = 6
print(f"original: {original}")
print(f"shallow: {shallow}")

# if we modify the outer object, the the change is not reflected in the original
print("If we modify the Outer objects:                    ")
shallow[0] = [4,5,6]
print(f"original: {original}")
print(f"shallow: {shallow}")


############# Deep Copy ###############

deep = copy.deepcopy(original)
print(f"deep: {deep}")
deep[0][0] = 1
print(f"original: {original}")
print(f"deep: {deep}")
