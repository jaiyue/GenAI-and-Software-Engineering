Running a repository search to find where to implement remove_vowels so the minimal edit can be made; reporting intent "Editing code" with the search.

def remove_vowels(text):
    vowels = set("aeiouAEIOU")
    return "".join(ch for ch in text if ch not in vowels)

