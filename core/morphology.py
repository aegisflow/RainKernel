from typing import Any, Dict, Tuple
from .integrity import IntegrityEngine

class GeneStructure:
    """
    Defines the atomic schema of a gene in Rain Kernel.
    """
    
    @staticmethod
    def compose(morphology_id: str, sequence_data: Any, compress: bool = False) -> Dict[str, Any]:
        """
        Builds base structure with embedded signature.
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
        Extracts valid components for processing.
        """
        return gene.get("m"), gene.get("s")
