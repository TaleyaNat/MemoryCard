from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout, QHBoxLayout,QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, randint

#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400,300)

#создание виджетов
lbl_question = QLabel('Вопрос')
RadioGroup = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Ответ 1')
rbtn_2 = QRadioButton('Ответ 2')
rbtn_3 = QRadioButton('Ответ 3')
rbtn_4 = QRadioButton('Ответ 4')
btn_ok = QPushButton('Ответить')

AnswerGroup = QGroupBox('Результат')
lbl_result = QLabel('Верно\Неверно')
lbl_correct = QLabel('Правильный ответ')

ButtonGroup = QButtonGroup()
ButtonGroup.addButton(rbtn_1)
ButtonGroup.addButton(rbtn_2)
ButtonGroup.addButton(rbtn_3)
ButtonGroup.addButton(rbtn_4)

answ = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

#привязка элементов к лэйаутам
row1 = QHBoxLayout()
row1.addWidget(rbtn_1)
row1.addWidget(rbtn_2)

row2 = QHBoxLayout()
row2.addWidget(rbtn_3)
row2.addWidget(rbtn_4)

col = QVBoxLayout()
col.addLayout(row1)
col.addLayout(row2)
RadioGroup.setLayout(col)

col1 = QVBoxLayout()
col1.addWidget(lbl_result, alignment=Qt.AlignLeft)
col1.addWidget(lbl_correct, alignment=Qt.AlignCenter)
AnswerGroup.setLayout(col1)
AnswerGroup.hide()

main_layout = QVBoxLayout()
main_layout.setSpacing(15)
main_layout.addWidget(lbl_question, alignment=Qt.AlignCenter, stretch= 1)
main_layout.addWidget(RadioGroup,stretch= 2)
main_layout.addWidget(AnswerGroup,stretch= 2)
main_layout.addWidget(btn_ok)

main_win.setLayout(main_layout)

class Question():
    def __init__(self, q, r, w1,w2,w3):
        self.question = q
        self.r_answer = r
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3

question_list = []
Q = Question('Как праздник Комоедицы называется сейчас?', 'Масленица', 'Пасха', 'Яблочный спас', 'Медовый спас' )
question_list.append(Q)
Q = Question('Когда славяне праздновали Велесову ночь', '31 октября', '1 сентбяря', '8 июля', '1 января')
question_list.append(Q)
Q = Question('Что НЕ делают в день Ивана Купала', 'наряжают ёлку', 'ищут клады', 'ищут цветок папоротника', 'прыгают через костер' )
question_list.append(Q)

def ShowResult():
    RadioGroup.hide()
    AnswerGroup.show()
    btn_ok.setText("Следующий вопрос")

def ShowQuestion():
    num = randint(0, len(question_list)-1)
    ask(question_list[num])
    RadioGroup.show()
    AnswerGroup.hide()
    btn_ok.setText("Ответить")
    ButtonGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    ButtonGroup.setExclusive(True)

def ask(q):
    shuffle(answ)
    lbl_question.setText(q.question)
    lbl_correct.setText(q.r_answer)
    answ[0].setText(q.r_answer)
    answ[1].setText(q.wrong1)
    answ[2].setText(q.wrong2)
    answ[3].setText(q.wrong3)

def checkAnswer():
    if btn_ok.text() == 'Ответить':
        if answ[0].isChecked():
            lbl_result.setText('Совершенно верно!')
        else:
            lbl_result.setText("Неверно!")
        ShowResult()
    else:
        ShowQuestion()


num = randint(0, len(question_list)-1)
ask(question_list[num])

btn_ok.clicked.connect(checkAnswer)

#запуск приложения
main_win.show()
app.exec_()
























# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (QApplication, QLabel, 
#         QPushButton, QRadioButton, QWidget, 
#         QGroupBox, QButtonGroup,
#         QVBoxLayout, QHBoxLayout)
# from random import shuffle, randint

# class Question():
#         def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
#                 self.question = question
#                 self.right_answer = right_answer
#                 self.wrong1 = wrong1
#                 self.wrong2 = wrong2
#                 self.wrong3 = wrong3


# question_list = []
# Q = Question('Как праздник Комоедицы называется сейчас?', 'Масленица', 'Пасха', 'Яблочный спас', 'Медовый спас' )
# question_list.append(Q)
# Q = Question('Когда славяне праздновали Велесову ночь', '31 октября', '1 сентбяря', '8 июля', '1 января')
# question_list.append(Q)
# Q = Question('Что НЕ делают в день Ивана Купала', 'наряжают ёлку', 'ищут клады', 'ищут цветок папоротника', 'прыгают через костер' )
# question_list.append(Q)


# #Создаем окно приложения
# app = QApplication([])
# main_win = QWidget()
# main_win.setWindowTitle('Memory card')
# main_win.resize(400, 300)

# #Создаем виджеты
# lbl_Question = QLabel('Какой национальсти не существует?')
# btn_Ok = QPushButton('Ответить')

# RadioGroupBox = QGroupBox('Варианты ответов:')
# rbtn_1 = QRadioButton('Смурфы')
# rbtn_2 = QRadioButton('Мордва')
# rbtn_3 = QRadioButton('Татары')
# rbtn_4 = QRadioButton('Якуты')

# answ = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

# RadioGroup = QButtonGroup()
# RadioGroup.addButton(rbtn_1)
# RadioGroup.addButton(rbtn_2)
# RadioGroup.addButton(rbtn_3)
# RadioGroup.addButton(rbtn_4)

# AnswGroupBox = QGroupBox('Результат:')
# lbl_Result = QLabel('Правильно\неправильно')
# lbl_Correct = QLabel('Правильный ответ')

# #Привязка виджетов к лэйаутам
# Layout_answ1 = QVBoxLayout()
# Layout_answ1.addWidget(rbtn_1)
# Layout_answ1.addWidget(rbtn_2)
# Layout_answ2 = QVBoxLayout()
# Layout_answ2.addWidget(rbtn_3)
# Layout_answ2.addWidget(rbtn_4)

# Layout_answ3 = QHBoxLayout()
# Layout_answ3.addLayout(Layout_answ1)
# Layout_answ3.addLayout(Layout_answ2)

# RadioGroupBox.setLayout(Layout_answ3)

# Layout_answ = QVBoxLayout()
# Layout_answ.addWidget(lbl_Result, alignment= (Qt.AlignLeft|Qt.AlignTop))
# Layout_answ.addWidget(lbl_Correct, alignment = (Qt.AlignCenter|Qt.AlignCenter))
# AnswGroupBox.setLayout(Layout_answ)

# row_1 = QHBoxLayout()
# row_1.addWidget(lbl_Question, alignment=Qt.AlignCenter)
# row_2 = QHBoxLayout()
# row_2.addWidget(RadioGroupBox)
# row_2.addWidget(AnswGroupBox)
# row_3 = QHBoxLayout()
# row_3.addStretch(1)
# row_3.addWidget(btn_Ok, stretch = 2)
# row_3.addStretch(1)

# RadioGroupBox.show()
# AnswGroupBox.hide()

# main_layout = QVBoxLayout()
# main_layout.addLayout(row_1, stretch = 1)
# main_layout.addLayout(row_2, stretch = 5)
# main_layout.addLayout(row_3, stretch = 1)
# main_win.setLayout(main_layout)

# #Функции обработки событий
# def show_result():
#         RadioGroupBox.hide()
#         AnswGroupBox.show()
#         btn_Ok.setText('Следующий вопрос')

# def show_question():
#         btn_Ok.setText('Ответить')
#         RadioGroup.setExclusive(False)
#         rbtn_1.setChecked(False)
#         rbtn_2.setChecked(False)
#         rbtn_3.setChecked(False)
#         rbtn_4.setChecked(False)
#         RadioGroup.setExclusive(True)
#         RadioGroupBox.show()
#         AnswGroupBox.hide()

# def start_test():
#         if btn_Ok.text()=="Ответить":
#                 show_correct()
#         else:
#                 quest = randint(0, len(question_list)-1)
#                 ask(question_list[quest])
#                 main_win.total += 1

# def ask(Q:Question):
#         lbl_Question.setText(Q.question)
#         shuffle(answ)
#         answ[0].setText(Q.right_answer)
#         answ[1].setText(Q.wrong1)
#         answ[2].setText(Q.wrong2)
#         answ[3].setText(Q.wrong3)
#         lbl_Correct.setText(Q.right_answer)
#         show_question()

# def show_correct():
#         if answ[0].isChecked():
#                 lbl_Result.setText('Верно!')
#                 main_win.score += 1
#         else:
#                 lbl_Result.setText('Не верно!')
#         show_result()
#         print('Статистика:')
#         print('задано вопросов:', main_win.total)
#         print('правильных ответов:', main_win.score)
#         print('рейтинг:', main_win.score/main_win.total*100, '%')




# #Привязка функций к виджетам
# btn_Ok.clicked.connect(start_test)



# #Запуск приложения
# quest = randint(0, len(question_list)-1)
# ask(question_list[quest])

# main_win.total = 1
# main_win.score = 0

# main_win.show()
# app.exec_()