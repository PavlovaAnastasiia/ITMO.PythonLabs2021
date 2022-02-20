def sorting():
    import pandas
    print("You have decided to sort values from lower price to higher!")
    df = pandas.read_csv('shop_list.csv', delimiter=',',
        names=["category", "product", "cost", "date"])
    print(df.sort_values(by='cost'))