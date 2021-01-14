from drivers import *

"""
Разработайте на основе XML-файла тест по основам 
программирования на языĸе Python
"""


if __name__ == '__main__':
    driver = XMLDriver('data.xml')
    driver.get_name()

    driver.get_question('1')
    print('>' * 50)
    driver.set_answer('1', str(input('Введите номер ответа-> ')))

    driver.get_question('2')
    print('>' * 50)
    driver.set_answer('2', str(input('Введите номер ответа-> ')))

    driver.get_question('3')
    print('>' * 50)
    driver.set_answer('3', str(input('Введите номер ответа-> ')))

    driver.get_question('4')
    print('>' * 50)
    driver.set_answer('4', str(input('Введите номер ответа-> ')))

    driver.get_question('5')
    print('>' * 50)
    driver.set_answer('5', str(input('Введите номер ответа-> ')))

    driver.get_question('6')
    print('>' * 50)
    driver.set_answer('6', str(input('Введите номер ответа-> ')))

    driver.get_question('7')
    print('>' * 50)
    driver.set_answer('7', str(input('Введите номер ответа-> ')))

    driver.get_question('8')
    print('>' * 50)
    driver.set_answer('8', str(input('Введите номер ответа-> ')))

    driver.get_question('9')
    print('>' * 50)
    driver.set_answer('9', str(input('Введите номер ответа-> ')))

    driver.get_question('10')
    print('>' * 50)
    driver.set_answer('10', str(input('Введите номер ответа-> ')))
