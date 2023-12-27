class PolishCases:
    def check_gender_number(func):
        def wrapper(word, gender, type, number, *args, **kwargs):
            # Validate gender and number
            if word.gender not in ['feminine', 'masculine', 'neuter']:
                return "Please input a relevant gender: feminine, masculine, or neuter"
            if word.number not in ['singular', 'plural']:
                return "Please input a relevant number: singular or plural"

            # Call the original function if validation passes
            return func(word, gender, number, *args, **kwargs)

        return wrapper
