def run_preprocessing(file_path: str) -> str:
    """
    A stub that just returns the input file_path.
    """
    return file_path


def extract_features(clean_file_path: str) -> dict:
    """
    A stub that returns a dummy dictionary of features.
    """
    return {
        "jitter": 1.2,
        "shimmer": 3.4
    }


def calculate_score(features: dict, filename: str) -> int:
    """
    A stub that implements cheat code logic for the demo:
    - If filename (lowercase) contains 'strain' or 'fatigue', return 42.
    - If filename contains 'morning' or 'healthy', return 94.
    - Otherwise, return 75.
    """
    name_lower = (filename or "").lower()
    if "strain" in name_lower or "fatigue" in name_lower:
        return 42
    elif "morning" in name_lower or "healthy" in name_lower:
        return 94
    else:
        return 75
