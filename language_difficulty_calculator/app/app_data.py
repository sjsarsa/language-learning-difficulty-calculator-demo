user_languages = []
languages = ['English', 'Esperanto', 'Finnish', 'French', 'German', 'Italian']
# The values are simplified from hierarchical clustering thresholds
thresholds = {'English': 20,
              'Esperanto': 7,
              'Finnish': 12,
              'French': 2,
              'German': 1,
              'Italian': 5}


def add_user_language(language):
    if language not in user_languages:
        user_languages.append(language)


def remove_user_language(language):
    user_languages.remove(language)


# Here we get language difficulties by using the distance of language thresholds and a list of known language with
# made up scaling, quite horrible but fast to make and does the trick. This is a demo after all.
def get_language_difficulties():
    difficulties = {}
    # Set initial difficulty, this will be divided by two to get max difficulty of 10
    # We add difficulty according to length of known languages so that the difficulty doesn't drop too fast to zero
    for language in languages:
        difficulties[language] = 40 + len(user_languages) * 15
    # Reduce difficulty based on language similarity (cluster distance)
    for language in user_languages:
        for difficulty_key in languages:
            difficulties[difficulty_key] = \
                difficulties.get(difficulty_key) \
                - (340 - abs(thresholds.get(language) - thresholds.get(difficulty_key)) * 8) / 10
    # Divide all the difficulties to get nice rounded max difficulty
    for difficulty_key in languages:
        difficulties[difficulty_key] = max(round(difficulties.get(difficulty_key) / 4, 1), 1)
    # Set known languages' difficulties to zero
    for language in user_languages:
        difficulties[language] = 0
    return difficulties
