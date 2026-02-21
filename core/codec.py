from typing import Any, Dict, Optional
from .morphology import GeneStructure
from .compression import SemanticCompressor

class CodecRegistry:
    """
    Registro de padrões de codificação. Extensível.
    """
    _handlers = {}

    @classmethod
    def register(cls, name: str):
        def wrapper(func):
            cls._handlers[name] = func
            return func
        return wrapper

    @classmethod
    def process(cls, morphology: str,  Any, context: Optional[Dict] = None) -> Any:
        handler = cls._handlers.get(morphism.replace('_cmp', ''))
        if handler:
            return handler(data, context)
        return data

@CodecRegistry.register("literal")
def _handle_literal( Any, ctx: Optional[Dict] = None) -> Any:
    return data

@CodecRegistry.register("repeat")
def _handle_repeat(data: Any, ctx: Optional[Dict] = None) -> Any:
    if ctx and 'count' in ctx:
        return data * ctx['count']
    return data

class DataCodec:
    @staticmethod
    def ingest(raw_ Any, compress: bool = True) -> Dict[str, Any]:
        """
        Transforma dado bruto em estrutura genética.
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
        Reconstrói o dado original a partir do gene.
        """
        m_id, sequence = GeneStructure.decompose(gene)
        
        if m_id.endswith('_cmp'):
            try:
                return SemanticCompressor.decode_payload(sequence)
            except Exception:
                return None
                
        return CodecRegistry.process(m_id, sequence, context)
