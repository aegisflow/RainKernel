from typing import Dict, Any, Callable, Optional, List

class GeneExpression:
    """
    Makes genes 'express' data like DNA expresses proteins.
    Data becomes executable behavior.
    """
    
    @staticmethod
    def transcribe(gene: Dict[str, Any]) -> Callable[[Optional[Dict]], Any]:
        """
        Transforms gene into executable function.
        """
        def express(context: Optional[Dict[str, Any]] = None) -> Any:
            if context is None:
                context = {}
            
            morphology = gene.get('m', 'literal')
            sequence = gene.get('s', '')
            
            # Remove compression suffix for evaluation
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
        Executes gene expression immediately.
        """
        expression = GeneExpression.transcribe(gene)
        return expression(context)
