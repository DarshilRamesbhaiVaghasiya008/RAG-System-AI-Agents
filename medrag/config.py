from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).parent.parent

def env_int(name, default=False):
    return int(os.getenv(name, default))

def env_bool(name, default = False):
    return os.getenv(name, default).lower() in ("true", "1", "t")

DATA_DIR = Path(os.getenv("MEDRAG_DATA_DIR", PROJECT_ROOT / "data"))
CHROMA_DIR = Path(os.getenv("MEDRAG_CHROMA_DIR", PROJECT_ROOT / "chroma_db"))
REGISTRY_DB = Path(os.getenv("MEDRAG_REGISTRY_DB", PROJECT_ROOT / "registry.sqlite"))
EMBEDDING_MODEL = os.getenv("MEDRAG_EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
CHUNK_SIZE = env_int("MEDRAG_CHUNK_SIZE", 1000)
CHUNK_OVERLAP = env_int("MEDRAG_CHUNK_OVERLAP", 150)
TOP_K = env_int("MEDRAG_TOP_K", 5)
LLM_MODEL = os.getenv("MEDRAG_LLM_MODEL", "llama3.1:8b")
OLLAMA_URL = os.getenv("MEDRAG_OLLAMA_URL", "http://localhost:11434")