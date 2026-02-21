from typing import List

class HelixEncoder:
    """
    Ultra-dense encoding inspired by nucleotides.
    4 base symbols = 2 bits per symbol.
    """
    BASES = ['α', 'β', 'γ', 'δ']
    
    @staticmethod
    def to_helix(data: bytes) -> str:
        """
        Converts bytes to DNA-like sequence.
        2 bits per symbol = 4x denser than hex.
        """
        helix: List[str] = []
        for byte in data:
            for i in range(0, 8, 2):
                pair = (byte >> i) & 0b11
                helix.append(HelixEncoder.BASES[pair])
        return ''.join(helix)
    
    @staticmethod
    def from_helix(helix: str) -> bytes:
        """
        Reconverts DNA sequence to bytes.
        """
        reverse_map = {v: k for k, v in enumerate(HelixEncoder.BASES)}
        bytes_list: List[int] = []
        for i in range(0, len(helix), 4):
            byte = 0
            for j, pos in enumerate(range(i, i+4)):
                if pos < len(helix):
                    byte |= reverse_map.get(helix[pos], 0) << (j * 2)
            bytes_list.append(byte)
        return bytes(bytes_list)
