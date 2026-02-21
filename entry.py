import sys
import json
from core.codec import DataCodec
from core.integrity import IntegrityEngine
from core.expression import GeneExpression

def main():
    if len(sys.argv) < 2:
        print("Usage: python entry.py <command> [data]")
        print("Commands: encode, decode, express")
        return

    command = sys.argv[1]
    
    if command == "encode":
        data = sys.argv[2] if len(sys.argv) > 2 else "Rain Kernel Example"
        gene = DataCodec.ingest(data)
        print(json.dumps(gene, indent=2))
        
    elif command == "decode":
        print("Decode via API recommended for v0.1")
        print("Example: from core.codec import DataCodec; DataCodec.express(gene)")
        
    elif command == "express":
        gene = {"v": "0.1", "m": "repeat", "s": "Hello ", "sig": "test"}
        result = GeneExpression.execute(gene, {"count": 3})
        print(f"Expressed: {result}")
        
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
