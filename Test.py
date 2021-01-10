from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from datetime import datetime
import os
import subprocess
import time
from selenium.webdriver.common.keys import Keys


def init():
    now = datetime.now()
    fileStr = os.path.join(
        "D:\\Users\\amr-e\\Desktop\\PL\\\PL__Project\\Puzzles\\Puzzle-{month}-{day}.txt".format(month=now.month,
                                                                                                day=now.day))
    values = get_puzzle_information(fileStr)
    return values


def getGoogle(driver):
    driver.get("https://www.google.com/")


def getWordnet(driver):
    driver.get("http://wordnetweb.princeton.edu/perl/webwn")


def getThesaurus(driver):
    driver.get("https://www.thesaurus.com/")


def getMerriam(driver):
    driver.get("https://www.merriam-webster.com/")


def getUrban(driver):
    driver.get("https://www.urbandictionary.com/")


def getAcronym(driver):
    driver.get("https://www.acronymfinder.com/")


def getAbbreviation(driver):
    driver.get("https://www.abbreviations.com/")


def get_chrome_driver():
    options = Options()
    options.add_argument("--mute-audio")
    options.add_argument("--disable-gpu")
    options.add_argument("--lang=en-GB")
    options.add_argument("log-level=2")
    driver = webdriver.Chrome(options=options)
    return driver


def get_puzzle_information(file_dir, url="https://www.nytimes.com/crosswords/game/mini"):
    now = datetime.now()
    file = open("D:\\Users\\amr-e\\Desktop\\PL\\\PL__Project\\Puzzles\\Puzzle-{month}-{day}.txt".format(month=now.month,
                                                                                                        day=now.day),
                "w+", encoding="utf-8")

    # Revealing puzzle and getting puzzle info
    options = Options()
    options.headless = True
    options.add_argument("--mute-audio")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome()
    driver.get('https://www.nytimes.com/crosswords/game/mini')
    print("Getting puzzle from https://www.nytimes.com/crosswords/game/mini")
    time.sleep(2)
    driver.find_element_by_class_name('buttons-modalButton--1REsR').click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='root']/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div/div[4]/div/main/div[2]/div/div/ul/div[2]/li[2]/ul/li[3]").click()
    time.sleep(2)
    driver.find_element_by_xpath(
        "//*[@id='root']/div/div[2]/div[2]/article/div[2]/button[2]").click()

    hint_list = {}
    keywords = ("Across", "Down")
    index = 0
    prev_no = 0
    clues = driver.find_elements_by_class_name("Clue-text--3lZl7")
    numbers = driver.find_elements_by_class_name("Clue-label--2IdMY")
    for number, clue in zip(numbers, clues):
        no = number.get_property("textContent")
        content = clue.get_property("textContent")
        if (int(no) < prev_no):
            index = 1
        s = keywords[index] + ":\t" + no + " " + content + "\n"
        file.write(s)
        prev_no = int(no)

    reveals = {}
    for i in range(25):
        reveal = driver.find_element_by_id("cell-id-{i}".format(i=i))
        reveal_sibs = reveal.get_property("parentNode").get_property("childElementCount")
        if reveal_sibs == 1:
            s = str(i + 1) + ":\tblack" + "\n"
            file.write(s)
            reveals[i + 1] = "black"
        elif reveal_sibs == 3:
            value = reveal.get_property("parentNode").get_property("childNodes")[1].get_property("textContent")
            s = str(i + 1) + ":\twhite " + value + "\n"
            file.write(s)
            reveals[i + 1] = ("white", value)
        elif reveal_sibs == 4:
            number = reveal.get_property("parentNode").get_property("childNodes")[1].get_property("textContent")
            value = reveal.get_property("parentNode").get_property("childNodes")[2].get_property("textContent")
            s = str(i + 1) + ":\twhite " + value + " " + number + "\n"
            file.write(s)
            reveals[i + 1] = ("white", number, value)
    file.close()
    print("Puzzle txt file created sucessfully!")

    return hint_list, reveals


def words():
    now = datetime.now()
    fileName = os.path.join(
        "D:\\Users\\amr-e\\Desktop\\PL\\PL__Project\\Puzzles\\Puzzle-{month}-{day}.txt".format(month=now.month,
                                                                                               day=now.day))
    file = open(fileName, "r", encoding="utf-8")
    letterArr = []
    count = 0
    for line in file:
        count += 1
        if (str(line[0]).isdigit()):
            if (line[3] == 'w'):
                letterArr.append("0{count}-{data}".format(count=count - 10, data=line[9]))
            elif (line[4] == 'w'):
                letterArr.append("{count}-{data}".format(count=count - 10, data=line[10]))
            elif (count - 10 > 9):
                letterArr.append("{count}-{data}".format(count=count - 10, data=' '))
            else:
                letterArr.append("0{count}-{data}".format(count=count - 10, data=' '))
    print(letterArr)
    wordArr = []
    word = ""
    for y in range(1, 6):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(6, 11):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(11, 16):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(16, 21):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(21, 26):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(1, 26, 5):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(2, 26, 5):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(3, 26, 5):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(4, 26, 5):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    word = ""
    for y in range(5, 26, 5):
        for x in letterArr:
            if (int(x[:2]) == y):
                word = word + x[-1]
    wordArr.append(word)
    return wordArr


def SearchAcronym(word, driver):
    text_field = driver.find_element_by_xpath("//*[@id='search-main-input']")
    text_field.clear()
    text_field.send_keys(word)
    text_field.send_keys(Keys.ENTER)

    time.sleep(2)
    retrieve = driver.find_element_by_xpath("//*[@id='content']/div[4]/div/table/tbody/tr[1]/td[2]")
    out = retrieve.get_attribute("innerText")
    return out


def SearchAbbreviation(word, driver):
    text_field = driver.find_element_by_xpath("//*[@id=\"search\"]")
    text_field.clear()
    text_field.send_keys(word)
    text_field.send_keys(Keys.ENTER)

    time.sleep(2)
    retrieve = driver.find_element_by_xpath("//*[@id=\"content-body\"]/div/div[3]/div/table[2]/tbody/tr[1]/td[2]/p[1]")
    out = retrieve.get_attribute("innerText")
    return out


def SearchGoogle(word, driver):
    text_field = driver.find_element_by_css_selector(".gLFyf.gsfi")
    text_field.clear()
    text_field.send_keys(word + " meaning")
    text_field.send_keys(Keys.ENTER)

    try:
        element = driver.find_element_by_css_selector('.mQo3nc.hsL7ld')
        driver.execute_script("""
            var element = arguments[0];
            element.innerHTML = "";
            """, element)
    except Exception as e:
        pass

    meanings = driver.find_elements_by_css_selector('.QIclbb.XpoqFe span')
    if (len(meanings) != 0):
        res_str = ""
        for x in range(0, len(meanings)):
            try:
                temp_str = meanings[x].text
                res_str += "" + temp_str[:1].upper() + temp_str[1:]
            except Exception as e:
                pass
        return res_str


def SearchWord(word, driver):
    text_field = driver.find_element_by_name("s")
    submit_button = driver.find_element_by_name("sub")
    text_field.clear()
    text_field.send_keys(word)
    submit_button.click()

    search_list = []

    all_ul = driver.find_elements_by_tag_name("ul")
    for ul in all_ul:
        # priority_li = []
        all_li = ul.find_elements_by_tag_name("li")
        for li in all_li:
            text = li.get_attribute("innerText")
            ## Substring -> whether it is a verb or noun
            firstLP = text.index("(")
            firstRP = text.index(")")

            ## Substring -> find what it means
            secondLP = text.index("(", firstLP + 1)
            secondRP = text.rindex(")", firstRP + 1)

            ## If the search key doesn't exist as part of the found words, skip
            loc = text[firstRP + 1:secondLP].lower().find(word)
            if (loc == -1):
                continue

            ## If the search key is not contained in the result, return it
            if (text[secondLP + 1:secondRP].find(word) == -1):
                search_list.append(text[secondLP + 1:secondRP])
                # priority_li.append(loc)
    if (len(search_list) != 0):
        return search_list[0]


def SearchUrbanDic(word, driver):
    text_field = driver.find_element_by_name("term")
    text_field.clear()
    text_field.send_keys(word)
    text_field.send_keys(Keys.ENTER)

    definitions = []
    sentences = []

    meanings = driver.find_elements_by_class_name("meaning")
    examples = driver.find_elements_by_class_name("example")
    for meaning, example in zip(meanings, examples):
        if word.lower() == "adele":
            break
        mean = meaning.get_attribute("innerText")
        ex = example.get_attribute("innerText")
        m_lines = mean.split("\n")
        for m in m_lines:
            if (re.search(r"\b{0}\b".format(word), m.lower()) is None):
                if (len(m.split()) < 30) and (len(m.split()) > 0):
                    # and (numpy.ndarray.tolist(predict([m]))==[0]):
                    # if(len([x for x in arrBad if m.lower().find(x) is not -1]) == 0):
                    definitions.append(m)

        e_lines = ex.split("\n")
        for e in e_lines:
            if (re.search(r"\b{0}\b".format(word), e.lower()) is not None):
                if (len(e.split()) < 30) and (len(e.split()) > 0):
                    # and (numpy.ndarray.tolist(predict([e]))==[0]):
                    # if(len([x for x in arrBad if m.lower().find(x) is not -1]) == 0):
                    # e = e.replace(word,"?"*len(word))
                    sentences.append(e)
        if definitions[0].find("Ü") != -1:
            definitions[0] = definitions[0][0:definitions[0].index(".")]
    if (len(definitions) != 0):
        return definitions[0]


def SearchThesaurus(word, driver):
    text_field = driver.find_element_by_id("searchbar_input")
    submit_button = driver.find_element_by_id("search-submit")
    text_field.clear()
    text_field.send_keys(word)
    submit_button.click()

    search_list = []

    a = driver.find_elements_by_css_selector(".css-1twju98.e9i53te7")
    if (len(a) != 0):
        em = a[0].find_element_by_tag_name("em")
        if (em.get_attribute("innerText") == "as in"):
            strong = a[0].find_element_by_tag_name("strong")
            search_list.append("as in '" + strong.get_attribute("innerText") + "'")
    return search_list


def SearchMerriam(word, driver):
    text_field = driver.find_element_by_id("s-term")
    text_field.clear()
    text_field.send_keys(word)
    text_field.send_keys(Keys.ENTER)

    search_list = []
    beginning = ""
    plural = ""

    changed = driver.find_elements_by_class_name("hword")
    alternatives = driver.find_elements_by_class_name("vg-ins")

    ## check if search key was changed by the dictionary
    if (len(changed) != 0):
        if (word != changed[0]):
            if (len(alternatives) != 0):
                if (word == "media"):
                    return search_list
                if (word not in alternatives[0].get_attribute("innerText")):
                    return search_list

    # check if it is plural
    if (len(alternatives) != 0):
        pl = alternatives[0].find_elements_by_css_selector(".il.plural")
        ifs = alternatives[0].find_elements_by_css_selector(".if")

        if (len(pl) != 0):
            if (len(ifs) != 0):
                if (ifs[0].get_attribute("innerText").lower() != word.lower()):
                    if (re.search(r"plural", pl[0].get_attribute("innerText"))):
                        plural = "Plural"

    # check if the search key is from a foreign language etc
    form = driver.find_elements_by_class_name("fl")
    if (len(form) != 0):
        beginning = form[0].get_attribute("innerText").strip()

    results = driver.find_elements_by_class_name("dtText")
    for result in results:
        # find the size of children (the text content is separated among them)
        children_size = driver.execute_script("return arguments[0].childNodes.length", result)

        # if there are more than 1 child, take the contents of #text
        # else, get the contents of the first child
        text = driver.execute_script(
            'str = ""; arguments[0].childNodes.forEach( (item) => { if (item.nodeName != "SPAN" && item.nodeName != "STRONG" && item.nodeName != "P") { str = str + item.textContent; } } ); return str;',
            result).strip()

        if (text != ""):
            if (text[0] == ";"):
                text = text[2:]

            if (beginning != "" and re.search(r"\bnoun\b", beginning) == None and re.search(r"\bverb\b",
                                                                                            beginning) == None and re.search(
                r"\binterjection\b", beginning) == None):
                text = beginning + ", " + text

            if (plural != ""):
                text = plural + ", " + text

            # print(text)
            search_list.append(text)

    if (word == "clark"):
        search_list.pop(0)
        search_list.pop(0)
    if (len(search_list) != 0):
        return search_list[0]


def searchAll(word):
    # desktopPath = os.path.join(os.path.expanduser('~'), 'Desktop')
    fileString = os.path.join("D:\\Users\\amr-e\\Desktop\\PL\\PL__Project\\Processing Files\\outputFile.txt")
    # file2 = open(fileString, "w+", encoding="utf-8")

    browser = get_chrome_driver()
    new_hints = []
    getGoogle(browser)

    # getThesaurus(browser3)

    for x in range(0, 10):
        new_hints.append((SearchGoogle(word[x].lower(), browser)))
        try:
            new_hints[x] = str(x) + ". " + str(word[x]) + ":\t" + new_hints[x].split('.')[0][:1].upper() + \
                           new_hints[x].split('.')[0][1:] + "\n"
        except Exception as e:
            pass
    for y in range(0, 10):
        if (new_hints[y] is None):
            getMerriam(browser)
            new_hints[y] = SearchMerriam(word[y].lower(), browser)
            if (not (new_hints[y] is None)):
                try:
                    new_hints[y] = str(y) + ". " + str(word[y]) + ":\t" + new_hints[y][:1].upper() + new_hints[y][1:] + ".\n"
                except AttributeError:
                    new_hints[y] = str(y) + ". " + str(word[y]) + ":\t" + "Not found!!\n"

        if (new_hints[y] is None):
            getWordnet(browser)
            new_hints[y] = SearchWord(word[y].lower(), browser)
            if (not (new_hints[y] is None)):
                try:
                    new_hints[y] = str(y) + ". " + str(word[y]) + ":\t" + new_hints[y][:1].upper() + new_hints[y][
                                                                                                     1:] + ".\n"
                except AttributeError:
                    new_hints[y] = str(y) + ". " + str(word[y]) + ":\t" + "Not found!!\n"

        if (new_hints[y] is None):
            getThesaurus(browser)
            new_hints[y] = SearchThesaurus(word[y].lower(), browser)
            if (not (new_hints[y] is None)):
                try:
                    new_hints[y] = str(y) + ". " + str(word[y]) + ":\t" + new_hints[y][:1].upper() + new_hints[y][
                                                                                                     1:] + ".\n"
                except AttributeError:
                    new_hints[y] = str(y) + ". " + str(word[y]) + ":\t" + "Not found!!\n"

        if (new_hints[y] is None):
            getAcronym(browser)
            new_hints[y] = SearchAcronym(word[y].lower(), browser)
            if (not (new_hints[y] is None)):
                try:
                    new_hints[y] = str(y) + ". " + str(word[y]) + ":\t" + new_hints[y][:1].upper() + new_hints[y][
                                                                                                     1:] + ".\n"
                except AttributeError:
                    new_hints[y] = str(y) + ". " + str(word[y]) + ":\t" + "Not found!!\n"

        if (new_hints[y] is None):
            getAbbreviation(browser)
            new_hints[y] = SearchAbbreviation(word[y].lower(), browser)
            if (not (new_hints[y] is None)):
                try:
                    new_hints[y] = str(y) + ". " + str(word[y]) + ":\t" + new_hints[y][:1].upper() + new_hints[y][
                                                                                                     1:] + ".\n"
                except AttributeError:
                    new_hints[y] = str(y) + ". " + str(word[y]) + ":\t" + "Not found!!\n"

    with open(fileString, "w+", encoding="utf-8") as file2:
        for z in range(0, 10):
            if (not (new_hints[z] is None)):
                #print(new_hints[z])
                file2.write(new_hints[z])
            else:
                new_hints[z] = str(z) + ". " + str(word[z]) + new_hints[z][:1].upper() + new_hints[z][1:] + ":\n"
                file2.write(new_hints[z])


def runJava():
    proc = subprocess.Popen(['javac', 'D:\\Users\\amr-e\\Desktop\\PL\\PL__Project\\src\\getData.java'])
    proc = subprocess.Popen(['javac', 'D:\\Users\\amr-e\\Desktop\\PL\\PL__Project\\src\\Grid.java'])
    subprocess.Popen('java Grid')


def main():
    init()
    word = words()
    searchAll(word)
    runJava()


if __name__ == '__main__':
    main()
