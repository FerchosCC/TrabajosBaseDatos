#count
versiones_plone = [2.1,2.5,3.6,4,5,6]
print("6 ->",versiones_plone.count(6))
print("5 ->",versiones_plone.count(5))
print("2.5 ->",versiones_plone.count(2.5),"\n")

#extend
versiones_plone = [2.1,2.5,3.6]
print(versiones_plone)
versiones_plone.extend([4])
print(versiones_plone)
versiones_plone.extend(range(5,7))
print(versiones_plone)

#mas rango
versiones_plone.extend(range(4,3))
print(versiones_plone)
