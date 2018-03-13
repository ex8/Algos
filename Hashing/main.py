from Hashing.chaining import Chaining
from Hashing.probing import LinearProbing


def main():
    # c = Chaining(size=11)           # Force collision
    # c.insert(key=53, value="Rawr")  # hash(53) = 9
    # c.insert(key=9, value="LEET")   # hash(9) = 9
    # c.insert(key=1, value="OSRS")
    # c.remove(key=1)
    # print(c.buckets)
    # print(c.find(key=1))
    # print(c.exists(key=1))

    lp = LinearProbing(size=11)
    lp.insert(key=1, data="56")
    lp.insert(key=1, data="58")
    lp.insert(key=1, data="60")
    lp.insert(key=5, data="62")
    lp.insert(key=5, data="64")
    lp.insert(key=4, data="66")
    lp.insert(key=4, data="68")
    lp.insert(key=4, data="70")
    lp.insert(key=4, data="72")
    lp.insert(key=4, data="74")
    lp.insert(key=4, data="76")
    lp.insert(key=4, data="78")
    # lp.remove(key=1)
    print(lp.buckets)
    print(lp.exists(key=1))
    print(lp.exists(key=2))
    print(lp.get(key=10))


if __name__ == "__main__":
    main()
