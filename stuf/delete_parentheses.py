class Solution:

    def lenLongestFibSubseq1(self, arr) -> int:
        sum_result = 0
        for i in range(len(arr) - 1, 0, -1):
            sum = 1
            print('-- -------- ------- ------- ----')
            j = i
            var1 = arr[j]
            for j in range(i - 1, 0, -1):
                var2 = arr[j]
                print(f'---{arr[j]}---')

                while True:
                    var_result = var1 - var2
                    if var_result > var1 / 2:
                        print(f'{var1}-{var2}={var_result}', end=' | ')
                    if var_result in arr:
                        var1, var2 = var2, var_result
                        sum += 1

                    else:
                        if sum > sum_result:
                            sum_result = sum
                        break

                print()
        return sum_result

    def fib(self, arr) -> int:
        max_range = 0
        # for i in range(len(arr) - 2):
        i, j, stop = 0, 1, False
        while i < len(arr) - 1:
            # while j < (len(arr) - 2):
            print(f'*** i = {i} j = {j}', end=' ***\n')
            f1, f2 = arr[i], arr[j]
            if (f1 + f2) in arr[arr.index(f2):]:
                s = 3
                print('| ', f1, '+', f2, f' = {f1 + f2} |')
                while True:
                    f1, f2 = f2, f1 + f2
                    print('| ', f1, '+', f2, f' = {f1 + f2} |')
                    if f1 + f2 not in arr[arr.index(f2):]:
                        max_range = max(max_range, s)
                        j += 1
                        if f2 == arr[len(arr) - 1]:
                            print('stop')
                            stop = True
                        break
                    s += 1
                if stop:
                    break
            else:
                j += 1
            if j > len(arr) - 1:
                j = i + 2
                i += 1
            # print('---- ---- ----')
        return max_range






b = [1, 2, 3, 4, 5, 6, 7, 8]
c = [2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]
a = [2, 5, 6, 7, 8, 10, 12, 17, 24, 41, 65]
d = [2, 4, 5, 6, 7, 8, 11, 13, 14, 15, 21, 22, 34]
e = [3, 4, 9, 10, 12, 14, 15, 24, 27, 38, 42]
arr = \
    [3, 9, 14, 22, 23, 32, 37, 52, 54, 59, 60, 67, 68, 69, 71, 74, 76, 77, 82, 84, 85, 96, 97, 99, 100, 101, 113, 118,
     138,
     140, 145, 152, 157, 161, 167, 170, 176, 178, 204, 219, 222, 246, 254, 258, 271, 274, 275, 280, 356, 360, 364, 398,
     407,
     411, 441, 447, 451, 452, 560, 582, 583, 653, 656, 712, 726, 727, 916, 942, 947, 1054, 1060, 1153, 1174, 1177, 1178,
     1476, 1524, 1710, 1713, 1865, 1901, 1903, 1904, 2392, 2466, 2764, 2773, 3018, 3075, 3080, 3082, 3868, 3990, 4474,
     4486,
     4883, 4976, 4986, 6260, 6456, 7238, 7259, 7901, 8051, 8068, 10128, 10446, 11712, 11745, 12784, 13027, 13054, 16388,
     16902, 18950, 19004, 20685, 21078, 26516, 27348, 30662, 30749, 33469, 34105, 42904, 44250, 49612, 49753, 54154,
     55183,
     69420, 71598, 80274, 80502, 87623, 89288, 112324, 115848, 129886, 130255, 141777, 144471, 181744, 187446, 210160,
     210757, 229400, 233759, 294068, 303294, 340046, 341012, 371177, 378230, 475812, 490740, 550206, 551769, 600577,
     611989,
     769880, 794034, 890252, 892781, 990219, 1245692, 1284774, 1440458, 1444550, 1602208, 1737563, 1748182, 2015572,
     2078808, 2330710, 2337331, 2592427, 3261264, 3363582, 3771168, 3781881, 4194635, 5276836, 5442390, 5531581,
     6006413,
     6119212, 6787062, 8805972, 9901093, 10960359, 10981697, 11101020, 11961598, 12976360, 14248362, 14442420, 14821434,
     15359202, 15936648, 16020305, 19284185, 21681839, 22638357, 23054334, 24756215, 24957247, 25145810, 25372355,
     25512030,
     25921398, 27381620, 27518473, 28432766, 28800930, 29239260, 30977016, 31317897, 32181690, 32597170, 33448471,
     34335563,
     35479655, 35679653, 36362380, 40370235, 41126782, 42047464, 44210863, 45032676, 45485453, 45927401, 46440611,
     47648021,
     48332713, 51739879, 53661087, 54013763, 55671099, 59729554, 61031400, 61152946, 62094075, 63334100, 63982252,
     64126215,
     67064863, 68090430, 68890150, 69771650, 70492097, 73093292, 73179931, 73734016, 73799297, 76592074, 78130473,
     78754798,
     80779631, 82434243, 83414845, 85057940, 85251139, 88819311, 89561647, 90331595, 92828269, 93468391, 94424903,
     95269536,
     96674583, 99147115, 99304223, 100683780, 101286921, 102423259, 106222561, 107513954, 110484789, 112624349,
     113305153,
     113420780, 114986792, 115331335, 116721365, 116763864, 119418978, 120058202, 123876716, 124130078, 124160561,
     124874359, 125866935, 127869582, 128668997, 130982132, 131187052, 131384155, 132021146, 134138723, 135387833,
     137108804, 140681630, 141774984, 142665527, 144009028, 146443879, 149607927, 150768349, 151574645, 155152577,
     155654187, 157120970, 160132832, 160239672, 160418454, 160629526, 162443201, 162528946, 162719409, 163574244,
     165243500, 166151622, 167651444, 167813760, 167890012, 169054168, 170539766, 170641609, 170790480, 171077223,
     171423306, 173382749, 173998398, 179781823, 179893993, 180122344, 182400879, 183411374, 183956080, 184023701,
     186025822, 186319462, 186515028, 187224835, 189123445, 191746044, 192011848, 192144662, 192890972, 193441337,
     193630982, 194555696, 194849625, 197904750, 198270074, 198569232, 199067326, 199465362, 205702616, 205865378,
     206968102, 207696508, 208473827, 208757599, 211569286, 211837048, 212570096, 213442202, 214701108, 216976425,
     217255176, 217366958, 217741564, 218086772, 218402158, 220008410, 223853002, 224386961, 225206489, 226685222,
     228238345, 228416869, 230451582, 231055196, 231130722, 231510218, 234952848, 235602988, 235717603, 238086790,
     238805521, 239086781, 243268500, 245805104, 247158300, 249204106, 259775936, 259987335, 260249539, 260384651,
     260885593, 262652406, 265666827, 265828471, 267051983, 268534122, 269300646, 269874004, 270482169, 271154775,
     273614210, 275336225, 276627875, 277408629, 277424909, 278354125, 280443227, 282166665, 283289408, 287574811,
     288902764, 289014555, 289309389, 290144124, 290549876, 290611941, 291102434, 292546319, 292637906, 293513631,
     294371513, 294372456, 295612903, 298210528, 298231632, 298897287, 299353983, 300092115, 300583166, 301398973,
     301879226, 303866189, 305299176, 305582067, 307373674, 307636141, 310451055, 311237942, 312075188, 312781745,
     313625496, 314437215, 315451863, 317997185, 318900555, 323335434, 324190312, 324193002, 324390157, 327100855,
     327715138, 329258352, 329526730, 331366326, 332153447, 334861288, 334919104, 336292270, 338983665, 339326621,
     340794440, 343134217, 344540424, 345491570, 345986797, 346756539, 347426753, 347546502, 348434394, 349498903,
     349737700, 350462422, 350632994, 352966259, 352968622, 354475635, 354929134, 355542822, 358129016, 368634316,
     369838051, 370079072, 373881839, 373954283, 375344485, 376042404, 376166339, 377421127, 378586103, 381284493,
     381572471, 381697337, 382078685, 383846673, 384514494, 385791639, 385984975, 386980639, 388228381, 388315594,
     389591731, 389748396, 391427423, 392855032, 393129880, 393476156, 393785983, 394403010, 397124802, 397829750,
     397872372, 398130330, 398829626, 400834600, 401805213, 402115549, 403640403, 403922823, 404692701, 405733259,
     406062999, 407609872, 411639501, 412153217, 413115262, 413358795, 413663015, 415231706, 415284345, 416377968,
     416476929, 419649117, 420386675, 421301058, 422826407, 423476028, 423488105, 423774920, 424366277, 424384242,
     424533280, 428303226, 428737660, 429722455, 430850087, 431047948, 431543995, 434254977, 437891125, 444256040,
     445179701, 445394151, 446213524, 446752005, 446976526, 447274635, 447546836, 448079510, 449171431, 450478112,
     453541063, 454569482, 456373151, 456525339, 458688929, 459203799, 459239886, 460227301, 460725799, 462092719,
     462287754, 462855242, 466259040, 467453533, 471124586, 471489242, 471879750, 472619678, 473539760, 474465284,
     475154773, 477627399, 478289343, 481179241, 481413353, 481539702, 484178863, 486083981, 486634675, 488629431,
     491711700, 492614022, 493013046, 495823042, 497439685, 497903345, 501353684, 502438951, 503391447, 503942300,
     505033754, 505333139, 506132576, 507894840, 508747923, 509001679, 509674032, 510621750, 511112199, 511285772,
     515833466, 516514806, 517574195, 518119196, 519796017, 521295921, 521571537, 524395807, 525886399, 528149235,
     529023126, 529906344, 530836243, 531085418, 533922222, 534974451, 535305241, 535384563, 535548874, 535574596,
     539040129, 542671046, 546647847, 547745392, 548270336, 548436248, 548645879, 548662022, 550087614, 557283503,
     558359552, 559601039, 561781533, 564607942, 565297595, 566707449, 566839708, 569637045, 571641073, 571652665,
     571994891, 572965547, 573523994, 579498811, 580456390, 581639381, 582948099, 584159197, 584401490, 584702789,
     584760550, 586071668, 587764056, 588339315, 589989660, 590465192, 590928739, 593731029, 595395274, 595562376,
     595670800, 596519380, 600309560, 601259745, 603213139, 603328730, 606981637, 607009433, 608060863, 609122190,
     616677864, 617740113, 617916927, 619031974, 619886375, 620829667, 620934603, 621792998, 623911099, 624760661,
     626586872, 627279143, 628321548, 630811914, 633943674, 636553833, 636632055, 638882815, 640747313, 640993950,
     644376879, 644930626, 646689712, 649673488, 650426322, 651004783, 651317354, 652004353, 653520887, 658684970,
     659103743, 660728885, 661541578, 661639585, 663605197, 664501184, 665603955, 667086941, 667804041, 668165106,
     669385393, 669809644, 670057129, 672143142, 673298706, 673948111, 674808417, 675650974, 676134763, 676576872,
     678946752, 681159669, 682774760, 684238880, 685870135, 690974789, 692786917, 695138203, 696018334, 696620553,
     696936056, 697332689, 697352393, 699455242, 699987754, 704101924, 708449168, 708735620, 710102900, 713112993,
     714721675, 715329058, 716225241, 717670686, 721626624, 722459082, 724041483, 724969219, 726741093, 727026507,
     727094693, 728814527, 730757329, 730907708, 731161428, 732266782, 732826958, 733717130, 736296761, 736299693,
     736895365, 736931921, 739506069, 744504260, 746462832, 746672738, 749059556, 749731819, 750028939, 750686307,
     750828744, 753475548, 754201596, 755018294, 756700967, 757744441, 759060552, 759362853, 760362696, 761411808,
     762659358, 765056061, 765712275, 767586006, 767705753, 769770100, 769991745, 770233582, 776870049, 777451070,
     777456024, 778086260, 778494988, 779221108, 779325867, 780746435, 782315675, 783606009, 784039066, 784538268,
     785850603, 789304147, 790168521, 790603227, 792021838, 792266532, 793526745, 793584461, 794054179, 795328015,
     800393689, 804143278, 805665592, 809409635, 811825394, 811931490, 815320990, 817649382, 818716102, 823082360,
     823701604, 826456896, 826750366, 828116759, 828664001, 828707090, 829164135, 832261636, 832455610, 835888967,
     835908269, 836690684, 837266363, 837641293, 838451281, 839770827, 840700413, 842205827, 842815791, 844849706,
     846854520, 848207519, 849137841, 849256184, 850999212, 851797196, 852047422, 852286866, 852925801, 852970204,
     853374990, 853941941, 855053502, 856671585, 856848452, 856851714, 857133817, 857513419, 857529764, 859751212,
     863727103, 864088001, 864802579, 865581180, 869590528, 870611028, 873795712, 874264022, 879944610, 883664714,
     885807712, 889018012, 890437972, 890505222, 891649570, 891929768, 893829620, 893845899, 894097188, 894479562,
     894834620, 896107400, 896591606, 896675526, 898051334, 898785698, 898857049, 899916301, 901011198, 904328179,
     904406351, 904518674, 904742091, 905484932, 906155231, 906589224, 908427712, 909215205, 911666265, 912193648,
     915264085, 917293384, 918287028, 919756036, 924242630, 925173009, 925407377, 926011655, 926337494, 927936720,
     928142475, 929623066, 930293302, 930781786, 931212840, 931219192, 932404877, 934041585, 937804436, 938173245,
     939022548, 939612015, 941530685, 941604005, 943202966, 943904045, 944287568, 944807066, 948156608, 949888275,
     950814572, 951008692, 952362711, 952885221, 952931935, 952967767, 954245205, 956237342, 956892501, 957478826,
     958851125, 959127049, 960671631, 961199142, 961857541, 962113078, 965248622, 966564339, 970715056, 973476038,
     973975773, 977000076, 978159310, 980470939, 980826297, 981244308, 982179297, 984840092, 984885883, 987490164,
     988527907, 989230340, 989749199, 989955771, 990849052, 990872873, 992125893, 992336688, 992627088, 993043544,
     995322102, 996260709, 998300525, 999895841]
arr2 = \
    [3, 9, 14, 22, 23, 32, 37, 52, 54, 59, 60, 67, 68, 69, 71, 74, 76, 77, 82, 84, 85, 96, 97, 99, 100, 101, 113, 118,
     138, 140, 145, 152, 157, 161, 167, 170, 176, 178, 204, 219, 222, 246, 254, 258, 271, 274, 275, 280, 356, 360, 364,
     398, 407, 411, 441, 447, 451, 452, 560, 582, 583, 653, 656, 712, 726, 727, 916, 942, 947, 1054, 1060, 1153, 1174,
     1177, 1178, 1476, 1524, 1710, 1713, 1865, 1901, 1903, 1904, 2392, 2466, 2764, 2773, 3018, 3075, 3080, 3082, 3868,
     3990, 4474, 4486, 4883, 4976, 4986, 6260, 6456, 7238, 7259, 7901, 8051, 8068, 10128, 10446, 11712, 11745, 12784,
     13027, 13054, 16388, 16902, 18950, 19004, 20685, 21078, 26516, 27348, 30662, 30749, 33469, 34105, 42904, 44250,
     49612, 49753, 54154, 55183, 69420, 71598, 80274, 80502, 87623, 89288, 112324, 115848, 129886, 130255, 141777,
     144471, 181744, 187446, 210160, 210757, 229400, 233759, 294068, 303294, 340046, 341012, 371177, 378230, 475812,
     490740, 550206, 551769, 600577, 611989, 769880, 794034, 890252, 892781, 990219, 1245692, 1284774, 1440458,
     1444550, 1602208, 1737563, 1748182, 2015572, 2078808, 2330710, 2337331, 2592427, 3261264, 3363582, 3771168,
     3781881, 4194635, 5276836, 5442390, 5531581, 6006413, 6119212, 6787062, 8805972, 9901093, 10960359, 10981697,
     11101020, 11961598, 12976360, 14248362, 14442420, 14821434, 15359202, 15936648, 16020305, 19284185, 21681839,
     22638357, 23054334, 24756215, 24957247, 25145810, 25372355, 25512030, 25921398, 27381620, 27518473, 28432766,
     28800930, 29239260, 30977016, 31317897, 32181690, 32597170, 33448471, 34335563, 35479655, 35679653, 36362380,
     40370235, 41126782, 42047464, 44210863, 45032676, 45485453, 45927401, 46440611, 47648021, 48332713, 51739879,
     53661087, 54013763, 55671099, 59729554, 61031400, 61152946, 62094075, 63334100, 63982252, 64126215, 67064863,
     68090430, 68890150, 69771650, 70492097, 73093292, 73179931, 73734016, 73799297, 76592074, 78130473, 78754798,
     80779631, 82434243, 83414845, 85057940, 85251139, 88819311, 89561647, 90331595, 92828269, 93468391, 94424903,
     95269536, 96674583, 99147115, 99304223, 100683780, 101286921, 102423259, 106222561, 107513954, 110484789,
     112624349, 113305153, 113420780, 114986792, 115331335, 116721365, 116763864, 119418978, 120058202, 123876716,
     124130078, 124160561, 124874359, 125866935, 127869582, 128668997, 130982132, 131187052, 131384155, 132021146,
     134138723, 135387833, 137108804, 140681630, 141774984, 142665527, 144009028, 146443879, 149607927, 150768349,
     151574645, 155152577, 155654187, 157120970, 160132832, 160239672, 160418454, 160629526, 162443201, 162528946,
     162719409, 163574244, 165243500, 166151622, 167651444, 167813760, 167890012, 169054168, 170539766, 170641609,
     170790480, 171077223, 171423306, 173382749, 173998398, 179781823, 179893993, 180122344, 182400879, 183411374,
     183956080, 184023701, 186025822, 186319462, 186515028, 187224835, 189123445, 191746044, 192011848, 192144662,
     192890972, 193441337, 193630982, 194555696, 194849625, 197904750, 198270074, 198569232, 199067326, 199465362,
     205702616, 205865378, 206968102, 207696508, 208473827, 208757599, 211569286, 211837048, 212570096, 213442202,
     214701108, 216976425, 217255176, 217366958, 217741564, 218086772, 218402158, 220008410, 223853002, 224386961,
     225206489, 226685222, 228238345, 228416869, 230451582, 231055196, 231130722, 231510218, 234952848, 235602988,
     235717603, 238086790, 238805521, 239086781, 243268500, 245805104, 247158300, 249204106, 259775936, 259987335,
     260249539, 260384651, 260885593, 262652406, 265666827, 265828471, 267051983, 268534122, 269300646, 269874004,
     270482169, 271154775, 273614210, 275336225, 276627875, 277408629, 277424909, 278354125, 280443227, 282166665,
     283289408, 287574811, 288902764, 289014555, 289309389, 290144124, 290549876, 290611941, 291102434, 292546319,
     292637906, 293513631, 294371513, 294372456, 295612903, 298210528, 298231632, 298897287, 299353983, 300092115,
     300583166, 301398973, 301879226, 303866189, 305299176, 305582067, 307373674, 307636141, 310451055, 311237942,
     312075188, 312781745, 313625496, 314437215, 315451863, 317997185, 318900555, 323335434, 324190312, 324193002,
     324390157, 327100855, 327715138, 329258352, 329526730, 331366326, 332153447, 334861288, 334919104, 336292270,
     338983665, 339326621, 340794440, 343134217, 344540424, 345491570, 345986797, 346756539, 347426753, 347546502,
     348434394, 349498903, 349737700, 350462422, 350632994, 352966259, 352968622, 354475635, 354929134, 355542822,
     358129016, 368634316, 369838051, 370079072, 373881839, 373954283, 375344485, 376042404, 376166339, 377421127,
     378586103, 381284493, 381572471, 381697337, 382078685, 383846673, 384514494, 385791639, 385984975, 386980639,
     388228381, 388315594, 389591731, 389748396, 391427423, 392855032, 393129880, 393476156, 393785983, 394403010,
     397124802, 397829750, 397872372, 398130330, 398829626, 400834600, 401805213, 402115549, 403640403, 403922823,
     404692701, 405733259, 406062999, 407609872, 411639501, 412153217, 413115262, 413358795, 413663015, 415231706,
     415284345, 416377968, 416476929, 419649117, 420386675, 421301058, 422826407, 423476028, 423488105, 423774920,
     424366277, 424384242, 424533280, 428303226, 428737660, 429722455, 430850087, 431047948, 431543995, 434254977,
     437891125, 444256040, 445179701, 445394151, 446213524, 446752005, 446976526, 447274635, 447546836, 448079510,
     449171431, 450478112, 453541063, 454569482, 456373151, 456525339, 458688929, 459203799, 459239886, 460227301,
     460725799, 462092719, 462287754, 462855242, 466259040, 467453533, 471124586, 471489242, 471879750, 472619678,
     473539760, 474465284, 475154773, 477627399, 478289343, 481179241, 481413353, 481539702, 484178863, 486083981,
     486634675, 488629431, 491711700, 492614022, 493013046, 495823042, 497439685, 497903345, 501353684, 502438951,
     503391447, 503942300, 505033754, 505333139, 506132576, 507894840, 508747923, 509001679, 509674032, 510621750,
     511112199, 511285772, 515833466, 516514806, 517574195, 518119196, 519796017, 521295921, 521571537, 524395807,
     525886399, 528149235, 529023126, 529906344, 530836243, 531085418, 533922222, 534974451, 535305241, 535384563,
     535548874, 535574596, 539040129, 542671046, 546647847, 547745392, 548270336, 548436248, 548645879, 548662022,
     550087614, 557283503, 558359552, 559601039, 561781533, 564607942, 565297595, 566707449, 566839708, 569637045,
     571641073, 571652665, 571994891, 572965547, 573523994, 579498811, 580456390, 581639381, 582948099, 584159197,
     584401490, 584702789, 584760550, 586071668, 587764056, 588339315, 589989660, 590465192, 590928739, 593731029,
     595395274, 595562376, 595670800, 596519380, 600309560, 601259745, 603213139, 603328730, 606981637, 607009433,
     608060863, 609122190, 616677864, 617740113, 617916927, 619031974, 619886375, 620829667, 620934603, 621792998,
     623911099, 624760661, 626586872, 627279143, 628321548, 630811914, 633943674, 636553833, 636632055, 638882815,
     640747313, 640993950, 644376879, 644930626, 646689712, 649673488, 650426322, 651004783, 651317354, 652004353,
     653520887, 658684970, 659103743, 660728885, 661541578, 661639585, 663605197, 664501184, 665603955, 667086941,
     667804041, 668165106, 669385393, 669809644, 670057129, 672143142, 673298706, 673948111, 674808417, 675650974,
     676134763, 676576872, 678946752, 681159669, 682774760, 684238880, 685870135, 690974789, 692786917, 695138203,
     696018334, 696620553, 696936056, 697332689, 697352393, 699455242, 699987754, 704101924, 708449168, 708735620,
     710102900, 713112993, 714721675, 715329058, 716225241, 717670686, 721626624, 722459082, 724041483, 724969219,
     726741093, 727026507, 727094693, 728814527, 730757329, 730907708, 731161428, 732266782, 732826958, 733717130,
     736296761, 736299693, 736895365, 736931921, 739506069, 744504260, 746462832, 746672738, 749059556, 749731819,
     750028939, 750686307, 750828744, 753475548, 754201596, 755018294, 756700967, 757744441, 759060552, 759362853,
     760362696, 761411808, 762659358, 765056061, 765712275, 767586006, 767705753, 769770100, 769991745, 770233582,
     776870049, 777451070, 777456024, 778086260, 778494988, 779221108, 779325867, 780746435, 782315675, 783606009,
     784039066, 784538268, 785850603, 789304147, 790168521, 790603227, 792021838, 792266532, 793526745, 793584461,
     794054179, 795328015, 800393689, 804143278, 805665592, 809409635, 811825394, 811931490, 815320990, 817649382,
     818716102, 823082360, 823701604, 826456896, 826750366, 828116759, 828664001, 828707090, 829164135, 832261636,
     832455610, 835888967, 835908269, 836690684, 837266363, 837641293, 838451281, 839770827, 840700413, 842205827,
     842815791, 844849706, 846854520, 848207519, 849137841, 849256184, 850999212, 851797196, 852047422, 852286866,
     852925801, 852970204, 853374990, 853941941, 855053502, 856671585, 856848452, 856851714, 857133817, 857513419,
     857529764, 859751212, 863727103, 864088001, 864802579, 865581180, 869590528, 870611028, 873795712, 874264022,
     879944610, 883664714, 885807712, 889018012, 890437972, 890505222, 891649570, 891929768, 893829620, 893845899,
     894097188, 894479562, 894834620, 896107400, 896591606, 896675526, 898051334, 898785698, 898857049, 899916301,
     901011198, 904328179, 904406351, 904518674, 904742091, 905484932, 906155231, 906589224, 908427712, 909215205,
     911666265, 912193648, 915264085, 917293384, 918287028, 919756036, 924242630, 925173009, 925407377, 926011655,
     926337494, 927936720, 928142475, 929623066, 930293302, 930781786, 931212840, 931219192, 932404877, 934041585,
     937804436, 938173245, 939022548, 939612015, 941530685, 941604005, 943202966, 943904045, 944287568, 944807066,
     948156608, 949888275, 950814572, 951008692, 952362711, 952885221, 952931935, 952967767, 954245205, 956237342,
     956892501, 957478826, 958851125, 959127049, 960671631, 961199142, 961857541, 962113078, 965248622, 966564339,
     970715056, 973476038, 973975773, 977000076, 978159310, 980470939, 980826297, 981244308, 982179297, 984840092,
     984885883, 987490164, 988527907, 989230340, 989749199, 989955771, 990849052, 990872873, 992125893, 992336688,
     992627088, 993043544, 995322102, 996260709, 998300525, 999895841]
arr3 = \
    [2, 3, 5, 6, 8, 10, 13, 21, 34, 36, 41, 48, 53, 55, 59, 62, 71, 76, 77, 79, 82, 85, 88, 89, 90, 92, 94, 100, 107,
     127, 135, 144, 151, 155, 170, 174, 175, 177, 178, 213, 229, 233, 254, 258, 262, 265, 266, 285, 302, 364, 377, 417,
     428, 431, 440, 463, 477, 577, 593, 679, 685, 686, 705, 706, 748, 779, 941, 957, 1096, 1114, 1116, 1145, 1146, 1211,
     1256, 1518, 1550, 1775, 1800, 1801, 1850, 1852, 1959, 2035, 2459, 2507, 2871, 2914, 2917, 2995, 2998, 3170, 3291,
     3977, 4057, 4646, 4714, 4718, 4845, 4850, 5129, 5326, 6436, 6564, 7517, 7628, 7635, 7840, 7848, 8299, 8617, 10413,
     10621, 12163, 12342, 12353, 12685, 12698, 13428, 13943, 16849, 17185, 19680, 19970, 19988, 20525, 20546, 21727,
     27262, 27806, 31843, 32312, 32341, 33210, 33244, 35155, 44111, 44991, 51523, 52282, 52329, 53735, 53790, 56882,
     71373, 72797, 83366, 84594, 84670, 86945, 87034, 92037, 115484, 117788, 134889, 136876, 136999, 140680, 140824,
     148919, 186857, 190585, 218255, 221470, 221669, 227625, 227858, 240956, 308373, 353144, 358346, 358668, 368305,
     368682, 389875, 571399, 579816, 595930, 596540, 630831, 924543, 938162, 964235, 965222, 1205687, 1495942, 1517978,
     1560165, 1561762, 2420485, 2456140, 2524400, 2526984, 3504731, 3831446, 3916427, 3974118, 4002090, 4084565,
     4509148, 4559662, 5348874, 6336912, 6430258, 6608965, 9639665, 10166759, 10253339, 10693530, 11791075, 12573186,
     15167813, 15784914, 16590251, 17242347, 17302495, 17453914, 17960008, 18395525, 22466942, 24130340, 24814929,
     25055001, 26147497, 26843590, 28600458, 29632548, 30143678, 31619589, 33316575, 33324705, 33929823, 34491960,
     36660636, 37023576, 38566553, 39005554, 39161190, 39751927, 41424002, 42470682, 43433841, 44450796, 44603755,
     49542081, 51204445, 53280589, 54160086, 54354920, 55016892, 55350758, 55688772, 58155893, 58213146, 59293127,
     59410084, 59813293, 61358327, 61752966, 62585447, 62856338, 63699870, 64127901, 69342941, 70257310, 71644382,
     71860863, 72963580, 73173493, 73923256, 74629208, 75078994, 77252482, 78358668, 78535889, 78780034, 81857328,
     84163423, 87339761, 91189193, 91410480, 92243700, 92322190, 94442269, 94942054, 95339444, 96904829, 97226016,
     101168719, 101460910, 103560098, 104051625, 105213329, 105444809, 105605074, 108051430, 108206549, 108487404,
     109069670, 112782136, 113823258, 114556687, 114581094, 115697128, 115728631, 116531844, 116822945, 118045433,
     120540898, 120734292, 122808639, 122871447, 123788160, 125346258, 125991846, 128161209, 129711782, 131971057,
     132477044, 133434449, 133844372, 138298540, 140182550, 140586965, 142236358, 143225417, 143632237, 144897975,
     145478161, 147313205, 148615559, 149473046, 151964835, 153558532, 153607150, 155499266, 155580401, 157193429,
     157808818, 159054382, 164746944, 166422752, 166453690, 166629517, 166862696, 167077932, 167222203, 168161720,
     168284247, 168766097, 169628320, 170904526, 172726498, 173212714, 173821355, 176089878, 177794179, 178319632,
     179820995, 179869583, 180600370, 180992422, 181798638, 182195168, 182612467, 183922607, 185263935, 186812612,
     189278070, 191371379, 191529936, 193075051, 193307317, 193684463, 193939438, 195156533, 195484292, 198067435,
     199822054, 200154734, 200719334, 203128800, 203616626, 206171095, 206777056, 207983486, 208360317, 210547395,
     212506844, 213478317, 214944805, 217741483, 219020281, 220542940, 220783823, 224112195, 225746076, 226065075,
     226905308, 229389005, 229863650, 230668040, 231194337, 231764785, 236327265, 237147722, 238624580, 239949153,
     241981840, 242845440, 243892913, 244017096, 244160600, 245127129, 246576704, 246610966, 248887329, 254886138,
     257421166, 257841025, 258468561, 262629345, 262665495, 262762914, 263027728, 264229836, 266123118, 267667749,
     268874526, 271003053, 272371305, 272904197, 273299604, 276890798, 277819526, 278784802, 281035594, 281658085,
     282958499, 283402734, 284239493, 284773090, 285026534, 285515483, 286009375, 289353808, 289428658, 290983106,
     291017166, 291695203, 293068921, 293084175, 293414793, 294445840, 298140488, 298222421, 298665843, 299614676,
     300124272, 300315863, 301669670, 302294777, 303354591, 303708275, 304306582, 304924680, 308204204, 310166858,
     310727680, 310896278, 311550974, 311693559, 312298447, 312773231, 314249724, 318855480, 322624549, 325306349,
     331678071, 332532249, 333186240, 334045554, 334295613, 334752625, 335019247, 337516550, 338405759, 338996818,
     339763698, 339899334, 340132342, 340795510, 341116555, 343424680, 343611022, 345417769, 346347365, 348097870,
     348261260, 348776328, 349500598, 351418413, 352664533, 353408396, 354449350, 355755401, 356796223, 357460525,
     358292157, 358416754, 360011320, 360079910, 362145391, 363234555, 363438822, 364928424, 365024379, 365538282,
     367614899, 372971424, 373348772, 375585767, 376890463, 377564515, 378912622, 380189427, 380659236, 380880228,
     382703926, 382995165, 383519034, 385283571, 387825679, 389058508, 389313630, 389910494, 390653935, 392445625,
     393487349, 393958446, 395245624, 395492856, 397431804, 398082099, 400598455, 400686579, 403253702, 403678723,
     405222823, 405317212, 407157192, 408277694, 412438744, 413775940, 415016507, 415219991, 418698794, 423298204,
     423350581, 425261493, 426156524, 426235865, 427575935, 428028330, 430431796, 432935904, 433227271, 433913255,
     434021017, 434683477, 435438804, 437858207, 438668874, 438683619, 439498831, 439718290, 443006180, 446529542,
     449002765, 450536872, 452401398, 453418334, 454118900, 455726329, 456232318, 456603378, 458138179, 459507264,
     460408329, 461627484, 461964842, 464332703, 464497564, 466138859, 467861035, 468890929, 469940202, 470026554,
     472336404, 472400093, 472878399, 473938566, 474891699, 475113346, 476869200, 477737466, 477828507, 477878434,
     480761205, 481495011, 482439667, 485433478, 487641801, 488183219, 489851845, 491410871, 493005254, 493169116,
     494609881, 499506408, 502056317, 502844009, 503290103, 505822061, 507485567, 508336407, 511561764, 511579408,
     515699165, 517225501, 518133008, 518226911, 519107220, 520442400, 520914712, 525798712, 527046372, 527971816,
     530872751, 532041816, 533871877, 534360006, 536789796, 537599343, 539693765, 539724460, 541541070, 541588961,
     542369991, 544413729, 546150435, 546443734, 547350265, 548655173, 549450196, 550298282, 551039142, 555884301,
     555891567, 559161289, 561740141, 561941178, 562401959, 563386462, 564549841, 566768771, 567691477, 569176194,
     569580314, 575949890, 578198155, 578982027, 580218740, 581004033, 583472360, 585199059, 585792484, 585898907,
     586427773, 590038877, 590057018, 590238769, 590468380, 590825839, 591254539, 591818188, 592060089, 593049903,
     597414549, 598884830, 599763447, 601916233, 602224485, 603031916, 603272640, 603461240, 604941229, 605895944,
     606322194, 608636231, 612338014, 615208238, 616018077, 616176033, 617361022, 618759805, 620050821, 620164443,
     622561882, 626289692, 626880004, 629621957, 630737575, 630976938, 631338366, 634567980, 635172621, 635470131,
     636420717, 636735376, 638911217, 640964740, 643494983, 644041705, 650734408, 651561500, 652471013, 656335212,
     657496902, 657780036, 657800319, 661009608, 661943410, 663724973, 665936391, 665955867, 666413759, 666896952,
     668306278, 668425104, 671660080, 672298631, 675720848, 675850467, 676337119, 676791485, 678914881, 682193154,
     684884375, 687086291, 687289044, 688326654, 688805517, 688906840, 689774052, 693500433, 694439783, 695717378,
     696096390, 697576315, 699119677, 700084838, 700677712, 701493809, 701694566, 701937397, 703007627, 704344737,
     707087284, 708202625, 708831405, 708871437, 709557730, 709681509, 711350997, 714002453, 714018685, 714187041,
     714918313, 716475606, 717176954, 717214219, 719324100, 719635705, 721171279, 721405376, 722256336, 724578781,
     726515524, 727130958, 727870552, 728928708, 730833659, 731745520, 732479026, 733739169, 734576801, 737318078,
     743966639, 744020403, 746476494, 746614338, 749108696, 749455331, 751257857, 752093345, 753008955, 753286896,
     753471644, 755407473, 756733629, 756980419, 757217074, 758087455, 758655449, 758709389, 758889848, 762624660,
     763157678, 765463195, 765619991, 766603386, 767877533, 768439551, 769160809, 770431082, 770651798, 773508942,
     776650514, 777224043, 777421126, 777977615, 778229427, 779118106, 781261110, 783273202, 783622451, 786756121,
     788108772, 788926126, 790502325, 797712880, 799756012, 800473552, 801114800, 802912146, 802922943, 803738996,
     805203848, 805321445, 805381056, 807988674, 809676893, 815846526, 818504672, 821874013, 822896361, 823649914,
     823927420, 824165179, 824573829, 825274383, 825947487, 826814013, 827148472, 828552957, 832755181, 832937699,
     834191669, 834962652, 836644759, 837225252, 838763304, 840232208, 845509639, 851587645, 852300110, 853343156,
     854702560, 856185391, 858824325, 858963867, 859452283, 861127311, 861412347, 862665826, 862678758, 864380345,
     865461085, 871386868, 873767170, 874492133, 874787104, 876011808, 876654909, 877071302, 877319588, 878536993,
     880677047, 881239887, 881598639, 881888628, 883567019, 884438668, 884797082, 885773728, 887011459, 889648065,
     891503932, 893335464, 893910176, 895950263, 896600877, 898352618, 899621329, 901061628, 901166144, 901350385,
     901697713, 902342948, 904413299, 904516917, 905461196, 907110699, 907748371, 910248594, 910422311, 910882806,
     912559732, 913002234, 918028097, 919597742, 920099850, 921998778, 922261728, 923200623, 924381388, 924629636,
     926272617, 929262340, 932435837, 934670279, 935623266, 936045126, 938443014, 939135676, 941168116, 941586662,
     943504394, 945088728, 947189986, 949316674, 951129193, 953403358, 953561021, 955897323, 958011752, 959294514,
     959632657, 963971474, 964840067, 966401177, 966609676, 970719919, 971874537, 972584348, 972916703, 975674317,
     975679210, 977669038, 979496732, 980618570, 980817727, 983110557, 984120047, 984676004, 985464753, 986333295,
     987204952, 987965771, 989837914, 990048311, 990758846, 991515606, 992367201, 993349328, 993666396, 995552914,
     996489140, 998275927, 999136057, 999312751]
# print('sum = ', Solution.lenLongestFibSubseq(self=Solution, arr=b))
# print('sum = ', Solution.lenLongestFibSubseq1(self=Solution, arr=b))
print('result ', Solution.fib(self=Solution, arr=arr3))
# print('result ', Solution.fib(self=Solution, arr=c))
# print('result ', Solution.fib(self=Solution, arr=arr))


