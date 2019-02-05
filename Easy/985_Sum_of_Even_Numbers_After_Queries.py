class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        sums = []
        init_sum = sum(i for i in A if not i%2)
        for query in queries:
            if A[query[1]] % 2 == 0:
                last = A[query[1]]
                A[query[1]] += query[0]
                if A[query[1]] % 2 == 0:
                    init_sum = init_sum + query[0]
                else:
                    init_sum = init_sum - last
            else:
                A[query[1]] += query[0]
                if A[query[1]] % 2 == 0:
                    init_sum = init_sum + A[query[1]]
            sums.append(init_sum)
        return sums
