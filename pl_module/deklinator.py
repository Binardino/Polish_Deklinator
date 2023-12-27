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

    @staticmethod
    @check_gender_number
    def mianownik(word, type, gender, number):
        return word
    
    @staticmethod
    @check_gender_number
    def dopelniacz(word, type, gender, number):            
        if word.gender == 'feminine' and  word.number == 'singular':
            if word[-1] == 'ć':
                return word[:-2] + 'ci'
      #      if word[-1] == 'ż':
      #          return word[:-2] + 'ci'
            if word[-2:] in ['ka', 'ga']:
                return word[-1:] + 'i'
            else:
                return word[:-1] + 'y'
            
        #masculine case
        elif word.gender == 'masculine'  and  word.number == 'singular':
        
        elif word.gender == 'masculine'  and  word.number == 'plural':
            if word in ["wiersz", "notariusz", "biegacz", "klucz"]:
                return word + 'y'
            else :
                return word + 'ów'
        
        #neutral case            
        elif word.gender == 'neutral' and  word.number == 'plural':
            if word[-2:] == 'ko':
                return word[:-2] + 'ek'
            if word[-2:] == 'ło':
                return word[:-2] + 'eł'
            if word[-2:] == 'no':
                return word[:-2] + 'ien'
            if word[-1] == 'ę':
                return word[:-1] + 'ąt'            
            else :
                return word[:-1]
