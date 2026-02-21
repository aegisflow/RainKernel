"""
Rain Kernel Self-Validator
Verifica a integridade, sanidade e saúde do núcleo.
Inspired by DNA self-repair mechanisms.
"""
import sys
import importlib
from typing import List, Tuple

class KernelValidator:
    """
    Valida a saúde do Rain Kernel usando seus próprios mecanismos.
    """
    
    @staticmethod
    def check_integrity() -> Tuple[bool, List[str]]:
        """Verifica se os módulos críticos importam sem erro."""
        errors = []
        modules = [
            'core.integrity',
            'core.morphology', 
            'core.compression',
            'core.codec',
            'core.resilience',
            'core.helix',
            'core.expression'
        ]
        
        for mod in modules:
            try:
                importlib.import_module(mod)
            except ImportError as e:
                errors.append(f"❌ {mod}: {e}")
        
        return len(errors) == 0, errors

    @staticmethod
    def check_semantic_sanity() -> Tuple[bool, str]:
        """Teste rápido de compressão/decompressão para validar lógica."""
        try:
            from core.codec import DataCodec
            from core.integrity import IntegrityEngine
            
            test_data = {"test": "rain_kernel", "v": 1}
            gene = DataCodec.ingest(test_data, compress=True)
            
            # Verifica assinatura
            if not IntegrityEngine.validate_signature(gene):
                return False, "❌ Signature validation failed"
            
            # Verifica reconstrução
            recovered = DataCodec.express(gene)
            if recovered != test_
                return False, "❌ Data reconstruction mismatch"
                
            return True, "✅ Semantic round-trip OK"
        except Exception as e:
            return False, f"❌ Sanity check error: {e}"

    @staticmethod
    def run_full_diagnostic() -> int:
        """Executa todos os checks e retorna código de saída (0=ok, 1=fail)."""
        print("🧬 Rain Kernel Self-Diagnostic v0.1")
        print("-" * 40)
        
        # Check 1: Integridade de Imports
        print("🔍 Checking module integrity...")
        ok, errors = KernelValidator.check_integrity()
        if ok:
            print("✅ All core modules imported successfully")
        else:
            for err in errors:
                print(err)
            return 1
        
        # Check 2: Sanidade Semântica
        print("\n🔍 Running semantic sanity check...")
        ok, msg = KernelValidator.check_semantic_sanity()
        print(msg)
        if not ok:
            return 1
            
        print("\n" + "-" * 40)
        print("🟢 Kernel Health: OPTIMAL")
        print("🚀 Ready for production use")
        return 0

if __name__ == "__main__":
    sys.exit(KernelValidator.run_full_diagnostic())
