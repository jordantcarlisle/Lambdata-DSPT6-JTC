def enlarge(n):
    '''This function will multiply the input by 100'''
    return n * 100

if __name__ == '__main__':
    y = int(input('Choose a number:'))
    print(y, enlarge(y))

def download(url):
    filename = url.split('/')[-1]
    print(f'Downloading {url}')
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)
    print(f'Downloaded {filename}')


def to_dataframe_column(list):
    x = pd.series(list)
    df = DataFram(x)
    print(df)
