import numpy as np


class LSH:
    def __init__(self, matrix, bands: int, bucket_length = 3, search_query=False):
        self._signature_matrix = np.array(matrix)
        self._search_query = search_query
        self._bands = bands
        self._bucket_length = bucket_length
        if self._search_query:
            self.bucket_value_matrix = self.__solver()

        else:
            self.bucket_matrix = self.__solver()

    def __solver(self):
        rows, cols = self._signature_matrix.shape
        bands = self._bands
        band_length = int(rows/bands)
        if rows % bands != 0:
            raise Exception

        # band buckets matrix b*bucket_length*docs list
        bucket_matrix = [[[] for buckets in range(self._bucket_length)] for row in range(bands)]
        # hashed_vale list for search query
        bucket_value_list = []

        for band in range(bands):
            for col in range(cols):
                band_vector = self._signature_matrix[band*band_length:(band+1)*band_length, col]
                col_decimal_value = band_vector.dot(2**np.arange(band_vector.size)[::-1])
                hashed_col_value = self.__hash_function(col_decimal_value)
                if self._search_query:
                    bucket_value_list.append(hashed_col_value)
                else:
                    bucket_matrix[band][hashed_col_value].append(col)
        # for LSH search query
        if self._search_query:
            return bucket_value_list
        # for LSH of all documents
        return bucket_matrix

    def __hash_function(self, value):
        value = value * 2 + 1
        return value % self._bucket_length

    def _bucket_matrix(self):
        # return bucket matrix bands * hash mod * documents
        if self._search_query:
            raise Exception

        return self.bucket_matrix

    def _bucket_value_matrix(self):
        if not self._search_query:
            raise Exception

        return self.bucket_value_matrix
