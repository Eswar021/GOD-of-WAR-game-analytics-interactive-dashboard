import csv
import re
# HTML content (your HTML string)
html_content = '''

<html>
<head>
<title>god-of-war</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">
<img src="god-of-war.gif" width="1920" height="1080" border="0" alt="" usemap="#god_of_war_Map">
<map name="god_of_war_Map">
<area shape="poly" alt="" coords="926,533, 925,530, 919,525, 915,527, 913,530, 913,548, 915,550, 919,552, 923,551, 925,547, 925,533, 926,533" href="inner">
<area shape="poly" alt="" coords="940,536, 935,520, 923,512, 913,512, 904,517, 898,525, 897,538, 899,550, 906,559, 915,564, 926,563, 936,555, 940,540, 940,536" href="outer">
<area shape="poly" alt="" coords="1087,660, 1086,659, 1072,656, 1058,657, 1055,659, 1058,661, 1066,662, 1074,662, 1087,660" href="inner">
<area shape="poly" alt="" coords="528,526, 519,498, 510,485, 496,477, 479,475, 462,479, 450,485, 441,496, 433,524, 434,553, 437,566, 443,579, 459,595, 478,601, 494,599, 506,593, 514,586, 521,578, 525,564, 527,550, 528,526" href="inner">
<area shape="poly" alt="" coords="720,522, 717,512, 710,499, 700,488, 676,479, 656,479, 636,481, 639,486, 636,495, 636,504, 639,521, 639,525, 642,527, 646,533, 646,547, 645,551, 642,553, 639,557, 639,596, 647,597, 672,596, 687,593, 699,586, 713,566, 720,543, 720,522" href="inner">
<area shape="poly" alt="" coords="1600,483, 1589,479, 1578,479, 1572,481, 1570,486, 1570,513, 1570,513, 1570,526, 1573,529, 1591,527, 1605,517, 1611,505, 1609,493, 1600,483" href="inner">
<area shape="poly" alt="" coords="958,643, 952,650, 958,656, 958,643" href="red">
<area shape="poly" alt="" coords="939,643, 939,654, 945,649, 940,643, 939,643" href="red">
<area shape="poly" alt="" coords="955,639, 943,637, 942,639, 948,645, 955,639" href="red">
<area shape="poly" alt="" coords="844,546, 840,523, 827,534, 844,546" href="red">
<area shape="poly" alt="" coords="1019,607, 1022,620, 1025,624, 1039,628, 1037,616, 1035,612, 1031,610, 1019,607" href="red">
<area shape="poly" alt="" coords="962,412, 960,412, 941,431, 941,436, 958,435, 960,434, 961,433, 962,412" href="red">
<area shape="poly" alt="" coords="793,519, 797,521, 801,525, 801,549, 821,534, 812,527, 803,521, 793,519" href="red">
<area shape="poly" alt="" coords="960,395, 953,396, 950,402, 949,408, 948,408, 947,399, 939,401, 940,425, 942,426, 955,413, 960,405, 960,395" href="red">
<area shape="poly" alt="" coords="939,684, 948,680, 958,681, 959,670, 957,661, 948,653, 943,657, 939,662, 939,684" href="red">
<area shape="poly" alt="" coords="963,501, 961,502, 959,503, 961,508, 966,515, 967,524, 967,528, 966,530, 963,535, 963,540, 964,544, 968,543, 967,560, 965,564, 961,569, 961,575, 995,575, 994,570, 993,567, 987,562, 986,554, 985,543, 993,543, 1000,543, 1007,548, 1007,526, 997,531, 986,531, 985,513,
1000,513, 1007,516, 1012,522,
1013,522, 1016,501, 997,501, 963,501" href="outer">
<area shape="poly" alt="" coords="989,405, 988,407, 976,401, 970,397, 968,391, 966,391, 964,439, 970,436, 976,439, 980,440, 984,439, 987,442, 1001,448, 1008,453, 1024,466, 1024,458, 1028,455, 1036,455, 1038,455, 1040,453, 1042,440, 1049,438, 1045,434, 1043,435, 1042,434, 1041,422, 1035,427, 1027,423,
1028,421, 1023,420,
1018,419, 1014,414, 1009,415, 1010,410, 1009,409, 1002,417, 1003,410, 994,407, 992,408, 989,405" href="red">
<area shape="poly" alt="" coords="989,405, 990,409, 990,409, 989,405" href="red">
<area shape="poly" alt="" coords="992,408, 990,409, 992,408" href="red">
<area shape="poly" alt="" coords="936,401, 930,406, 924,409, 923,409, 914,408, 909,413, 892,420, 887,420, 886,419, 889,417, 886,416, 886,404, 881,410, 880,416, 880,418, 870,420, 868,420, 866,423, 865,428, 861,432, 847,436, 847,437, 851,442, 857,445, 870,448, 873,451, 872,452, 858,450, 876,471, 878,464,
884,460, 902,449,
920,440, 936,439, 936,401" href="red">
<area shape="poly" alt="" coords="843,438, 834,455, 829,458, 828,465, 834,461, 839,457, 835,466, 827,471, 822,474, 821,481, 818,483, 820,487, 826,493, 825,494, 819,493, 815,488, 814,482, 815,475, 808,472, 806,471, 807,491, 803,492, 806,495, 803,503, 802,510, 804,517, 824,531, 843,516, 844,515, 846,506,
850,498, 856,488,
862,479, 867,475, 873,474, 865,465, 855,460, 846,456, 847,454, 859,457, 843,438" href="red">
<area shape="poly" alt="" coords="931,501, 908,501, 894,507, 883,517, 878,533, 880,552, 885,563, 894,571, 911,575, 927,575, 946,566, 956,553, 958,536, 958,532, 954,517, 945,506, 931,501" href="outer">
<area shape="poly" alt="" coords="876,606, 868,599, 851,573, 846,557, 843,550, 823,536, 805,553, 804,558, 806,562, 815,586, 824,607, 819,604, 813,607, 819,610, 825,612, 828,619, 831,627, 838,633, 842,633, 858,622, 851,619, 851,618, 865,616, 876,606" href="red">
<area shape="poly" alt="" coords="1083,653, 1072,651, 1062,649, 1047,648, 1038,645, 1045,650, 1044,653, 1021,653, 1016,650, 1016,644, 1019,648, 1023,645, 1022,641, 1025,639, 1032,637, 1040,633, 1035,630, 1024,628, 1020,626, 1018,622, 1013,605, 1000,617, 986,627, 970,634, 972,638, 971,639, 969,638,
964,637, 962,642, 963,649,
963,677, 966,682, 981,685, 989,683, 993,680, 990,686, 996,686, 996,683, 1010,682, 1010,684, 1004,688, 1052,688, 1099,682, 1098,676, 1110,679, 1111,677, 1105,676, 1100,674, 1094,674, 1096,679, 1094,681, 1081,681, 1080,680, 1087,676, 1087,675, 1060,679, 1066,675, 1078,672, 1087,667, 1099,665, 1105,664, 1110,666, 1116,659,
1115,650, 1111,656, 1105,656, 1101,656, 1083,653" href="red">
<area shape="poly" alt="" coords="820,660, 819,662, 816,662, 812,659, 808,658, 804,659, 787,655, 781,655, 777,657, 777,654, 764,650, 764,652, 773,659, 773,660, 767,658, 768,660, 777,665, 792,673, 797,675, 799,673, 813,677, 816,679, 817,681, 813,682, 821,682, 828,686, 832,683, 836,685, 839,687, 855,687,
858,687, 859,683,
865,686, 875,688, 885,687, 905,685, 913,684, 921,681, 924,682, 926,680, 929,682, 933,683, 935,679, 935,639, 918,633, 882,612, 877,611, 862,622, 869,624, 869,626, 857,625, 843,638, 848,638, 853,639, 856,644, 863,645, 872,650, 879,656, 868,659, 857,657, 845,656, 842,657, 836,661, 830,658, 829,663, 826,660, 820,660" href="red">
<area shape="poly" alt="" coords="826,660, 822,657, 817,659, 826,660" href="red">
<area shape="poly" alt="" coords="817,659, 817,659, 820,660, 817,659" href="red">
<area shape="poly" alt="" coords="1093,544, 1092,543, 1091,538, 1086,538, 1073,538, 1072,536, 1087,535, 1079,527, 1080,526, 1092,535, 1093,534, 1091,529, 1091,523, 1088,517, 1089,513, 1088,506, 1085,500, 1080,487, 1076,481, 1075,474, 1074,471, 1064,459, 1060,454, 1060,454, 1059,442, 1044,442, 1042,458,
1026,458, 1028,470,
1037,482, 1046,498, 1046,501, 1046,507, 1049,512, 1046,534, 1064,535, 1064,536, 1050,536, 1058,545, 1057,546, 1047,537, 1045,538, 1045,552, 1041,555, 1041,562, 1018,603, 1027,606, 1035,608, 1039,612, 1041,620, 1044,630, 1047,621, 1054,618, 1060,612, 1070,598, 1073,595, 1074,587, 1077,580, 1080,573, 1081,564, 1087,559, 1086,555,
1090,553, 1095,550, 1093,544" href="red">
<area shape="poly" alt="" coords="1504,607, 1501,603, 1497,602, 1489,599, 1484,592, 1479,584, 1476,577, 1475,572, 1469,558, 1457,529, 1455,526, 1445,515, 1449,510, 1446,506, 1443,502, 1443,496, 1442,493, 1429,462, 1423,458, 1406,459, 1402,461, 1389,490, 1378,518, 1356,572, 1347,592, 1339,600, 1328,603,
1324,605, 1322,609,
1322,615, 1325,617, 1331,617, 1332,617, 1375,617, 1375,608, 1369,601, 1368,594, 1372,583, 1384,550, 1395,522, 1402,510, 1405,514, 1415,537, 1419,548, 1425,560, 1429,570, 1432,581, 1439,592, 1437,597, 1432,604, 1431,610, 1431,617, 1434,618, 1455,618, 1494,618, 1502,617, 1505,615, 1504,607" href="outer">
<area shape="poly" alt="" coords="575,543, 575,538, 575,532, 574,528, 568,526, 566,508, 565,503, 561,500, 559,494, 548,479, 534,469, 517,462, 496,459, 468,457, 449,460, 431,466, 421,471, 416,476, 410,481, 405,487, 397,501, 396,503, 397,509, 395,514, 393,521, 391,525, 387,527, 384,530, 384,551, 391,554,
393,557, 394,564,
397,570, 400,581, 417,603, 441,615, 468,619, 496,618, 516,615, 535,607, 544,601, 552,592, 557,586, 560,578, 563,567, 566,556, 568,554, 575,550, 575,543" href="outer">
<area shape="poly" alt="" coords="758,517, 755,499, 746,484, 725,468, 699,462, 686,461, 673,460, 630,459, 611,460, 587,460, 587,463, 587,470, 593,475, 595,478, 597,482, 597,486, 598,490, 600,496, 598,502, 598,506, 598,521, 598,525, 595,527, 590,533, 591,545, 591,550, 596,553, 599,557, 598,586, 596,595,
589,602, 587,604,
588,615, 618,615, 657,616, 688,614, 709,607, 727,597, 743,581, 752,563, 757,544, 756,526, 757,521, 758,517" href="outer">
<area shape="poly" alt="" coords="379,548, 372,547, 346,547, 303,547, 298,548, 297,553, 318,563, 322,566, 324,570, 324,591, 321,595, 313,598, 304,599, 280,598, 278,597, 266,589, 256,578, 251,572, 247,566, 243,548, 241,532, 243,517, 249,504, 257,492, 265,485, 274,481, 285,478, 297,477, 321,478, 342,488,
347,492, 360,507,
365,512, 367,496, 362,483, 366,473, 366,462, 366,458, 362,457, 346,457, 294,457, 271,459, 248,464, 236,470, 224,478, 213,488, 207,502, 206,505, 201,512, 199,520, 198,525, 194,527, 191,528, 190,532, 191,548, 193,551, 200,556, 202,566, 208,579, 216,591, 229,599, 230,601, 239,608, 250,613, 278,618, 299,619, 319,617, 323,617,
324,621, 324,631, 328,639, 338,653, 342,659, 352,669, 360,680, 364,683, 366,679, 366,662, 365,631, 366,582, 366,569, 373,558, 377,554, 379,548" href="outer">
<area shape="poly" alt="" coords="1350,459, 1343,459, 1324,460, 1300,459, 1298,460, 1296,462, 1296,469, 1301,475, 1306,478, 1307,482, 1292,538, 1285,566, 1278,552, 1276,546, 1274,541, 1271,535, 1269,528, 1268,525, 1245,469, 1242,461, 1238,459, 1229,459, 1224,462, 1214,484, 1198,519, 1185,546, 1178,561,
1176,561, 1174,546,
1170,532, 1165,504, 1159,477, 1167,472, 1169,459, 1097,459, 1097,465, 1097,470, 1102,472, 1112,475, 1119,483, 1124,501, 1127,520, 1134,555, 1146,610, 1150,616, 1157,618, 1166,617, 1172,615, 1176,606, 1180,597, 1189,575, 1203,549, 1220,511, 1227,528, 1236,553, 1247,576, 1248,582, 1249,585, 1261,616, 1265,618, 1287,617, 1291,608,
1292,599, 1296,592, 1297,588, 1298,580, 1303,562, 1305,556, 1310,538, 1315,520, 1319,505, 1324,487, 1330,477, 1339,472, 1349,470, 1350,459" href="outer">
<area shape="poly" alt="" coords="1694,659, 1692,650, 1673,624, 1645,589, 1640,583, 1637,576, 1631,566, 1625,559, 1612,539, 1620,536, 1642,521, 1644,518, 1650,501, 1650,483, 1643,472, 1638,467, 1631,464, 1630,462, 1626,460, 1587,458, 1564,459, 1553,459, 1541,459, 1521,459, 1518,460, 1516,461, 1516,468,
1517,472, 1525,479,
1528,488, 1529,497, 1529,516, 1528,523, 1522,527, 1520,529, 1519,531, 1519,547, 1520,551, 1523,553, 1528,555, 1529,560, 1529,571, 1530,579, 1528,588, 1525,597, 1518,603, 1516,607, 1516,617, 1518,617, 1579,616, 1583,613, 1584,607, 1580,602, 1572,593, 1571,588, 1571,582, 1570,566, 1570,553, 1572,553, 1581,567, 1590,581, 1616,620,
1627,635, 1630,637, 1643,641, 1682,656, 1692,660, 1694,659" href="outer">
<area shape="poly" alt="" coords="160,363, 160,481, 160,599, 160,717, 293,717, 427,717, 560,717, 693,717, 827,717, 960,717, 1093,717, 1227,717, 1360,717, 1493,717, 1627,717, 1760,717, 1760,599, 1760,481, 1760,363, 1627,363, 1493,363, 1360,363, 1227,363, 1093,363, 960,363, 827,363, 693,363, 560,363,
427,363, 293,363, 160,363"
href="bg">
<area shape="poly" alt="" coords="990,409, 990,409, 992,408, 990,409" href="red">
<area shape="poly" alt="" coords="820,660, 817,659, 820,660" href="red">
<area shape="poly" alt="" coords="826,660, 822,657, 817,659, 817,659, 826,660" href="red">
<area shape="poly" alt="" coords="989,405, 990,409, 989,405" href="red">
</map>
</body>
</html>
'''

# Extract coordinates and color from the HTML content
pattern = re.compile(r'<area[^>]*coords="([^"]+)"[^>]*href="([^"]+)"')
matches = pattern.findall(html_content)

# Prepare CSV data
csv_data = []
record_id = 1
image_height = 1080  # Height of the image

for match in matches:
    coords = match[0].split(',')
    color = match[1]
    for i in range(0, len(coords), 2):
        path_id = (i // 2) + 1
        x = coords[i]
        y = str(image_height - int(coords[i+1]))  # Flip the y-coordinate
        csv_data.append([record_id, path_id, x, y, color])
    record_id += 1

# Write to CSV file
csv_file = 'GOD_WAR.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['RecordID', 'PathID', 'x', 'y', 'ColorID'])
    writer.writerows(csv_data)

print(f"Coordinates and color IDs have been saved to {csv_file}")