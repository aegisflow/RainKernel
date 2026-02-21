import json
import gzip
from core.codec import DataCodec
from core.compression import SemanticCompressor
from core.resilience import DNAResilience
from core.integrity import IntegrityEngine

def generate_ai_log_sample():
    """Generates a typical IA log (highly repetitive)."""
    base = {
        "type": "chat_completion",
        "user": "admin",
        "timestamp": "2023-10-27T10:00:00Z",
        "status": "ok",
        "data": { "prompt": "Explain quantum", "tokens": 150, "model": "rain-v1" }
    }
    return [base.copy() for _ in range(100)]

def test_resilience():
    """Tests recovery of corrupted fragments."""
    data = b"Rain Kernel Resilience Test Data" * 10
    redundant = DNAResilience.add_redundancy(data)
    
    # Simulates 50% loss
    fragments = redundant.split(b'§')
    import random
    random.shuffle(fragments)
    lost_count = len(fragments) // 2
    remaining = fragments[lost_count:]
    
    recovered = DNAResilience.recover_from_fragments(remaining)
    success = recovered == data
    
    return success, lost_count, len(fragments)

def run_benchmark():
    print("=" * 60)
    print("🚀 Rain Kernel Compression Benchmark v0.1")
    print("=" * 60 + "\n")
    
    raw_data = generate_ai_log_sample()
    raw_json = json.dumps(raw_data).encode('utf-8')
    
    # Rain Kernel
    gene = DataCodec.ingest(raw_data)
    gene_json = json.dumps(gene).encode('utf-8')
    
    # GZIP
    gzip_data = gzip.compress(raw_json)
    
    ratio_kernel = SemanticCompressor.calculate_ratio(len(raw_json), len(gene_json))
    ratio_gzip = SemanticCompressor.calculate_ratio(len(raw_json), len(gzip_data))
    
    print("📊 COMPRESSION RESULTS (IA Logs - 100 entries)")
    print("-" * 60)
    print(f"📦 Original (JSON):   {len(raw_json):>10,} bytes")
    print(f"📦 GZIP (Standard):   {len(gzip_data):>10,} bytes ({ratio_gzip:>5.1f}% reduction)")
    print(f"🧬 Rain Kernel:       {len(gene_json):>10,} bytes ({ratio_kernel:>5.1f}% reduction)")
    print(f"\n💡 Semantic Advantage: {ratio_kernel - ratio_gzip:>5.1f}% extra vs GZIP")
    print(f"📈 Compression Factor: {len(raw_json) / len(gene_json):>5.2f}x")
    
    print("\n" + "=" * 60)
    print("🛡️ RESILIENCE TEST (DNA-Inspired Recovery)")
    print("-" * 60)
    
    success, lost, total = test_resilience()
    print(f"🔴 Fragments Lost:    {lost}/{total} ({(lost/total)*100:.0f}%)")
    print(f"🟢 Recovery Success:  {'✅ YES' if success else '❌ NO'}")
    print(f"💪 Data Recovered:    {'100%' if success else 'Partial'}")
    
    print("\n" + "=" * 60)
    print("✅ Benchmark Complete - Rain Kernel v0.1")
    print("=" * 60)

if __name__ == "__main__":
    run_benchmark()
