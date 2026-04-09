import numpy as np
import matplotlib.pyplot as plt 


lamb =lambda t:  0.5*(1+(t/30)**2)
lambdaMax = lamb(120)

t =0
events = []
while(t<=120):
    E = np.random.exponential(1/lambdaMax)
    t = t+E
    if(t>120):
        break
    U = np.random.random()

    rate = lamb(t)/lambdaMax
    if(U<=rate):
        events.append(t)

events = np.array(events)
bins = np.arange(0, 121, 1)

counts, _ = np.histogram(events, bins=bins)

plt.bar(bins[:-1], counts, width=1)
plt.xlabel("Day")
plt.ylabel("Number of reports")
plt.title("Flu Reports per Day (0–120)")
plt.show()
total = len(events)
print(f"Total Number of Events: {total}")
print(f"Expected Number of Events: 380")
print(f"|Expected-Total Number of Events|: {total -380}")