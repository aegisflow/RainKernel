import hashlib
import binascii
from typing import Union, Dict, Any

class IntegrityEngine:
    """
    Cryptographic Integrity Engine.
    Ensures genes do not suffer external entropy.
    """
    
    @staticmethod
    def derive_fingerprint(payload: Union[str, bytes]) -> str:
        """
        Generates immutable identity vector (SHA-256 wrapped).
        Does not use ephemeral system hash.
        """
        if isinstance(payload, str):
            payload = payload.encode('utf-8')
        
        raw_digest = hashlib.sha256(payload).digest()
        return binascii.hexlify(raw_digest).decode('ascii')[:16]

    @staticmethod
    def validate_signature(sequence: Dict[str, Any]) -> bool:
        """
        Verifies structure has not been corrupted.
        """
        if 'sig' not in sequence:
            return False
            
        payload = f"{sequence.get('m')}{sequence.get('s')}"
        expected = IntegrityEngine.derive_fingerprint(payload)
        
        return sequence['sig'] == expected
