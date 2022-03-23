f = open("players.txt", "r")
player_stats = f.read()

names_qb = []
points_qb = []
names_wr = []
points_wr = []
names_te = []
points_te = []
names_rb = []
points_rb = []

for line in player_stats:
    one = line.split("\n")
    points = int(int(one[2])/25 + int(one[3])* 4 + int(one[4])/10 + int(one[5])*6 + int(one[6])/10 + int(one[7])*6) 
    
    if one[0] == "QB":
        names_qb.append(one[1])
        points_qb.append(points)
    elif one[0] == "WR":
        names_wr.append(one[1])
        points_wr.append(points)
    elif one[0] == "TE":
        names_te.append(one[1])
        points_te.append(points)
    elif one[0] == "RB":
        names_rb.append(one[1])
        points_rb.append(points)

for i in points_qb:
    if points_qb[i] == max(points_qb):
        index_qb = points_qb[i].index()
        name_qb = names_qb[index_qb]
        points_qb.remove(points_qb[i])
        qb_points = points_qb[i]

for i in points_te:
    if points_te[i] == max(points_te):
        index_te = points_te[i].index()
        name_te = names_te[index_qb]
        points_te.remove(points_te[i])
        te_points = points_te[i]

for i in points_wr:
    if points_wr[i] == max(points_wr):
        index_wr1 = points_wr[i].index()
        name_wr1= names_wr[index_wr1]
        points_wr.remove(points_wr[i])
        wr1_points = points_wr[i]

for i in points_wr:
    if points_wr[i] == max(points_wr):
        index_wr2 = points_wr[i].index()
        name_wr2= names_wr[index_wr2]
        points_wr.remove(points_wr[i])
        wr2_points = points_wr[i]

for i in points_rb:
    if points_rb[i] == max(points_rb):
        index_rb1 = points_rb[i].index()
        name_rb1= names_rb[index_rb1]
        points_rb.remove(points_rb[i])
        rb1_points = points_rb[i]

for i in points_rb:
    if points_rb[i] == max(points_rb):
        index_rb2 = points_rb[i].index()
        name_rb2= names_rb[index_rb2]
        points_rb.remove(points_rb[i])
        rb2_points = points_rb[i]

max_rb = max(points_rb)
max_wr = max(points_wr)
max_te = max(points_te)

if max_rb > max_wr and max_rb > max_te:
    index_flex = points_rb.index(max_rb)
    flex_player = names_rb[index_flex]
    flex_points = max_rb
elif max_wr > max_rb and max_wr > max_te:
    index_flex = points_wr.index(max_wr)
    flex_player = names_wr[index_flex]
    flex_points = max_wr
elif max_te > max_wr and max_te > max_rb:
    index_flex = points_te.index(max_te)
    flex_player = names_te[index_flex]
    flex_points = max_te

print("QB", name_qb, qb_points)
print("RB1", name_rb1, rb1_points)
print("RB2", name_rb2, rb2_points)
print("WR1", name_wr1, wr1_points)
print("WR2", name_wr2, wr2_points)
print("TE", name_te, te_points)
print("FLEX", flex_player, flex_points)




    


#print(list)
    