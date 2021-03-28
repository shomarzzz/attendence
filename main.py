import os
import datetime
sub = ["Roll", "English 1st", "English 2nd", "Bangla 1st", "Bangla 2nd", "G.Math", "H.Math", "ICT", "Religion",
       "Physics", "Chemistry", "Biology"]


def text_input():
    with open("rolls.txt") as rolls:
        roll = rolls.readlines()
        lost = roll[1].split(",")
        tc_rolls = [int(i) for i in lost]
        total_rolls = [i for i in range(1, int(roll[0].rstrip("\n"))+1) if i not in tc_rolls]
        return total_rolls


def see_files():
    for root, dirs, files in os.walk(r"C:\Users\Col Khalil\Documents\Zoom"):
        for file in files:
            if file == "meeting_saved_chat.txt":
                k = os.path.join(root, file)
                return k


def present():
    rolls = text_input()
    present_rolls = []
    with open(see_files()) as fil:
        a = fil.readlines()
        for lines in a:
            line = lines[15:]
            if line[:2].isdigit():
                present_rolls.append(int(line[:2]))
    present_rolls = sorted(list(dict.fromkeys(present_rolls)))
    absent_rolls = [i for i in rolls if i not in present_rolls]
    return absent_rolls, present_rolls


def time():
    now = datetime.datetime.now()
    year = now.strftime("%y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    return year, month, day


def text_maker(present_rolls, subject):
    if len(subject) < 14:
        space = 14-len(subject)
        for _ in range(space):
            subject += " "
    with open("data.txt", "a") as data:
        year, month, day = time()
        data.write(f"{day}\{month}\{year}||{subject}||{present_rolls}\n")


y, m, d = time()


def union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def read_rolls(subject, date=f"{d}\{m}\{y}"):
    with open("data.txt") as data:
        lines = data.readlines()
    for i in range(len(lines)):
        if lines[i][:8] == date and subject in lines[i]:
            value = 0
            present_students = ""
            roll = lines[i][27:].rstrip()
            roll = roll.replace("]", "")
            got = roll.split(",")
            got = [int(k) for k in got]
    return got


def text_updater(rolls, subject, date=f"{d}\{m}\{y}", present_or_absent=True):
    new_lines = []
    with open("data.txt") as data:
        lines = data.readlines()
    for i in range(len(lines)):
        if lines[i][:8] == date and subject in lines[i]:
            value = 0
            present_students = ""
            roll = lines[i][27:].rstrip()
            roll = roll.replace("]", "")
            got = roll.split(",")
            got = [int(k) for k in got]
            if present_or_absent:
                new_roll = union(got, rolls)
            else:
                new_roll = intersection(got, rolls)
                new_roll = [no for no in got if no not in new_roll]
            for g in new_roll:
                if value == 0:
                    present_students += f"{g}"
                    value = 1
                else:
                    present_students += f",{g}"
            present_students += "]\n"
            a = lines[i].replace(lines[i][27:], present_students)
            print(a)
            new_lines.append(a)
            continue
        new_lines.append(lines[i])
    with open("data.txt", "w") as data:
        for line in new_lines:
            data.write(line)


absent, p = present()
for i in sub:
    text_updater(p, i)
