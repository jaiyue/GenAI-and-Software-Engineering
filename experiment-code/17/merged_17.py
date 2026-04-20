from typing import List

def parse_music(music_string: str) -> List[int]:
    """Parse ASCII music tokens into beat lengths."""
    mapping = {'o': 4, 'o|': 2, '.|': 1}
    if not music_string or music_string.strip() == '':
        return []
    tokens = music_string.split()
    result: List[int] = []
    for t in tokens:
        if t in mapping:
            result.append(mapping[t])
            continue
        # allow tokens with accidental surrounding characters by filtering to valid note chars
        cleaned = ''.join(ch for ch in t if ch in 'o.|')
        if cleaned in mapping:
            result.append(mapping[cleaned])
        else:
            raise ValueError(f"Unknown note token: {t}")
    return result

