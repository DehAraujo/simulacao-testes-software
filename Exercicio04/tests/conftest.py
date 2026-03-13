import sys
from pathlib import Path

# Add parent directory to Python path so imports like "from Exercicio04.src..." work
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
