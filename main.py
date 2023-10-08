from PyQt5.QtWidgets import*

import json

try:
    with open("notes_data.json", "r", encoding = "utf - 8") as file:
        notes = json.load(file)
except:
    notes = {}




app = QApplication([])
window = QWidget()
window.resize(900, 700)

armature = QLabel("Список заміток")
bulochka = QLabel("Список тегів")
textplace = QTextEdit()
textsearch = QLineEdit()
Napoleon0 = QPushButton("Створити замітку")
Napoleon1 = QPushButton("Видалити замітку")
Napoleon2 = QPushButton("Зберегти замітку")
Napoleon3 = QPushButton("Додати до замітки")
Napoleon4 = QPushButton("Відкріпити від замітки")
Napoleon5 = QPushButton("Шукати замітки по тегу")
algebra = QListWidget()
geometrydash = QListWidget()

mainline = QHBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()
lineer1 = QHBoxLayout()
lineer2 = QHBoxLayout()

mainline.addLayout(line1)
mainline.addLayout(line2)

line1.addWidget(textplace)
line2.addWidget(armature)
line2.addWidget(algebra)
lineer1.addWidget(Napoleon0)
lineer1.addWidget(Napoleon1)
line2.addLayout(lineer1)
line2.addWidget(Napoleon2)
line2.addWidget(bulochka)
line2.addWidget(geometrydash)
line2.addWidget(textsearch)
lineer2.addWidget(Napoleon3)
lineer2.addWidget(Napoleon4)
line2.addLayout(lineer2)
line2.addWidget(Napoleon5)
window.setLayout(mainline)

def save_note():
    if algebra.selectedItems():
        key = algebra.selectedItems()[0].text()
        notes[key]["текст"] = textplace.toPlainText()
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)
    else:
        print("Замітка для збереження не вибрана!")

def show_note():
    # отримуємо текст із замітки з виділеною назвою та відображаємо її в полі редагування
    key = algebra.selectedItems()[0].text()
    print(key)
    textplace.setText(notes[key]["текст"])
    geometrydash.clear()
    geometrydash.addItems(notes[key]["теги"])

def del_note():
    if algebra.selectedItems():
        key = algebra.selectedItems()[0].text()
        notes.pop(key)
        algebra.clear()
        geometrydash.clear()
        textplace.clear()
        algebra.addItems(notes)
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False, indent=4)

    else:
        print("Замітка для вилучення не обрана!")
def add_note():
    note_name, ok = QInputDialog.getText(window, "Додати замітку", "Назва замітки: ")
    if ok and note_name != "":
        notes[note_name] = {
            "текст": "",
            "теги": []
        }
        algebra.clear()
        textplace.clear()
        algebra.addItems(notes)
        with open("notes_data.json", "w", encoding = "utf - 8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)


Napoleon0.clicked.connect(add_note)
Napoleon1.clicked.connect(del_note)
Napoleon2.clicked.connect(save_note)
algebra.itemClicked.connect(show_note)
algebra.addItems(notes)
window.show()
app.exec()