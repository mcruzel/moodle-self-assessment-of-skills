# V 1.0, March 2023
# Maxime Cruzel
# Generate a xml set of feedback questions about competencies mastering

scale = {
    1 : "lvl 1",
    2 : "lvl 2",
    3 : "lvl 3"
}

def loop_competency_entry(competency_pool):
    # Ask for the competency code
    print("Enter the competency code or type \"-q\" to generate xml file")
    comp_code = input("> ")
    if len(comp_code.split("-q")) > 1: # leave
        print(competency_pool)
        gen_xml(competency_pool, scale)
    else:
        # Ask for the competency name
        comp_name = input("Enter the competency name > ")
        competency_pool.append([comp_code, comp_name])
        loop_competency_entry(competency_pool) 
        
def gen_xml(competency_pool, scale):
    filecontent = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n"
    filecontent += "<FEEDBACK VERSION=\"200701\" COMMENT=\"XML-Importfile for mod/feedback\">\n"
    filecontent += "\t<ITEMS> \n"
    
    
    for competency in competency_pool:
        filecontent += "\t\t<ITEM TYPE=\"multichoice\" REQUIRED=\"1\">\n"
        filecontent += "\t\t<ITEMID><![CDATA[203]]></ITEMID>\n"
        filecontent += "\t\t<ITEMTEXT><![CDATA[{}]]></ITEMTEXT>\n".format(competency[1])
        filecontent += "\t\t<ITEMLABEL><![CDATA[{}]]></ITEMLABEL>\n".format(competency[0])
        filecontent += "\t\t<PRESENTATION><![CDATA[r>>>>>"
        count = 0
        for key, value in scale.items():
            if count == 0:
                filecontent += """{} - {}\n""".format(key, value)
                count += 1
            else:
                filecontent += """|{} - {}\n""".format(key, value)
        filecontent += "<<<<<1]]></PRESENTATION>\n"
        filecontent += "\t\t<OPTIONS><![CDATA[h]]></OPTIONS>\n"
        filecontent += "\t\t<DEPENDITEM><![CDATA[0]]></DEPENDITEM>\n"
        filecontent += "\t\t<DEPENDVALUE><![CDATA[]]></DEPENDVALUE>\n"
        filecontent += "\t\t</ITEM>\n" 
        
    filecontent += "\t</ITEMS>\n"
    filecontent += "</FEEDBACK>"
    
    with open("feedback.xml", "w", encoding="UTF-8") as file:
        # write the xml file with filecontent
        file.write(filecontent)
         
def main(scale):
    competency_pool = []
    loop_competency_entry(competency_pool)
    
main(scale)
