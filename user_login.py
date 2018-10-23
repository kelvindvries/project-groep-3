def login_bezoeker(gebr_bezoeker, ww_bezoeker):

    with open('bezoekerFiles.txt', 'w+') as bezoekerFile:
        bezoekerFile.write(gebr_bezoeker, ww_bezoeker)


def login_aanbieder(gebr_aanbieder, ww_aanbieder):

    with open('aanbiederFiles.txt', 'w+') as aanbiederFile:
        aanbiederFile.write(gebr_aanbieder, ww_aanbieder)