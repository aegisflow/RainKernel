import json
import zlib
import base64
from typing import Any, Dict

class SymbolTable:
    """
    Global dictionary of frequent symbols for IA/Logs.
    """
    COMMON_TOKENS = {
        "id": "§1", "type": "§2", "data": "§3", 
        "user": "§4", "system": "§5", "error": "§6",
        "timestamp": "§7", "status": "§8", "ok": "§9",
        "content": "§a", "role": "§b", "assistant": "§c",
        "message": "§d", "prompt": "§e", "response": "§f"
    }
    
    @classmethod
    def compress_text(cls, text: str) -> str:
        for token, code in cls.COMMON_TOKENS.items():
            text = text.replace(token, code)
        return text

    @classmethod
    def decompress_text(cls, text: str) -> str:
        for token, code in cls.COMMON_TOKENS.items():
            text = text.replace(code, token)
        return text

class SemanticCompressor:
    """
    Compression engine specific for structured data.
    """
    
    @staticmethod
    def encode_payload(data: Any) -> str:
        """
        1. Serialize 2. Semantic Substitution 3. Binary Compress 4. Base64
        """
        json_str = json.dumps(data, separators=(',', ':'))
        semantic_str = SymbolTable.compress_text(json_str)
        compressed = zlib.compress(semantic_str.encode('utf-8'), level=9)
        return base64.b64encode(compressed).decode('ascii')

    @staticmethod
    def decode_payload(blob: str) -> Any:
        """
        Reverses the exact process.
        """
        compressed = base64.b64decode(blob.encode('ascii'))
        semantic_str = zlib.decompress(compressed).decode('utf-8')
        json_str = SymbolTable.decompress_text(semantic_str)
        return json.loads(json_str)

    @staticmethod
    def calculate_ratio(original_bytes: int, compressed_bytes: int) -> float:
        if original_bytes == 0:
            return 0.0
        return (1 - (compressed_bytes / original_bytes)) * 100
