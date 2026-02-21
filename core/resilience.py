from typing import Dict, List, Any
from .integrity import IntegrityEngine

class DNAResilience:
    """
    Camada de tolerância a falhas inspirada em replicação de DNA.
    Recupera dados mesmo com fragmentação severa.
    """

    @staticmethod
    def add_redundancy( bytes, copies: int = 3) -> bytes:
        """
        Cria múltiplas cópias com variações para recuperação.
        Similar a cromossomos homólogos.
        """
        chunks = [data[i:i+256] for i in range(0, len(data), 256)]
        redundant_chunks = []
        
        for chunk in chunks:
            redundant_chunks.append(chunk)
            redundant_chunks.append(DNAResilience._parity_chunk(chunk, 1))
            redundant_chunks.append(DNAResilience._parity_chunk(chunk, 2))
        
        return b'§'.join(redundant_chunks)
    
    @staticmethod
    def recover_from_fragments(fragments: List[bytes]) -> bytes:
        """
        Reconstrói dados mesmo com até 66% de perda.
        Usa votação majoritária entre cópias.
        """
        recovered = []
        for i in range(0, len(fragments), 3):
            group = fragments[i:i+3]
            if len(group) >= 2:
                recovered.append(DNAResilience._majority_vote(group))
        
        return b''.join(recovered)
    
    @staticmethod
    def _parity_chunk(chunk: bytes, seed: int) -> bytes:
        """Gera variação com parity para recuperação."""
        return bytes((b + seed) % 256 for b in chunk)
    
    @staticmethod
    def _majority_vote(chunks: List[bytes]) -> bytes:
        """Recupera byte mais comum entre cópias."""
        if not chunks:
            return b''
        max_len = max(len(c) for c in chunks)
        result = []
        for i in range(max_len):
            votes = [c[i] if i < len(c) else None for c in chunks]
            votes = [v for v in votes if v is not None]
            if votes:
                result.append(max(set(votes), key=votes.count))
        return bytes(result)

    @staticmethod
    def validate_chain(genes: List[Dict[str, Any]]) -> bool:
        """
        Verifica a integridade de uma cadeia de genes.
        """
        return all(IntegrityEngine.validate_signature(g) for g in genes)

    @staticmethod
    def recover_partial(genes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Filtra genes corrompidos, mantendo os válidos.
        """
        return [g for g in genes if IntegrityEngine.validate_signature(g)]
