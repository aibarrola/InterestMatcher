# Mentorship Pairing Tool
Allows pairing committee members to efficiently pair big and littles based on interest
---
__Context__: The mentorship program are for new members to sign up as little brother/sister and for older members to sign up as big brother/sister. When they sign up, they fill out a detailed application that asks them about their interest, personality, life experience, and more. A committee then looks at these applications and pairs up a little with a big that can help mentor and guide them through college and life. This pairing process is long and tedious as the committee has to go through every application multiple times one by one to make sure they get the best pairing. This is just messy, inefficient, and difficult. This tool will allow more quality pairings and give more time for the committee to focus on other aspects of the application.

__Challenges__: We had to figure out the best algorithm or data structure that best fits our model. We narrowed it down between: Radix sort, Priority Queue using heaps, and Bipartite matching algorithm. We decided with Radix sort because it has a time complexity of O(n) and it works with our model since it will always be a fixed number of bigs/littles. However, it takes more memory.

__Personal Impact__: Increased accuracy of compatibilities by 10% by adding a dynamic factor to the algorithm
Created the algorithm and point system that would determine compatibility between a big and little based on interests

## Installments
```
pip install Flask
pip install Flask-WTF
pip install gspread
pip install oauth2client
pip install dataclass
```

## How it works:
1) Have all the big and littles fill out the google form that ask about interests
2) Run the website
3) Click on Littles button
4) Click on a little's name
5) View the top 5 bigs that are compatible with that little


# Demonstration 
![](pairingtooldemo.gif)
