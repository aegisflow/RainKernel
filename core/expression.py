from typing import Dict, Any, Callable, Optional, List

class GeneExpression:
    """
    Faz os genes 'expressarem' dados como DNA expressa proteínas.
    O dado vira comportamento executável.
    """
    
    @staticmethod
    def transcribe(gene: Dict[str, Any]) -> Callable[[Optional[Dict]], Any]:
        """
        Transforma gene em função executável.
        """
        def express(context: Optional[Dict[str, Any]] = None) -> Any:
            if context is None:
                context = {}
            
            morphology = gene.get('m', 'literal')
            sequence = gene.get('s', '')
            
            # Remove sufixo de compressão para avaliação
            morphology = morphology.replace('_cmp', '')
            
            if morphology == 'literal':
                return sequence
            elif morphology == 'repeat':
                count = context.get('count', 1)
                return sequence * count
            elif morphology == 'transform':
                if context.get('uppercase', False):
                    return sequence.upper()
                return sequence.lower() if context.get('lowercase', False) else sequence
            elif morphology == 'compose':
                if isinstance(sequence, list):
                    return [g.get('s', '') for g in sequence]
                return sequence
            elif morphology == 'conditional':
                if context.get('condition', False):
                    return sequence
                return context.get('alternative', '')
            
            return sequence
        
        return express

    @staticmethod
    def execute(gene: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Any:
        """
        Executa a expressão do gene imediatamente.
        """
        expression = GeneExpression.transcribe(gene)
        return expression(context)
