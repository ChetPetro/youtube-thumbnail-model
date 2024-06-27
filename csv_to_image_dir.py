import pandas as pd
import urllib.request 

def main():
    df = pd.read_csv('thumbnail_data.csv')
    df['score'] = df['score'] // 0.25
    df = df.reset_index()

    for index, row in df.iterrows():
        imgURL = row['thumbnail']
        try:
            urllib.request.urlretrieve(imgURL, f'images/{int(row['score'])}/img{index}.jpg')
        except:
            pass
    
    print('done')
    
if __name__ == '__main__':
    main()
