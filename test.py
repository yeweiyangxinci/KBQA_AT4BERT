import pandas as pd

def convertToPredict():
    f = open('./output/output_nlpcc2016.txt', 'r')
    line_entity = []
    test_result = []
    question_strs = []
    que_str = ""
    while True:
        content = f.readline()
        if content == '':
            break
        elif content[0]=='\n':
            test_result.append(line_entity)
            question_strs.append(que_str)
            line_entity = []
            que_str = ""
        else:
            content = content.strip().split()
            line_str = ''
            if content[2] != 'O':
                while True:
                    #print(len(content))
                    if content[0] == '\n':
                        test_result.append(line_entity)
                        question_strs.append(que_str)
                        line_entity = []
                        que_str = ""
                        break
                    elif content[2] == 'O':
                        que_str = que_str + content[0]
                        break
                    else:
                        line_str = line_str + content[0]
                        que_str = que_str + content[0]
                        content = f.readline()
                line_entity.append(line_str)
            else:
                que_str = que_str + content[0]



    nlpcc_test_data = pd.read_csv("./data/NER_Data/q_t_a_df_testing.csv")
    nlpcc_test_result = []
    #print(test_result)
    # print(len(test_result))
    # print(question_strs)
    # print(len(question_strs))
    # print(len(nlpcc_test_data))
    result_idx = 0
    result_len = len(test_result)

    another = []
    nn = []
    idx = 0
    outidx = 0
    for row in nlpcc_test_data.index:
        # if result_idx > 2:
        #     break
        question = nlpcc_test_data.loc[row, "q_str"]
        entity = nlpcc_test_data.loc[row, "t_str"].split("|||")[0].split(">")[1].strip()
        attribute = nlpcc_test_data.loc[row, "t_str"].split("|||")[1].strip()
        answer = nlpcc_test_data.loc[row, "t_str"].split("|||")[2].strip()
        another.append(question)
        outidx = outidx+1
        if question in question_strs[idx]:
            idx = idx + 1
        if idx >= 9000:
            break
    print(idx)
    print(outidx)

    # print("----------")
    # print(another[0] == question_strs[0])
    print(len(another))
    # print(question_strs[0])
    # print("----------")
    #    str = question_strs[result_idx]
    #     print(str)
    #     print(question)
    #     if str in question:
    #         nlpcc_test_result.append(question + "\t" + entity + "\t" + attribute + "\t" + answer + "\t" + ','.join(str))
    #         result_idx = result_idx + 1
    #     else:
    #         nlpcc_test_result.append(question + "\t" + entity + "\t" + attribute + "\t" + answer + "\t" + ','.join(""))
    # with open("./data/NER_Data/q_t_a_testing_predict.txt", "w") as f:
    #     f.write("\n".join(nlpcc_test_result))

if __name__ == "__main__":
    #tf.app.run()
    convertToPredict()