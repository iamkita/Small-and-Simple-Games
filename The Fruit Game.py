result = input("Type your favorite fruit from the list to get some information about it- Apple, Orange, Banana, Blueberry, Strawberry or Grapes: ")

if result == "Apple":
  print("An apple is an edible fruit produced by an apple tree. Apple trees are cultivated worldwide and are the most widely grown species in the genus Malus. The tree originated in Central Asia, where its wild ancestor, Malus sieversii, is still found today.")
elif result == "Orange":
  print("The orange is the fruit of various citrus species in the family Rutaceae; it primarily refers to Citrus × sinensis, which is also called sweet orange, to distinguish it from the related Citrus × aurantium, referred to as bitter orange.")
elif result == "Banana":
  print("A banana is an elongated, edible fruit – botanically a berry – produced by several kinds of large herbaceous flowering plants in the genus Musa. In some countries, bananas used for cooking may be called 'plantains', distinguishing them from dessert bananas.")
elif result == "Blueberry":
  print("Blueberries are perennial flowering plants with blue or purple berries. They are classified in the section Cyanococcus within the genus Vaccinium. Vaccinium also includes cranberries, bilberries, huckleberries and Madeira blueberries. Commercial blueberries—both wild and cultivated —are all native to North America.")
elif result == "Strawberry":
  print("The garden strawberry is a widely grown hybrid species of the genus Fragaria, collectively known as the strawberries, which are cultivated worldwide for their fruit. The fruit is widely appreciated for its characteristic aroma, bright red color, juicy texture, and sweetness.")
elif result == "Grapes":
  print("A grape is a fruit, botanically a berry, of the deciduous woody vines of the flowering plant genus Vitis. Grapes can be eaten fresh as table grapes or they can be used for making wine, jam, grape juice, jelly, grape seed extract, raisins, vinegar, and grape seed oil.")
else:
  print("Invalid Input, you might have missed capital-letters or you have typed a fruit which is not in the list provided.")
