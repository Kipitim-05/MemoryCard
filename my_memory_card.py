#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('MemoryCard')
main_win.resize(600, 400)

question = QLabel('Какой национальности не существует')
btn = QPushButton('Ответить')

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1) 

AnsGroupBox = QGroupBox('Результат теста')
is_right = QLabel('Правильно/Неправильно')
right_answer = QLabel('Правильный ответ')
ans_layout = QVBoxLayout()
ans_layout.addWidget( is_right)
ans_layout.addWidget(right_answer, alignment = Qt.AlignCenter)
AnsGroupBox.setLayout(ans_layout)
AnsGroupBox.hide()

layout=QVBoxLayout()
layout.addWidget(question, alignment = Qt.AlignCenter)
layout.addWidget(RadioGroupBox)
layout.addWidget(AnsGroupBox)
layout.addWidget(btn, alignment = Qt.AlignCenter)
main_win.setLayout(layout)



class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q):
    question.setText(q.question)
    rbtn_1.setText(q.right_answer)
    rbtn_2.setText(q.wrong1)
    rbtn_3.setText(q.wrong2)
    rbtn_4.setText(q.wrong3)

question_list = list()
question_list.append(Question(
    'Государственный язык Бразилии',
     'Португальский',
     'Испанский', 'Итальянский', 'Бразильский'))

question_list.append(Question(
    'День народного единства отмечается',
     '4 ноября',
     '12 июня', '7 октября', '3 сентября')) 

question_list.append(Question(
    'Когда начинается Пасха?',
    '20 февраля',
    '10 апреля', '7 сентября', '5 марта'))

question_list.append(Question(
    'Когда распался СССР ?',
    '1991',
    '1865', '1490', '1394'))

question_list.append(Question(
    'Столица Польши',
    'Варшава',
    'Берлин', 'Осло', 'Лисабон'))

from random import randint
main_win.cur = -1
total = 0
score = 0

def next_question():
    global total
    total += 1
    main_win.cur = randint(0, len(question_list)-1)
    #if main_win.cur == len(question_list):
    #    main_win.cur = 0
    q = question_list[main_win.cur]
    ask(q)

AnsGroupBox.hide()

def check_answer():
    global total, score
    if rbtn_1.isChecked():
        is_right.setText('Правильно')
        right_answer.setText(rbtn_1.text())
        score +=1
    else:
        is_right.setText('Не правильно')
        right_answer.setText(rbtn_1.text())
    print('Статистика:')
    print('Задано вопросов:', total)
    print('Правильных ответов:', score)
    print('Рейтинг сотрудника:', score/total, '%')

next_question()     

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')

RG = QButtonGroup()
RG.addButton(rbtn_1)
RG.addButton(rbtn_2)
RG.addButton(rbtn_3)
RG.addButton(rbtn_4)

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn.setText('Ответить')
    RG.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RG.setExclusive(True)

def btn_start():
    if btn.text()== 'Ответить':
        show_result()
        check_answer()
    
    else:
        show_question()
        next_question()   

btn.clicked.connect(btn_start)




main_win.show()
app.exec_()