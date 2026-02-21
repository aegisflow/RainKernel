import hashlib
import binascii
from typing import Union, Dict, Any

class IntegrityEngine:
    """
    Motor de Integridade Criptográfica.
    Garante que genes não sofram entropia externa.
    """
    
    @staticmethod
    def derive_fingerprint(payload: Union[str, bytes]) -> str:
        """
        Gera vetor de identidade imutável (SHA-256 wrapped).
        Não utiliza hash efêmero do sistema.
        """
        if isinstance(payload, str):
            payload = payload.encode('utf-8')
        
        raw_digest = hashlib.sha256(payload).digest()
        return binascii.hexlify(raw_digest).decode('ascii')[:16]

    @staticmethod
    def validate_signature(sequence: Dict[str, Any]) -> bool:
        """
        Verifica se a estrutura não foi corrompida.
        """
        if 'sig' not in sequence:
            return False
            
        payload = f"{sequence.get('m')}{sequence.get('s')}"
        expected = IntegrityEngine.derive_fingerprint(payload)
        
        return sequence['sig'] == expected
