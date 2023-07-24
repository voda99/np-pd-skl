import pandas as pd
authors = pd.DataFrame(
    {
     'author_id' : [1, 2, 3],
     'author_name' : ['Тургенев', 'Чехов', 'Островский']
    }
)
book = pd.DataFrame(
    {
     'author_id' :  [1, 1, 1, 2, 2, 3, 3],
     'book_title' : ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
     'price' : [500, 400, 300, 350, 450, 600, 200]
    }
)
authors_price = pd.merge(authors, book, how='outer', on='author_id')
top5 = authors_price.sort_values('price', ascending=False).head(5)
authors_stats = authors_price.groupby('author_name')['price'].agg(['min', 'max', 'mean']).rename(
    columns={'min' : 'min_price', 'max' : 'max_priice', 'mean' : 'mean_price'})
authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
book_info = authors_price.pivot_table(values='price', index='author_name', columns='cover', aggfunc='sum', fill_value=0)
book_info.to_pickle('book_info.pkl')
book_info2 = pd.read_pickle('book_info.pkl')
