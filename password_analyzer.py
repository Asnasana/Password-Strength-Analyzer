import itertools
import string
import re
import math

class PasswordAnalyzer:
    def __init__(self):
        self.common_passwords = {'password', '123456', 'qwerty', 'admin', 'letmein', 'welcome'}

    def analyze_strength(self, password):
        """
        Analyze password strength based on length, complexity, and predictability.
        Returns a dictionary with score, feedback, and detailed metrics.
        """
        length = len(password)
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[^A-Za-z0-9]', password))

        # Complexity score: variety of character types
        complexity_score = sum([has_upper, has_lower, has_digit, has_special]) / 4.0

        # Predictability score: higher means more predictable (weaker)
        predictability = 0.0
        if password.lower() in self.common_passwords:
            predictability += 0.5
        if re.search(r'\d{4}$', password):  # Ends with 4 digits (e.g., year)
            predictability += 0.2
        if re.search(r'123|abc|qwe|asd|zxc', password.lower()):
            predictability += 0.3
        if length < 8:
            predictability += 0.2

        # Entropy calculation (simplified)
        char_set_size = 0
        if has_lower: char_set_size += 26
        if has_upper: char_set_size += 26
        if has_digit: char_set_size += 10
        if has_special: char_set_size += 32  # Approximate
        entropy = length * math.log2(char_set_size) if char_set_size > 0 else 0

        # Overall score: combine factors
        overall_score = (entropy / 100.0 * 0.4) + (complexity_score * 0.3) + ((1 - predictability) * 0.3)
        overall_score = min(1.0, max(0.0, overall_score))

        # Feedback
        feedback = []
        if length < 8:
            feedback.append("Password is too short. Use at least 8 characters.")
        if not (has_upper and has_lower):
            feedback.append("Include both uppercase and lowercase letters.")
        if not has_digit:
            feedback.append("Add numbers for better strength.")
        if not has_special:
            feedback.append("Include special characters like !@#$%.")
        if predictability > 0.5:
            feedback.append("Avoid common patterns or words.")

        # Estimated crack time (very rough approximation)
        crack_time = self._estimate_crack_time(length, char_set_size)

        return {
            'score': overall_score,
            'length': length,
            'complexity': complexity_score,
            'predictability': predictability,
            'entropy': entropy,
            'feedback': feedback,
            'crack_time': crack_time
        }

    def _estimate_crack_time(self, length, char_set_size):
        """Rough estimate of crack time in seconds for offline attack."""
        attempts_per_second = 1e10  # Hypothetical
        total_combinations = char_set_size ** length
        time_seconds = total_combinations / attempts_per_second
        if time_seconds < 60:
            return f"{time_seconds:.2f} seconds"
        elif time_seconds < 3600:
            return f"{time_seconds / 60:.2f} minutes"
        elif time_seconds < 86400:
            return f"{time_seconds / 3600:.2f} hours"
        elif time_seconds < 31536000:
            return f"{time_seconds / 86400:.2f} days"
        else:
            return f"{time_seconds / 31536000:.2f} years"

class WordlistGenerator:
    def __init__(self):
        self.leetspeak = {
            'a': ['4', '@'],
            'e': ['3'],
            'i': ['1', '!'],
            'o': ['0'],
            's': ['5', '$'],
            't': ['7'],
            'l': ['1']
        }

    def generate_wordlist(self, base_words, rules=None):
        """
        Generate a custom wordlist based on base words and rules.
        Rules can include: 'append_numbers', 'prepend_numbers', 'leetspeak', 'special_chars'
        """
        if rules is None:
            rules = ['append_numbers']

        wordlist = set()

        for word in base_words:
            variations = [word]

            if 'leetspeak' in rules:
                variations = self._apply_leetspeak(variations)

            if 'append_numbers' in rules:
                variations = self._append_numbers(variations)

            if 'prepend_numbers' in rules:
                variations = self._prepend_numbers(variations)

            if 'special_chars' in rules:
                variations = self._add_special_chars(variations)

            wordlist.update(variations)

        return list(wordlist)

    def _apply_leetspeak(self, words):
        new_words = []
        for word in words:
            # Simple leetspeak replacement
            leet_word = word.lower()
            for char, replacements in self.leetspeak.items():
                for rep in replacements:
                    leet_word = leet_word.replace(char, rep)
            new_words.append(leet_word)
        return new_words

    def _append_numbers(self, words):
        new_words = []
        for word in words:
            for num in range(1000, 2024):  # Years or common numbers
                new_words.append(word + str(num))
        return new_words

    def _prepend_numbers(self, words):
        new_words = []
        for word in words:
            for num in range(1000, 2024):
                new_words.append(str(num) + word)
        return new_words

    def _add_special_chars(self, words):
        new_words = []
        specials = ['!', '@', '#', '$', '%', '&', '*']
        for word in words:
            for special in specials:
                new_words.append(word + special)
                new_words.append(special + word)
        return new_words

def main():
    analyzer = PasswordAnalyzer()
    generator = WordlistGenerator()

    # Example usage
    password = input("Enter a password to analyze: ")
    analysis = analyzer.analyze_strength(password)
    print(f"Password Strength Analysis:")
    print(f"Score: {analysis['score']:.2f}")
    print(f"Length: {analysis['length']}")
    print(f"Complexity: {analysis['complexity']:.2f}")
    print(f"Predictability: {analysis['predictability']:.2f}")
    print(f"Estimated Crack Time: {analysis['crack_time']}")
    print(f"Feedback: {analysis['feedback']}")

    # Generate wordlist
    base_words = ['password', 'admin', 'user']
    rules = ['append_numbers', 'leetspeak']
    wordlist = generator.generate_wordlist(base_words, rules)
    print(f"\nGenerated {len(wordlist)} potential passwords.")
    print("Sample:", wordlist[:10])

if __name__ == "__main__":
    main()
