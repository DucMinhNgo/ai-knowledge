import pandas as pd
from scipy.spatial.distance import cosine

if __name__ == '__main__':
    data = pd.read_csv('../datasets/lastfm-matrix-germany.csv')
    # --- Start Item Based Recommendations --- #
    # Drop any column named "user"
    data_item_base = data.drop('user', 1)
    # print data_item_base.head(8).ix[:,0:6]
    # store DataFrame
    data_item_base_frame = pd.DataFrame(index=data_item_base.columns, columns=data_item_base.columns)
    # print data_item_base_frame.head(6).ix[:,0:6]
    # Calculate similarily
    for i in range(0, len(data_item_base_frame.columns)):
        # Loop through the columns for each column
        for j in range(0, len(data_item_base_frame.columns)):
            # Calculate similarity
            # print (i , " and ", j)
            data_item_base_frame.iloc[i, j] = 1 - cosine(data.iloc[:, i], data.iloc[:, j])

    data_item_base_frame.to_csv('data_item_base_frame.csv', sep=',', encoding='utf-8')
    # data_item_base_frame = pd.read_csv('data_item_base_frame.csv')
    print (data_item_base_frame.head(6).iloc[:,0:5])

    # Initial a frame for save closes neighbors to an item
    data_neighbors = pd.DataFrame(index=data_item_base_frame.columns, columns = range(1, 11))

    # Order by similarity
    for i in range(0, len(data_item_base_frame.columns)):
        data_neighbors.iloc[i,:10] = data_item_base_frame.iloc[0:, i].sort_values(ascending=False)[:10].index

    print (data_neighbors.head(6).iloc[:,0:4])