class LinkedList:
    
    def __init__(self):
        self.List = []
    
    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.List):
            return -1
        return self.List[index]

    def insertHead(self, val: int) -> None:
        self.List.insert(0, val)

    def insertTail(self, val: int) -> None:
        self.List.append(val)

    def remove(self, index: int) -> bool:
        if index < 0 or index >= len(self.List):
            return False
        self.List.remove(self.List[index])
        return True

    def getValues(self) -> List[int]:
        return self.List
