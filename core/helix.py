from typing import List

class HelixEncoder:
    """
    Codificação ultra-densa inspirada em nucleotídeos.
    4 símbolos base = 2 bits por símbolo.
    """
    BASES = ['α', 'β', 'γ', 'δ']
    
    @staticmethod
    def to_helix( bytes) -> str:
        """
        Converte bytes para sequência tipo DNA.
        2 bits por símbolo = 4x mais denso que hex.
        """
        helix: List[str] = []
        for byte in 
            for i in range(0, 8, 2):
                pair = (byte >> i) & 0b11
                helix.append(HelixEncoder.BASES[pair])
        return ''.join(helix)
    
    @staticmethod
    def from_helix(helix: str) -> bytes:
        """
        Reconverte sequência DNA para bytes.
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
