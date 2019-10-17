from LSH import LSH
import search_documents as sd

if __name__ == '__main__':
    list = [[1,0,1],[1,1,1],[1,0,0],[0,0,1],[0,1,0],[0,1,1]]
    search_list = [[1],[0],[1],[0],[1],[1]]
    lsh = LSH(list,3,2)
    buckets_list = lsh._bucket_matrix()
    lsh_search = LSH(search_list,3,2,True)
    query_bucket_list = lsh_search._bucket_value_matrix()
    print(buckets_list)
    print(query_bucket_list)
    doc_list = sd.getDocuments(buckets_list, query_bucket_list)
    print(doc_list)
    
