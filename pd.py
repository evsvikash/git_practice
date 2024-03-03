import pandas as pd
simpsons = pd.read_html('https://en.wikipedia.org/wiki/The_Simpsons')
len(simpsons)
print(len(simpsons))
print(simpsons[5])