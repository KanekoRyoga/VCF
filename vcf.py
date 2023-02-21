use_list = []
with open("Generation01.vcf") as vcffile:

    #1行ずつ読み込む。文字列
    for vcffile_line in vcffile:
        #print(vcffile_line)
        #読み込んだ行にmissense_variantという文字があれば抜き出す。文字列
        if "missense_variant" in vcffile_line:

            #行をANN=で区切って後ろ側と取り出す。文字列
            get_info = vcffile_line.split(';ANN=')[1]
            #print(get_info)
            
            #取り出した後ろ側をカンマで区切る。 リスト
            split_comma_list = get_info.split(',')
            #print(split_comma_list)
            for split_comma_list_youso in split_comma_list:
                
                #取り出した要素をパイプで区切ってmissense_variantを含む場合処理する。
                split_comma_split_pipe_list = split_comma_list_youso.split('|')
                #print(split_comma_split_pipe_list)
                if  "missense_variant" in split_comma_split_pipe_list:
                    ID_varpos_list = [split_comma_split_pipe_list[6],split_comma_split_pipe_list[10]]
                    use_list.append(ID_varpos_list)
                
                else:
                    pass
        
        else:
            pass


print(len(use_list))

for youso in use_list:
    print(youso)

