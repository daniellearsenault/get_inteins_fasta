if __name__ == '__main__':
    #where inbase_html_28Dec2020.txt == html of InBase intein seq list (currently 2 pages long)
    #in my version of inbase_html_28Dec2020:
    #   I cut out the top chunk
    #   from <html> to just before <h1>Inteins[...]
    #   by hand
    #AND
    #   replaced all instances of 'Intein Sequence:'
    #   with 'intseq:'
    import re
    with open('inbase_html_28Dec2020.txt', 'r') as file:
        inteins_str = file.read()
    #remove white space and line breaks
    inteins_str = re.sub(r"[\n\t\s]*", "", inteins_str)
    #writing str to .txt file
    output_file = open("inbase_html_nospace.txt", "w")
    output_file.write(inteins_str)
    output_file.close()
    #now have all of InBase 2.0 int list as conc. .txt file
    #1273 entries as of 12/28/2020

    int_name_indexes = []
    for i in range(len(inteins_str)):
        if (inteins_str[i] == 'I') and (inteins_str[i + 6] == 'N') and (inteins_str[i + 10] == ':'):
            int_name_indexes.append((i + 15))
    #following print statements for testing
    #print("these are indexes for I of every InteinName:", int_name_indexes)
    print("InteinName count:", len(int_name_indexes))
    seq_indexes = []
    for i in range(len(inteins_str)):
        if (inteins_str[i] == 'S') and (inteins_str[i + 2] == 'q') and (inteins_str[i + 8] == ':'):
            seq_indexes.append((i + 13))
    #following print statements for testing
    #print("these are indexes for S of every Sequence:", seq_indexes)
    print("Sequence count:", len(seq_indexes))

    #following creates output in format of
    #>inteinname newline
    #SEQUENCECONTENT newline
    #>inteinname [...]

    name_seq_pairs = []
    for n in range(len(int_name_indexes)):
        this_int_name = ''
        i = 0
        while inteins_str[int_name_indexes[n] + i] != '<':
            this_int_name += inteins_str[int_name_indexes[n] + i]
            i += 1
        this_seq = ''
        i = 0
        while inteins_str[seq_indexes[n] + i] != '<':
            this_seq += inteins_str[seq_indexes[n] + i]
            i += 1
        name_seq_pairs.append([this_int_name, this_seq])

    #after reviewing ouptut, some seq names at end have '&gt;' at start, would like to remove
    for n in range(len(name_seq_pairs)):
        this_pair = name_seq_pairs[n]
        this_name = this_pair[0]
        this_seq = this_pair[1]
        if len(this_name) >= 4:
            first_four_of_name = this_name[0] + this_name[1] + this_name[2] + this_name[3]
            if first_four_of_name == '&gt;':
                name_seq_pairs[n] = [this_name[4:], this_seq]

    output = ""
    for n in range(len(name_seq_pairs)):
        this_pair = name_seq_pairs[n]
        output += '>'
        output += this_pair[0]
        output += '\n'
        output += this_pair[1]
        output += '\n'

    output_txt = open("all_inteins_28Dec2020.fasta", "w")
    output_txt.write(output)
    output_txt.close()
    #final output, fasta of all current inteins +-1 extein residue
    #saved as all_inteins_28Dec2020.fasta
