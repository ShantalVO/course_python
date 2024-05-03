people = ['F1', 'F2', 'A1', 'A2', 'A3', 'S1', 'S2', 'S3', 'S4']

fellow = ['F1', 'F2']
associates = ['A1', 'A2', 'A3']
students = ['S1', 'S2', 'S3', 'S4']

pos_result = []

for m1 in people:
    for m2 in people:
        for m3 in people:
            pos_result.append((m1, m2, m3))

#print(len(pos_result))

for f in fellow:
    for a in associates:
        for s in students:
            cases_interest.append((f,a,s))
            cases_interest.append((f, s, a))
            cases_interest.append((a, f, s))
            cases_interest.append((a, f, s))

print(len(cases_interest))

proobability = len()
