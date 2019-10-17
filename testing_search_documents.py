import search_documents as sd

buckets_list = [[[0],[1,2]],[[0,1],[2]]]
query_bucket_list = [0, 1]

doc_list = sd.getDocuments(buckets_list, query_bucket_list)
print(doc_list)