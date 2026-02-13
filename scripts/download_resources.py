"""
Download required NLP resources
"""
import spacy
import subprocess
import nltk

def download_spacy_model():
    """Download spaCy model"""
    print("\nDownloading spaCy model...")
    try:
        subprocess.run([
            "python", "-m", "spacy", "download", "en_core_web_sm"
        ], check=True)
        
        
        print("✓ Downloaded en_core_web_sm")
    except Exception as e:
        print(f"✗ Failed to download spaCy model: {e}")

def download_nltk_data():
    """Download NLTK data"""
    print("\nDownloading NLTK data...")
    resources = ['stopwords', 'punkt']
    for res in resources:
        nltk.download(res)
        print(f"✓ Downloaded {res}")

if __name__ == "__main__":
    download_spacy_model()
    download_nltk_data()
    print("\n✅ All NLP resources downloaded successfully!")