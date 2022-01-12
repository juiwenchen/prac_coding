from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # address duplicates in the list
        A, B = map(set, zip(*paths))
        return (B-A).pop()

        # if 1 <= len(paths) <= 100:
        #     flatten_cities = []
        #     two_unique_cities = []
        #     for path in paths:
        #         if len(path) == 2:
        #             flatten_cities.extend(path)
        #         else:
        #             return False
        # else:
        #     return False
            
        # two_unique_cities = [ city for city in flatten_cities if flatten_cities.count(city) == 1]
        # if len(two_unique_cities) != 2:
        #     return False

        # for idx in range(len(flatten_cities)):
        #     if 1 <= len(flatten_cities[idx]) <= 10:
        #         if flatten_cities[idx] in two_unique_cities:
        #             if (idx % 2) == 0:
        #                 start_city = flatten_cities[idx]
        #             else:
        #                 destination = flatten_cities[idx]
        #                 return destination
        #     else:
        #         return False

def main():
    paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
    destiny = Solution().destCity(paths=paths)
    print(destiny)


if __name__ == '__main__':
    main()