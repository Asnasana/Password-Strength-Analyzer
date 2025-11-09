# Password Strength Analyzer and Wordlist Generator

This web application analyzes password strength based on length, complexity, and predictability, and generates custom wordlists for password-cracking simulations or audit testing.

## Features

### Password Strength Analysis
- **Length**: Checks password length.
- **Complexity**: Evaluates variety of character types (uppercase, lowercase, digits, special characters).
- **Predictability**: Detects common passwords, patterns, and sequences.
- **Entropy**: Calculates password entropy.
- **Feedback**: Provides suggestions for improvement.
- **Crack Time Estimation**: Rough estimate of time to crack via brute force.
- **Visual Score Bar**: Color-coded progress bar indicating strength.

### Wordlist Generation
- Generates custom wordlists from base words.
- Supports rules like:
  - Appending/prepending numbers (e.g., years).
  - Leetspeak substitutions.
  - Adding special characters.

## Installation

1. Ensure Python 3.x is installed.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Web Interface
1. Run the Flask app:
   ```
   python app.py
   ```
2. Open a web browser and navigate to `http://127.0.0.1:5000`.
3. Use the GUI to analyze passwords or generate wordlists.

### CLI Usage (Alternative)
Run the script directly:
```
python password_analyzer.py
```

### Example Web Interaction
- Enter a password like "MySecurePass123!" in the analysis section to see detailed metrics.
- Input base words like "password, admin, user" and select rules to generate a wordlist.

## Project Structure

- `app.py`: Flask web application with routes for analysis and generation.
- `password_analyzer.py`: Core logic for password analysis and wordlist generation.
- `templates/index.html`: HTML template for the web interface.
- `requirements.txt`: Python dependencies.
- `README.md`: This documentation.

## Classes

### PasswordAnalyzer
- `analyze_strength(password)`: Returns a dict with analysis metrics.

### WordlistGenerator
- `generate_wordlist(base_words, rules)`: Generates wordlist based on rules.

## Customization

- Modify `common_passwords` in `PasswordAnalyzer` for custom weak password lists.
- Adjust leetspeak mappings in `WordlistGenerator`.
- Extend rules in `generate_wordlist` for more variations.

## Disclaimer

This tool is for educational and security auditing purposes only. Use responsibly and ethically.
