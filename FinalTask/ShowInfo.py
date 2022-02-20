def show_info():
    import pandas as df
    print("You have decided to show all information.")
    df = df.read_csv('shop_list.csv', delimiter=',',
        names=["category", "product", "cost", "date"])
    print(df)