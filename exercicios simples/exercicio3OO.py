class classe(object):
    __nums = 0

    def __init__(self,n):
        self.__nums = n

    def maior(self):
        print(max(self.__nums))

    def menor(self):
        print(min(self.__nums))


nums = classe(input().split())

nums.maior()
nums.menor()
