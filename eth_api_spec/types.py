from hexbytes import HexBytes


class address(str):
    pass


class uint(int):
    pass


class uint64(int):
    pass


class uint256(int):
    pass


class hash32(HexBytes):
    pass


class bytes256(HexBytes):
    pass


class bytes32(HexBytes):
    pass


class bytes8(HexBytes):
    pass


class byte(int):
    pass
