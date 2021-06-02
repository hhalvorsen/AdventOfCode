import sys, os, re


class Instruction:
    instruction = ""
    step = 0
    previous_line_pos = 0
    executed = False
    position = 0


def run_code(liste, accum, start_pos):
    line = start_pos
    something_changed = False
    changed_line = 0
    previous_line = 0
    while line < len(liste) - 1:

        if liste[line].executed:
            # Del 2:

            previous_line = liste[line].previous_line_pos
            print(previous_line)
            if something_changed:
                something_changed = False
                if liste[changed_line].instruction == "nop":
                    liste[changed_line].instruction = "jmp"
                    line = liste[changed_line].previous_line_pos
                elif liste[changed_line].instruction == "jmp":
                    liste[changed_line].instruction = "nop"
                    line = liste[changed_line].previous_line_pos
            else:
                if liste[previous_line].instruction == "nop":
                    liste[previous_line].instruction = "jmp"
                    liste[previous_line].executed = False
                    changed_line = previous_line
                    something_changed = True
                elif liste[previous_line].instruction == "acc":
                    accum -= liste[previous_line].step
                    line = liste[previous_line].previous_line_pos
                    liste[line].executed = False
                    while liste[line].instruction.equals("acc"):
                        accum -= liste[line].step
                        line = liste[line].previous_line_pos
                        liste[line].executed = False
                elif liste[previous_line].instruction == "jmp":
                    liste[previous_line].instruction = "nop"
                    liste[previous_line].executed = False
                    changed_line = previous_line
                    something_changed = True

            # Del 1:
            # break
        else:
            liste[line].executed = True
            saveline = line

            if liste[line].instruction == "nop":
                line += 1
            elif liste[line].instruction == "acc":
                accum += liste[line].step
                line += 1
            elif liste[line].instruction == "jmp":
                line += liste[line].step

            liste[line].previous_line_pos = saveline

    return accum


with open(os.path.join(sys.path[0], 'input.txt'), mode='r', encoding='utf-8') as _file:
    records = _file.read().split('\n')

instructionliste = list()
for x in records:
    tempLine = x.split()
    tempIns = Instruction()
    tempIns.instruction = tempLine[0]
    tempIns.step = int(tempLine[1])
    tempIns.position = len(instructionliste)

    instructionliste.append(tempIns)

# Kjører gjennom
startPosition = 0
accumulator = 0

accumulator = run_code(instructionliste, accumulator, startPosition)

print(accumulator)
