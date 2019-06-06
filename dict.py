#keyが名前,valueがスコアの辞書
name_score_dict = {"sean":120,"bob":20,"sarah":30,"josh":25,"alex":50}

name_score_dict["bob"] = 80

for name , score in name_score_dict.items():

    print(name,score)

for name in name_score_dict.keys():

    print(name_score_dict[name])
