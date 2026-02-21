from typing import Any, Dict, Tuple
from .integrity import IntegrityEngine

class GeneStructure:
    """
    Define o esquema atômico de um gene no Kernel Rain.
    """
    
    @staticmethod
    def compose(morphology_id: str, sequence_ Any, compress: bool = False) -> Dict[str, Any]:
        """
        Monta a estrutura base com assinatura embutida.
        """
        payload_vector = f"{morphology_id}{sequence_data}"
        signature = IntegrityEngine.derive_fingerprint(payload_vector)
        
        return {
            "v": "0.1",
            "m": morphology_id,
            "s": sequence_data,
            "sig": signature
        }

    @staticmethod
    def decompose(gene: Dict[str, Any]) -> Tuple[str, Any]:
        """
        Extrai componentes válidos para processamento.
        """
        return gene.get("m"), gene.get("s")
