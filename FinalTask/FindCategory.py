
def show_by_category():
    print("You have decided to show products by category.")
    import pandas
    df = pandas.read_csv('shop_list.csv', delimiter=',',
        names=["category", "product", "cost", "date"])
    category = input('Category:')
    print(df.loc[df['category'] == category])