from typing import Any, Dict, Optional
from .morphology import GeneStructure
from .compression import SemanticCompressor

class CodecRegistry:
    """
    Encoding pattern registry. Extensible.
    """
    _handlers = {}

    @classmethod
    def register(cls, name: str):
        def wrapper(func):
            cls._handlers[name] = func
            return func
        return wrapper

    @classmethod
    def process(cls, morphology: str, data: Any, context: Optional[Dict] = None) -> Any:
        handler = cls._handlers.get(morphism.replace('_cmp', ''))
        if handler:
            return handler(data, context)
        return data

@CodecRegistry.register("literal")
def _handle_literal(data: Any, ctx: Optional[Dict] = None) -> Any:
    return data

@CodecRegistry.register("repeat")
def _handle_repeat(data: Any, ctx: Optional[Dict] = None) -> Any:
    if ctx and 'count' in ctx:
        return data * ctx['count']
    return data

class DataCodec:
    @staticmethod
    def ingest(raw_data: Any, compress: bool = True) -> Dict[str, Any]:
        """
        Transforms raw data into genetic structure.
        """
        if compress and isinstance(raw_data, (dict, list)):
            sequence = SemanticCompressor.encode_payload(raw_data)
            morphology = "literal_cmp"
        else:
            sequence = str(raw_data)
            morphology = "literal"
            
        return GeneStructure.compose(morphology, sequence)

    @staticmethod
    def express(gene: Dict[str, Any], context: Optional[Dict] = None) -> Any:
        """
        Reconstructs original data from gene.
        """
        m_id, sequence = GeneStructure.decompose(gene)
        
        if m_id.endswith('_cmp'):
            try:
                return SemanticCompressor.decode_payload(sequence)
            except Exception:
                return None
                
        return CodecRegistry.process(m_id, sequence, context)
