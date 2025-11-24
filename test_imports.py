import sys
import os

# Add the backend directory to the path
sys.path.insert(0, os.path.dirname(__file__))

# Test imports
try:
    print("Testing imports...")
    from backend.services.llm_factory import LLMFactory
    print("✓ LLMFactory imported")
    
    from backend.services.vector_store import VectorStoreService
    print("✓ VectorStoreService imported")
    
    from backend.services.rag_agent import RAGAgent
    print("✓ RAGAgent imported")
    
    # Test LLM initialization
    print("\nTesting LLM initialization...")
    os.environ["GEMINI_API_KEY"] = "test_key"
    llm = LLMFactory.get_llm()
    print(f"✓ LLM initialized: {type(llm)}")
    
    print("\n✅ All imports successful!")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()
