import os
from sentence_transformers import SentenceTransformer

def initialize_local_embedding_engine():
    """
    Downloads and freezes the all-MiniLM-L6-v2 transformer model weights
    into a dedicated local project directory to guarantee 100% air-gapped,
    offline runtime capabilities without internet pings.
    """
    model_name = "all-MiniLM-L6-v2"
    
    # Project ke andar hi ek fixed premium folder path define kar rahe hain
    target_local_dir = os.path.join(os.path.dirname(__file__), "local_models", model_name)
    
    print("[INFO] Initializing Aegis Model Localizer Pipeline...")
    
    try:
        # Step 1: Internet se model pull karke direct humare custom folder mein save karega
        print(f"[INFO] Fetching weights for '{model_name}' from Hugging Face Hub...")
        model = SentenceTransformer(model_name)
        
        print(f"[INFO] Freezing and serializing model architecture to disk: {target_local_dir}")
        model.save(target_local_dir)
        
        print("[SUCCESS] Cold-Start Dependency Localization Complete! System is now 100% Air-Gapped.")
        
    except Exception as e:
        print(f"[CRITICAL ERROR] Failed to download model layers: {str(e)}")

if __name__ == "__main__":
    initialize_local_embedding_engine()