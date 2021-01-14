from xml.dom import minidom


class XMLDriver(object):
    def __init__(self, path):
        self._doc = minidom.parse(path)

# Красивенький принт
    def nice_print(self, value):
        print('>' * 50)
        print(value)

# Метод вывода навания теста
    def get_name(self):
        root = self._doc.getElementsByTagName('test')[0]
        name = root.attributes['name'].value
        self.nice_print(name)

# Сдесь я обьеденила в один метод вывод вопроса и вариантов его отвата. Просто, как по мне, это логичней)
    def get_question(self, number: str):
        questions = self._doc.getElementsByTagName('question')
        for q in questions:
            if q.attributes['number'].value == number:
                answers = q.getElementsByTagName('answer')
                result = f"Вопрос {q.attributes['number'].value}. {q.attributes['text'].value}"
                self.nice_print(result)

                # Вот эта часть отвечает за вывод вариантов для вопроса, который запрашиваеться
                for a in answers:
                    result2 = f"->>> {a.attributes['number'].value}. {a.attributes['text'].value}"
                    print(result2)

    """
    После многочисленых попыток, я наконец то сделала рабочий метод для 
    ввода варианта ответа и его проверки. Наш метод принимает новер вопроса,
    который идет по умолчанию в main и номер варианта ответа. 
    
    Далее идет проверка на правильность ести тэг correct имеет значение True.
    И результат сразу выводиться в консоль.
    
    Возможно его можно написать попроще и покороче, но я художник, я так вижу)
    """
    def set_answer(self, question_number, answer_number):
        questions = self._doc.getElementsByTagName('question')
        for q in questions:
            if q.attributes['number'].value == question_number:
                answers = self._doc.getElementsByTagName('answer')
                for a in answers:
                    if a.attributes['number'].value == answer_number:
                        if a.attributes['correct'].value == "True":
                            result = f"Ответ {a.attributes['number'].value} правильный. Ураа!!!"
                            self.nice_print(result)
                        else:
                            print(f"Ответ {a.attributes['number'].value} НЕ правильный. Плак-плак( ")


    def final(self):
        self.nice_print('Текст окончен!')
