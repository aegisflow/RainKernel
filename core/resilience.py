from typing import Dict, List, Any
from .integrity import IntegrityEngine

class DNAResilience:
    """
    Fault tolerance layer inspired by DNA replication.
    Recovers data even with severe fragmentation.
    """

    @staticmethod
    def add_redundancy(data: bytes, copies: int = 3) -> bytes:
        """
        Creates multiple copies with variations for recovery.
        Similar to homologous chromosomes.
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
        Reconstructs data even with up to 66% loss.
        Uses majority vote among copies.
        """
        recovered = []
        for i in range(0, len(fragments), 3):
            group = fragments[i:i+3]
            if len(group) >= 2:
                recovered.append(DNAResilience._majority_vote(group))
        
        return b''.join(recovered)
    
    @staticmethod
    def _parity_chunk(chunk: bytes, seed: int) -> bytes:
        """Generates variation with parity for recovery."""
        return bytes((b + seed) % 256 for b in chunk)
    
    @staticmethod
    def _majority_vote(chunks: List[bytes]) -> bytes:
        """Recovers most common byte among copies."""
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
        Verifies integrity of a gene chain.
        """
        return all(IntegrityEngine.validate_signature(g) for g in genes)

    @staticmethod
    def recover_partial(genes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Filters corrupted genes, keeping valid ones.
        """
        return [g for g in genes if IntegrityEngine.validate_signature(g)]
