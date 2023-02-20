from dataclasses import dataclass, field

@dataclass
class User:
    id: str
    name: str
    orders_ids: str = ''

    def unpack(self) -> list[str]:
        all_data = self.__dict__.values()
        return [str(i) for i in all_data]

if __name__ == '__main__':
    user = User('12','ltt')
    print(user.unpack())
    
        

