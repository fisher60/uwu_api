import functools
import random
import re
import string

UWU_WORDS = {
    "fi": "fwi",
    "l": "w",
    "r": "w",
    "some": "sum",
    "th": "d",
    "thing": "fing",
    "tho": "fo",
    "you're": "yuw'we",
    "your": "yur",
    "you": "yuw",
}


def _replace_many(
        sentence: str,
        replacements: dict,
        *,
        ignore_case: bool = False,
        match_case: bool = False,
) -> str:
    """
    Replaces multiple substrings in a string given a mapping of strings.
    By default replaces long strings before short strings, and lowercase before uppercase.
    Example:
        var = replace_many("This is a sentence", {"is": "was", "This": "That"})
        assert var == "That was a sentence"
    If `ignore_case` is given, does a case insensitive match.
    Example:
        var = replace_many("THIS is a sentence", {"IS": "was", "tHiS": "That"}, ignore_case=True)
        assert var == "That was a sentence"
    If `match_case` is given, matches the case of the replacement with the replaced word.
    Example:
        var = replace_many(
            "This IS a sentence", {"is": "was", "this": "that"}, ignore_case=True, match_case=True
        )
        assert var == "That WAS a sentence"
    This is shamelessly stolen from Python Discord's seasonalbot
    https://github.com/CharlieADavies/seasonalbot/blob/master/bot/utils/__init__.py
    """
    if ignore_case:
        replacements = dict(
            (word.lower(), replacement) for word, replacement in replacements.items()
        )

    words_to_replace = sorted(replacements, key=lambda s: (-len(s), s))

    # Join and compile words to replace into a regex
    pattern = "|".join(re.escape(word) for word in words_to_replace)
    regex = re.compile(pattern, re.I if ignore_case else 0)

    def _repl(match: re.Match) -> str:
        """Returns replacement depending on `ignore_case` and `match_case`."""
        word = match.group(0)
        replacement = replacements[word.lower() if ignore_case else word]

        if not match_case:
            return replacement

        # Clean punctuation from word so string methods work
        cleaned_word = word.translate(str.maketrans("", "", string.punctuation))
        if cleaned_word.isupper():
            return replacement.upper()

        elif cleaned_word[0].isupper():
            return replacement.capitalize()

        else:
            return replacement.lower()

    return regex.sub(_repl, sentence)


def stutter(s, rate=0.5):
    """Adds repetition separated by dashes at the start of each word in a string."""

    def _stutter(w):
        while random.random() < rate:
            w = w[0] + '-' + w
        return w
    return ' '.join(map(_stutter, s.split(' ')))


def to_uwu(text: str) -> str:
    """
            Converts a given `text` into it's uwu equivalent.
            This is shamelessly stolen from Python Discord's seasonalbot.
            https://github.com/python-discord/seasonalbot/blob/master/bot/exts/evergreen/fun.py
            """
    conversion_func = functools.partial(
        _replace_many, replacements=UWU_WORDS, ignore_case=True, match_case=True
    )
    converted_text = conversion_func(text)

    # Don't put >>> if only embed present
    if converted_text:
        converted_text = f"{converted_text.lstrip('> ')}"
    return converted_text
