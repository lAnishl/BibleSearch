from LSH import LSH

if __name__ == '__main__':
    list = [[1,0,1],[1,1,1],[1,0,0],[0,0,1],[0,1,0],[0,1,1]]
    lsh = LSH(list,3,2)
    val = lsh._bucket_matrix()
    print(val)
