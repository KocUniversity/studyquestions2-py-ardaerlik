1. Write a simple Python program that creates a class called `House` to represent a great house in Westeros, yes, we are talking about Game of Thrones universe again! Let the `House` object have a `motto` and `sigil` attributes required initially, that is in the `__init__` method.

2. Create instances of `House` object to represent the following great Houses in Westeros:

* **House Stark**: House Stark's sigil is a "direwolf", a powerful creature that is larger than most wolves and can grow to the size of the horse. The Stark's six children (including Jon Snow) each had a direwolf to protect them. The motto of House Stark is "Winter is coming".

* **House Arryn**: The motto of House Arryn is "As High As Honor". The sigil of House Arryn is a "falcon" soaring against the moon.

* **House Lannister**: Their sigil is a "golden lion" on a crimson field and the motto is "Hear Me Roar!". Another popular saying attributed to them is that "A Lannister always pays his debts".

* **House Targaryen**: The Targaryen sigil is a "three-headed dragon", red on black. The three heads are supposed to represent Aegon and his sisters, founder of the Old Dynasty. Their motto is "Fire and Blood".

* **House Greyjoy**: Their sigil is a "golden kraken" upon a black field, which befits their culture as seafarers and raiders. The motto is "We Do Not Sow".

* **House Baratheon**: The House Baratheon’s motto is "Ours is the Fury". Its sigil is a "crowned black stag" on a golden field.

* **House Martell**: Their sigil is a "red sun pierced by a golden spear". Their motto is "Unbowed, Unbent, Unbroken".

* **House Tully**: Their sigil is a "silver trout" leaping over a field of blue and red. The motto of House Tully is "Family, Duty, Honor".

* **House Tyrell**: The Tyrell sigil is a "golden rose" on a grass-green field. Ser Loras, a popular knight from the Tyrell family, is known as the "Knight of Flowers". Their motto is "Growing Strong".

3. Add getter methods `speak` and `show` to the `House` class which returns the `motto` and the `sigil` of the house, respectively. Then, also add setter methods for both called `set_motto`/`set_sigil` which take a new motto/sigil and changes the value of the respective properties when called.

4. Implement an interface for the `House` class, that's when we try to print `Stark` instance for example, it says something like:

> Our sigil is a direwolf and our motto is "Winter is Coming!".

**Hint** Remember the `__str__` method?

5. Add a method called `make_an_alliance` which takes another `House` object as an argument and creates an alliance with that `House` object. Keep a list of allies for the `House` object and append to that list each time a new alliance is established. Do not forget to modify both objects to have a two-way alliance.

6. Similarly, write a method called `go_to_war` which breaks the alliance with the `House` object given as an argument by removing it from the list of allies for both houses. Also, keep track of the houses that are at war with the house object by adding a list of `enemies`. When there is a new alliance, the new alliance should be removed from the list of `enemies`.

Create a list of alliances initially to test your implementation and start wars between random houses. Print the state of Westeros after each war by printing all the houses.

Try to add more fun functionalities such as `make_peace` to end wars, `conspire_against` a house together with another house :)