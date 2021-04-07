import random

def process():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1
  numberOfQuotes = random.randint(0, last)

  for x in range(numberOfQuotes):
    quoteIndex = random.randint(0, last)
    print(quotes[quoteIndex].removesuffix("\n"))

if __name__== "__main__":
  process()
