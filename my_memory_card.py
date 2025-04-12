#создай приложение для запоминания информации
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QGroupBox, QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QButtonGroup
from random import shuffle 

app = QApplication([])
main_win = QWidget()


class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии','Португальский','Английский','Испанский','Бразильский'))
question_list.append(Question('Какого цвета нет на флаге России','Зеленый','Красный','Белый','Синий'))
question_list.append(Question('Национальная хижина якутов','Ураса','Юрта','Иглу','Хата'))
main_win.setWindowTitle('Memory Card')
btn_ok = QPushButton('Ответить')
lb_question = QLabel('Какой национальности не существует?')
radio_group_box = QGroupBox('Варианты ответов')
rb1 = QRadioButton('Энцы')
rb2 = QRadioButton('Смурфы')
rb3 = QRadioButton('Чулымцы')
rb4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rb1)
layout_ans2.addWidget(rb2)
layout_ans3.addWidget(rb3)
layout_ans3.addWidget(rb4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

radio_group_box.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addStretch(1)
layout_line1.addWidget(btn_ok, stretch=2)
layout_line1.addStretch(1)
layout_line2.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(radio_group_box)

answer_groupbox = QGroupBox('Результат теста')
lb_result = QLabel('Правильно|Неправильно')
lb_correct = QLabel('Правильный ответ: ')
layout_result = QVBoxLayout()
layout_result.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(lb_correct, alignment=Qt.AlignHCenter)

answer_groupbox.setLayout(layout_result)
answer_groupbox.hide()

main_layout = QVBoxLayout()
main_layout.addLayout(layout_line2, stretch=2)
main_layout.addLayout(layout_line3, stretch=8)
main_layout.addStretch(1)
main_layout.addLayout(layout_line1, stretch=1)
main_layout.addStretch(1)
main_layout.setSpacing(5)
main_win.setLayout(main_layout)

answers = [rb1, rb2, rb3, rb4]
button_group = QButtonGroup()
button_group.addButton(rb1)
button_group.addButton(rb2)
button_group.addButton(rb3)
button_group.addButton(rb4)

def show_result():
    radio_group_box.hide()
    answer_groupbox.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    radio_group_box.show()
    answer_groupbox.hide()
    btn_ok.setText('Ответить')
    button_group.setExclusive(False)
    for answer in answers:
        answer.setChecked(False)
    button_group.setExclusive(True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_correct.setText(f'Правильный ответ: {q.right_answer}')
    show_question()
def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or  answers[2].isChecked() or  answers[3].isChecked():
            show_correct('Неверно')

def next_question():
    main_win.cur_question = main_win.cur_question + 1
    if main_win.cur_question >=len(question_list):
        main_win.cur_question = 0
    q=question_list[main_win.cur_question]
    ask(q)

def click_ok():
    if btn_ok.text()=='Ответить':
        check_answer()
    else:
        next_question()
    
main_win.cur_question = -1

btn_ok.clicked.connect(click_ok)
main_win.show()
app.exec()