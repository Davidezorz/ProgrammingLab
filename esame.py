#http://autograding.xyz/

class ExamException(Exception):
    pass

class Diff:

    def __init__ (self, ratio=1):
        if isinstance(ratio, int)==False and isinstance(ratio, float)==False:
            raise ExamException('ratio not int or float')
        elif ratio==0:
            raise ExamException('impossibile dividere per 0')
        elif ratio<0:
            raise ExamException('ratio negativo non valido')
        else:
            self.ratio = ratio

    def compute (self, lista):

        if isinstance(lista, list)==False:
            raise ExamException('compute ha in ingresso una lista')
        
        else:
            diff = []
            prev_data = None

            for item in lista:

                if isinstance(item, int)==False and isinstance(item, float)==False:
                    raise ExamException('un elemento della lista nn è int o float')
                elif len(lista)<2:
                    raise ExamException("la lunghezza della lista dev'essere almeno pari a 2")
                   
                else:
                    if prev_data == None:
                        prev_data = item

                    else:
                        a = item - prev_data
                        diff.append(a/self.ratio)
                        prev_data = item
                
            return diff
