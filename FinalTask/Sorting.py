def sorting():
    import pandas as df
    print("You have decided to sort values from lower price to higher!")
    df = df.read_csv('shop_list.csv', delimiter=',',
        names=["category", "product", "cost", "date"])
    print(df.sort_values(by='cost'))