#!/usr/bin/env python3
"""
Rain Kernel - Usage Examples
============================
Three demonstrations in a single file.

Run:
    python examples.py              # All examples
    python examples.py 1            # Example 1 only
    python examples.py 2            # Example 2 only
    python examples.py 3            # Example 3 only
"""

import json
import sys
from kernel import DataCodec, IntegrityEngine, DNAResilience, GeneExpression

# ============================================================================
# EXAMPLE 1: Basic Usage (Encode/Decode)
# ============================================================================

def example_1_basic():
    """Demonstrates the fundamental flow of encoding and decoding."""
    print("\n" + "=" * 50)
    print("📌 Example 1: Basic Usage")
    print("=" * 50)
    
    original = {
        "message": "Hello Digital Eternity",
        "timestamp": "2024-01-15T10:30:00Z",
        "tags": ["dna", "kernel", "resilient"]
    }
    
    print(f"\n📥 Original: {json.dumps(original, ensure_ascii=False)}")
    
    # Encode
    gene = DataCodec.ingest(original, compress=True)
    print(f"🧬 Gene: {gene['sig'][:16]}... (v{gene['v']})")
    
    # Verify integrity
    valid = IntegrityEngine.validate_signature(gene)
    print(f"🛡️ Integrity: {'✅ Valid' if valid else '❌ Corrupted'}")
    
    # Decode
    recovered = DataCodec.express(gene)
    print(f"📤 Recovered: {json.dumps(recovered, ensure_ascii=False)}")
    
    # Fidelity check
    match = original == recovered
    print(f"{'✅ DATA IDENTICAL' if match else '❌ DATA CORRUPTED'}")

# ============================================================================
# EXAMPLE 2: DNA Resilience (Self-Healing)
# ============================================================================

def example_2_resilience():
    """Simulates corruption and demonstrates DNA-inspired recovery."""
    print("\n" + "=" * 50)
    print("📌 Example 2: DNA Resilience")
    print("=" * 50)
    
    data = b"Critical Data Block - Rain Kernel Test" * 5
    print(f"\n📥 Original: {len(data)} bytes")
    
    # Add redundancy
    redundant = DNAResilience.add_redundancy(data, copies=3)
    fragments = redundant.split(b'§')
    print(f"🔐 Fragments with redundancy: {len(fragments)}")
    
    # Simulate 50% loss
    import random
    random.shuffle(fragments)
    remaining = fragments[:len(fragments)//2 + 1]
    print(f"🔥 After 50% loss: {len(remaining)} fragments")
    
    # Recover
    recovered = DNAResilience.recover_from_fragments(remaining)
    success = recovered == data
    
    print(f"🔍 Recovery: {'✅ 100% SUCCESS' if success else '⚠️ PARTIAL'}")
    if success:
        print(f"💾 Data recovered: {len(recovered)} bytes")

# ============================================================================
# EXAMPLE 3: Chat Seed (Expression with Context)
# ============================================================================

def example_3_chat_seed():
    """Demonstrates conversations stored as executable genetic seeds."""
    print("\n" + "=" * 50)
    print("📌 Example 3: Chat Seed")
    print("=" * 50)
    
    # Simulate messages as genes
    messages = [
        {"role": "user", "content": "What is the Rain Kernel principle?"},
        {"role": "assistant", "content": "Data is not stored. It is reconstructed."},
        {"role": "user", "content": "How does resilience work?"},
        {"role": "assistant", "content": "DNA-inspired. Fragments recover the whole."}
    ]
    
    print("\n📝 Encoding conversation...")
    genes = [DataCodec.ingest(msg, compress=True) for msg in messages]
    
    for i, gene in enumerate(genes):
        print(f"   [{i+1}] Gene: {gene['sig'][:8]}...")
    
    print("\n🔓 Recovering conversation...")
    for i, gene in enumerate(genes):
        msg = DataCodec.express(gene)
        emoji = "👤" if msg.get("role") == "user" else "🤖"
        print(f"   {emoji} {msg.get('role')}: {msg.get('content')}")
    
    # Expression with context (demonstration)
    print("\n🎭 Expression with context...")
    repeat_gene = DataCodec.ingest("Echo: ", compress=False)
    repeat_gene["m"] = "repeat"
    result = GeneExpression.execute(repeat_gene, {"count": 3})
    print(f"   Result: '{result}'")

# ============================================================================
# MAIN
# ============================================================================

def run_all():
    """Runs all examples."""
    print("\n🧬 Rain Kernel - Usage Examples")
    print("=" * 50)
    example_1_basic()
    example_2_resilience()
    example_3_chat_seed()
    print("\n" + "=" * 50)
    print("✅ All examples completed")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            num = int(sys.argv[1])
            if num == 1:
                example_1_basic()
            elif num == 2:
                example_2_resilience()
            elif num == 3:
                example_3_chat_seed()
            else:
                print(f"Example {num} not found. Use 1, 2, or 3.")
        except ValueError:
            print("Usage: python examples.py [1|2|3]")
    else:
        run_all()
