from arraystack import ArrayStack

def read_file():
    file = open('base.lst','r', encoding="utf-8")
    st = ArrayStack()
    for line in file:
        st.push(line)
    print(st)
read_file()