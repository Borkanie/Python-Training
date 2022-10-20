

inputs="1,nepper,15,hamster,24,philipp,30,mmautne,31,hamster,49,thebenil,57,fliegimandi,59,ev,61,philipp,64,ev,74,philipp,69,philipp,71,fliegimandi,78,hamster,78,mio,95,hamster,103,macquereauxpl,135"
auctionPrice=1
betters={}
lastBidder=""
for el in inputs.split(","):
    if el.isnumeric():
        auctionPrice=int(el)
    else:
        if lastBidder in betters.keys():
            betters[lastBidder]=auctionPrice-1
        lastBidder=el
max=0
maxBeter=""
for key in betters.keys():
    if betters[key]>max:
        maxBeter=key
        max=betters[key]
        
print("Maxbetter=")
print(maxBeter)
print("\nMaxValue=")
print(max)