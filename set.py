#set=collection which is unordered,unindexed. No duplicate values

utensils={"fork","spoon","knife"}
dishes={"bowl","plate","cup","knife"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
dishes.update(utensils)#adds all the elements of dishes to utensils
dinner_table=utensils.union(dishes)

print(dishes.difference(utensils))
print(utensils.intersection(dishes))